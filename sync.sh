#!/bin/zsh
# 维护者用：正本在作者本机的 AIGC 工作区，改完跑这个，把 skill 同步进仓库、打包、提交、推送。
# 用法：./sync.sh "改了什么"
set -e
R="${0:A:h}"
SRC="${JUESE_SRC:-$HOME/.config/skillshare/skills/aigc/juese-sheji}"   # 正本在 skillshare 源的 aigc 分组
rsync -a --delete --exclude .DS_Store --exclude __pycache__ --exclude 'evals/runs' "$SRC/" "$R/juese-sheji/"
cd "$R"
python3 package.py   # 本地也打一份 dist/ 的两个 zip；推送后 GitHub Actions 自动发新版本（提交说明末尾写 井号 minor 或 井号 major 升大版本）
git add -A
git diff --cached --quiet && { echo "没有改动"; exit 0; }
git commit -q -m "${1:-同步 skill}"
git push -q
echo "已推送：$(git log -1 --format='%h %s')"
