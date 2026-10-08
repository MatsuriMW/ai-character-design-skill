#!/usr/bin/env python3
"""从一个 Obsidian 风格库（一个风格一篇笔记，frontmatter 写 type: 审美风格）生成 references/styles/服装风格.md。

风格库是正本：在 Obsidian 里加风格页、改单品、写「我的笔记」，跑一次这个脚本就同步进 skill。
页面格式见 references/styles/索引.md 的「用你自己的风格库」。

用法：
  python3 scripts/sync-styles.py <风格目录>
  JUESE_STYLE_DIR=<风格目录> python3 scripts/sync-styles.py
"""
import json
import os
import pathlib
import re
import sys

SKILL = pathlib.Path(__file__).resolve().parent.parent
OUT = SKILL / "references/styles/服装风格.md"


def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None
    fm_raw, body = m.groups()
    fm = {}
    for line in fm_raw.split("\n"):
        mm = re.match(r"^([^\s:#][^:]*):\s*(.*)$", line)
        if not mm:
            continue
        k, v = mm.group(1).strip(), mm.group(2).strip()
        if v.startswith("["):
            try:
                v = json.loads(v)
            except ValueError:
                v = [x.strip().strip('"') for x in v.strip("[]").split(",") if x.strip()]
        else:
            v = v.strip('"')
        fm[k] = v
    if fm.get("type") != "审美风格":
        return None
    quote = next((l[2:].strip() for l in body.split("\n") if l.startswith("> ")), "")
    sub = re.search(r"^## 细分\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    subs = [l.strip()[2:] for l in sub.group(1).split("\n") if l.strip().startswith("- ")] if sub else []
    # 「风格档案」：取每个 ### 小节的标题和正文，跳过只有链接的「品牌」小节
    essay = []
    arch = re.search(r"^## 风格档案\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    if arch:
        for m2 in re.finditer(r"^### (.+?)\n(.*?)(?=^### |\Z)", arch.group(1), re.S | re.M):
            title, text = m2.group(1).strip(), " ".join(l.strip() for l in m2.group(2).split("\n") if l.strip() and not l.strip().startswith("- ["))
            if title != "品牌" and text:
                essay.append((title, text))
    notes = re.search(r"^## 我的笔记\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    note_lines = [l for l in (notes.group(1).split("\n") if notes else []) if l.strip() not in ("", "-")]
    return dict(name=path.stem.replace("（风格）", ""), fm=fm, quote=quote, subs=subs, essay=essay, notes=note_lines)


def as_list(v):
    return v if isinstance(v, list) else ([v] if v else [])


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("JUESE_STYLE_DIR")
    if not src or not pathlib.Path(src).expanduser().is_dir():
        sys.exit("用法：python3 scripts/sync-styles.py <风格目录>（或设置环境变量 JUESE_STYLE_DIR）")
    src = pathlib.Path(src).expanduser()
    styles = [s for s in (parse(p) for p in sorted(src.glob("*.md"))) if s]
    styles.sort(key=lambda s: (s["fm"].get("类别", ""), int(s["fm"].get("排序") or 999), s["name"]))
    out = [
        "# 服装风格",
        "",
        f"由 `scripts/sync-styles.py` 从一个 Obsidian 风格库生成（{len(styles)} 个风格；随 skill 发布的这一份来自作者马自立的风格库）。**不要手改这个文件**：改风格页再跑脚本，见 `索引.md` 的「用你自己的风格库」。",
        "",
        "用法见 `索引.md`。落到人物身上时，从「经典单品」里挑 3–5 件，按 `../dimensions/04-服装.md` 往下切到款式、版型、面料、穿法；配色直接用 HEX；「要当心」那一条通常就是这个人的破绽或者可以反转的地方。",
        "品牌只作风格参照、帮你想起具体的样子，锁定段里不写品牌和 logo，换成款式描述。",
        "",
        "| 风格 | 关键词 | 类别 · 层级 |",
        "|---|---|---|",
    ]
    for s in styles:
        fm = s["fm"]
        out.append(f"| [{s['name']}](#{s['name']}) | {'、'.join(as_list(fm.get('关键词')))} | {fm.get('类别', '')} · {fm.get('层级', '')} |")
    for s in styles:
        fm = s["fm"]
        out += ["", f"## {s['name']}", ""]
        if s["quote"]:
            out += [f"> {s['quote']}", ""]
        if as_list(fm.get("aliases")):
            out.append(f"- **别名**：{'、'.join(as_list(fm.get('aliases')))}")
        out.append(f"- **关键词**：{'、'.join(as_list(fm.get('关键词')))}")
        out.append(f"- **经典单品**：{'、'.join(as_list(fm.get('经典单品')))}")
        if fm.get("入门"):
            out.append(f"- **最小组合**：{fm['入门']}")
        if as_list(fm.get("配色")):
            out.append(f"- **配色**：{' '.join(as_list(fm.get('配色')))}")
        if fm.get("风险"):
            out.append(f"- **要当心**：{fm['风险']}")
        brands = as_list(fm.get("品牌")) + as_list(fm.get("国内品牌"))
        if brands:
            out.append(f"- **参照品牌**：{'、'.join(brands)}")
        if s["subs"]:
            out.append("- **细分**：")
            out += [f"  - {x}" for x in s["subs"]]
        if s["essay"]:
            out.append("- **风格档案**：")
            out += [f"  - **{t}**：{x}" for t, x in s["essay"]]
        if s["notes"]:
            out.append("- **笔记**：")
            out += ["  " + l if l.startswith("-") else "  - " + l.strip() for l in s["notes"]]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"已生成 {OUT.relative_to(SKILL)}：{len(styles)} 个风格")


if __name__ == "__main__":
    main()
