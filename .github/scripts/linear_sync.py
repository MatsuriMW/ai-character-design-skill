#!/usr/bin/env python3
"""把仓库的变化同步到 Linear 的 ai-character-design-skill project。

用法（GitHub Actions 里调用）：
  python3 .github/scripts/linear_sync.py project   每次推送到 main：project 介绍刷新成 README 开头 +「能做什么」、当前版本、最近 10 次提交
  python3 .github/scripts/linear_sync.py release   发完新版本：project 发一条版本更新；提交说明里提到的卡（MAT-123）
                                                  各评论「已发布于」；基线卡评论完整更新说明；再刷新一次 project 介绍

环境变量：LINEAR_API_KEY（仓库 secret，没有就跳过）、LINEAR_PROJECT（project id）、LINEAR_BASELINE（基线卡，不填就不评论基线卡）、
LINEAR_TEAM（卡号前缀，默认取基线卡的前缀或 MAT）、README_FROM（只取 README 里这个标记之后的部分当介绍，比如中文说明的锚点）、
release 模式另需 TAG、PREV，以及当前目录下的 notes.md。
"""
import json
import os
import re
import subprocess
import sys
import urllib.request

MODE = sys.argv[1] if len(sys.argv) > 1 else "project"
KEY = os.environ.get("LINEAR_API_KEY", "").strip()
PROJECT = os.environ["LINEAR_PROJECT"]
BASELINE = os.environ.get("LINEAR_BASELINE", "").strip()
TEAM = os.environ.get("LINEAR_TEAM") or (BASELINE.split("-")[0] if BASELINE else "MAT")
README_FROM = os.environ.get("README_FROM", "")
REPO = os.environ["GITHUB_REPOSITORY"]
GH = f"https://github.com/{REPO}"


def sh(*args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout.strip()


def gql(query, variables=None):
    req = urllib.request.Request(
        "https://api.linear.app/graphql",
        data=json.dumps({"query": query, "variables": variables or {}}).encode(),
        headers={"Content-Type": "application/json", "Authorization": KEY},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        out = json.load(r)
    if out.get("errors"):
        raise RuntimeError(out["errors"])
    return out["data"]


def comment(identifier, body):
    # 卡不存在、没权限、已删或已归档：记一笔，不让流程失败。
    # 删掉的卡（在回收站里）按卡号还查得到，评论时才报 Entity not found，所以评论也要包在里面
    try:
        issue = gql("query($id:String!){issue(id:$id){id}}", {"id": identifier})["issue"]
        gql("mutation($i:CommentCreateInput!){commentCreate(input:$i){success}}",
            {"i": {"issueId": issue["id"], "body": body}})
    except Exception as e:
        print(f"跳过 {identifier}：{e}")
        return
    print(f"已评论 {identifier}")


def absolute_links(md):
    """README 里的相对链接换成 GitHub 上的绝对链接。"""
    return re.sub(r"\]\((?!https?://|#|mailto:)([^)]+)\)", lambda m: f"]({GH}/blob/main/{m.group(1)})", md)


def readme_parts():
    text = open("README.md", encoding="utf-8").read()
    if README_FROM and README_FROM in text:
        # 只要标记之后的部分（比如 README 末尾的中文说明）：整段当介绍，去掉它自己的二级标题
        part = text.split(README_FROM, 1)[1].strip()
        part = re.sub(r"^## [^\n]*\n+", "", part)
        return part, ""
    intro = []
    for line in text.splitlines()[1:]:  # 跳过标题
        if line.startswith("[English summary]") or line.strip() == "---":
            break
        intro.append(line)
    m = re.search(r"^## 能做什么\n(.*?)(?=^## )", text, re.S | re.M)
    return "\n".join(intro).strip(), (m.group(1).strip() if m else "")


def current_version():
    tag = os.environ.get("TAG")
    if tag:
        return tag
    try:
        return sh("gh", "release", "view", "--repo", REPO, "--json", "tagName", "-q", ".tagName")
    except Exception:
        return ""


def refresh_project():
    intro, features = readme_parts()
    ver = current_version()
    # 文件名（package.py、sync.sh）包进代码格式，免得 Linear 把它们当成网址自动加链接
    filename = re.compile(r"(?<![`\w/])([\w.-]+\.(?:py|sh|md|yml|zip|json))(?![`\w])")
    rows = sh("git", "log", "--no-merges", "-10", "--format=%h%x09%H%x09%ad%x09%s", "--date=short").splitlines()
    lines = []
    for row in rows:
        h, full, date, subj = row.split("\t", 3)
        subj = filename.sub(r"`\1`", subj)
        lines.append(f"- [`{h}`]({GH}/commit/{full}) {subj}（{date}）")
    commits = "\n".join(lines)
    parts = [
        "> 这一页由 GitHub Actions 从仓库自动同步，每次推送都会覆盖。要改介绍，改仓库的 README。",
        intro,
        f"**当前版本**：[{ver}]({GH}/releases/tag/{ver}) · [全部版本]({GH}/releases) · [仓库]({GH})" if ver else f"[仓库]({GH})",
    ]
    if features:
        parts += ["## 能做什么", features]
    parts += ["## 最近改动", commits]
    content = absolute_links("\n\n".join(parts))
    gql("mutation($id:String!,$i:ProjectUpdateInput!){projectUpdate(id:$id,input:$i){success}}",
        {"id": PROJECT, "i": {"content": content}})
    print("已刷新 project 介绍")


def release():
    tag, prev = os.environ["TAG"], os.environ["PREV"]
    url = f"{GH}/releases/tag/{tag}"
    notes = open("notes.md", encoding="utf-8").read()
    gql("mutation($i:ProjectUpdateCreateInput!){projectUpdateCreate(input:$i){success}}",
        {"i": {"projectId": PROJECT, "health": "onTrack", "body": f"🚀 **[{tag}]({url})** 已发布\n\n{notes}"}})
    print("已发 project 更新")
    log = sh("git", "log", "--no-merges", "--format=%B", f"{prev}..HEAD" if prev else "HEAD")
    ids = sorted(set(re.findall(rf"\b{TEAM}-\d+\b", log)) - {BASELINE}, key=lambda s: int(s.split("-")[1]))
    for i in ids:
        comment(i, f"🚀 已发布于 [{tag}]({url})")
    if BASELINE:
        comment(BASELINE, f"🚀 **[{tag}]({url})** 已发布\n\n{notes}")


if not KEY:
    print("没有配置 LINEAR_API_KEY，跳过 Linear 同步")
    sys.exit(0)
if MODE == "release":
    release()
refresh_project()
