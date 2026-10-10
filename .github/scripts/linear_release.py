#!/usr/bin/env python3
"""发完 GitHub Release 后同步到 Linear（release.yml 最后一步调用）。

- 上一版以来的提交说明里提到的每张卡（MAT-123），各留一条「已发布于 vX.Y.Z」的评论
- 基线卡（LINEAR_BASELINE，默认 MAT-96）留一条带完整更新说明的评论，当作版本记录
没有配 LINEAR_API_KEY 这个仓库 secret 时直接跳过，不影响发版。
"""
import json
import os
import re
import subprocess
import sys
import urllib.request

KEY = os.environ.get("LINEAR_API_KEY", "").strip()
TAG, PREV = os.environ["TAG"], os.environ["PREV"]
REPO = os.environ["GITHUB_REPOSITORY"]
BASELINE = os.environ.get("LINEAR_BASELINE", "MAT-96")
TEAM = BASELINE.split("-")[0]
URL = f"https://github.com/{REPO}/releases/tag/{TAG}"


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
    try:
        issue = gql("query($id:String!){issue(id:$id){id}}", {"id": identifier})["issue"]
    except Exception as e:  # 卡不存在或没权限：记一笔，不让发版失败
        print(f"跳过 {identifier}：{e}")
        return
    gql("mutation($i:CommentCreateInput!){commentCreate(input:$i){success}}",
        {"i": {"issueId": issue["id"], "body": body}})
    print(f"已评论 {identifier}")


if not KEY:
    print("没有配置 LINEAR_API_KEY，跳过 Linear 同步")
    sys.exit(0)

log = subprocess.run(["git", "log", "--no-merges", "--format=%B", f"{PREV}..HEAD"],
                     capture_output=True, text=True, check=True).stdout
ids = sorted(set(re.findall(rf"\b{TEAM}-\d+\b", log)) - {BASELINE}, key=lambda s: int(s.split("-")[1]))

for i in ids:
    comment(i, f"🚀 已发布于 [{TAG}]({URL})")

notes = open("notes.md", encoding="utf-8").read()
comment(BASELINE, f"🚀 **[{TAG}]({URL})** 已发布\n\n{notes}")
