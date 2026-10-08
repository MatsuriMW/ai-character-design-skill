#!/usr/bin/env python3
"""把 juese-sheji/ 打包成 dist/juese-sheji.zip（claude.ai 上传、Release 附件用）。

用 Python 打包而不是 macOS 自带的 zip：后者不给中文文件名打 UTF-8 标记，
别的系统解压（包括 claude.ai）会变成乱码，SKILL.md 里引用的文件就找不到了。
"""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
SKILL = ROOT / "juese-sheji"
OUT = ROOT / "dist" / "juese-sheji.zip"
SKIP = {".DS_Store"}

OUT.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(SKILL.rglob("*")):
        if p.is_file() and p.name not in SKIP and "__pycache__" not in p.parts:
            z.write(p, p.relative_to(ROOT).as_posix())
with zipfile.ZipFile(OUT) as z:
    names = z.namelist()
    bad = [i.filename for i in z.infolist() if not i.filename.isascii() and not i.flag_bits & 0x800]
print(f"已打包 {OUT.relative_to(ROOT)}：{len(names)} 个文件，{OUT.stat().st_size // 1024} KB" + ("" if not bad else f"，有 {len(bad)} 个文件名没打 UTF-8 标记！"))
