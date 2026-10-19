#!/usr/bin/env python3
"""Build a deterministic, dependency-free module archive."""
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def main():
    subprocess.run([sys.executable, str(ROOT / "scripts/merge_cn.py")], cwd=ROOT, check=True)
    with zipfile.ZipFile(ROOT / "mod_chn.zip", "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in ("module.json", "cn.json", "welcome.js"):
            info = zipfile.ZipInfo(name, date_time=(2000, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (ROOT / name).read_text(encoding="utf-8").encode("utf-8"))
    print(ROOT / "mod_chn.zip")

if __name__ == "__main__":
    main()
