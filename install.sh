#!/usr/bin/env bash
# 安装 juese-sheji（AI 人物设计）skill
#   ./install.sh               装到 ~/.claude/skills（Claude Code，所有项目都能用）
#   ./install.sh <项目目录>     装到 <项目目录>/.claude/skills（只在这个项目里用）
#   ./install.sh --codex       装到 ~/.codex/skills（Codex）
# 已经装过的会先挪到 skills 目录外面备份，不会直接覆盖。
set -e
here="$(cd "$(dirname "$0")" && pwd)"
case "${1:-}" in
  --codex) dest="${CODEX_HOME:-$HOME/.codex}/skills" ;;
  "")      dest="$HOME/.claude/skills" ;;
  *)       dest="$1/.claude/skills" ;;
esac
mkdir -p "$dest"
if [ -e "$dest/juese-sheji" ]; then
  bak="$(dirname "$dest")/juese-sheji.bak-$(date +%Y%m%d-%H%M%S)"   # 放到 skills 外面，免得被当成第二个同名 skill 加载
  mv "$dest/juese-sheji" "$bak"
  echo "已有旧版本，备份到 $bak"
fi
cp -R "$here/juese-sheji" "$dest/"
echo "已安装：$dest/juese-sheji"
echo "在 Claude Code 里说「帮我把『一个轻佻的男性』写具体」试试。"
