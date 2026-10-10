#!/usr/bin/env python3
"""把 juese-sheji/ 打成两个 zip，放在 dist/：

- juese-sheji.zip          文件带 juese-sheji/ 前缀（claude.ai 上传、Release 附件用）
- juese-sheji-skillhub.zip SKILL.md 在根目录（SkillHub 上传用）

用 Python 打包而不是 macOS 自带的 zip：后者不给中文文件名打 UTF-8 标记，
别的系统解压（包括 claude.ai）会变成乱码，SKILL.md 里引用的文件就找不到了。
GitHub Actions（.github/workflows/release.yml）每次推送也跑这个，把两个包传到 Release。
"""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
SKILL = ROOT / "juese-sheji"
DIST = ROOT / "dist"
SKIP = {".DS_Store"}

# 输出文件 → 包内路径相对于哪个目录
TARGETS = {
    DIST / "juese-sheji.zip": ROOT,
    DIST / "juese-sheji-skillhub.zip": SKILL,
}

DIST.mkdir(exist_ok=True)
files = [p for p in sorted(SKILL.rglob("*"))
         if p.is_file() and p.name not in SKIP and "__pycache__" not in p.parts]
for out, base in TARGETS.items():
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, p.relative_to(base).as_posix())
    with zipfile.ZipFile(out) as z:
        names = z.namelist()
        bad = [i.filename for i in z.infolist() if not i.filename.isascii() and not i.flag_bits & 0x800]
    print(f"已打包 {out.relative_to(ROOT)}：{len(names)} 个文件，{out.stat().st_size // 1024} KB" + ("" if not bad else f"，有 {len(bad)} 个文件名没打 UTF-8 标记！"))
