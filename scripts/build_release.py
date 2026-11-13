#!/usr/bin/env python3
"""Build a deterministic, dependency-free module archive.

Pass ``--release-tag`` (or ``--version``) when building a GitHub release.  The
manifest is rewritten to the current version and to the ``latest`` download
URLs, so the asset uploaded with a release never points at an old tag.
"""
import argparse
import json
import os
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/observer1236/fvtt_mod_chn"
MANIFEST_URL = f"{REPO_URL}/releases/latest/download/module.json"
DOWNLOAD_URL = f"{REPO_URL}/releases/latest/download/mod_chn.zip"


def _version_from_tag(tag: str) -> str:
    return tag[1:] if tag.startswith("v") else tag


def update_manifest(tag: str, version: str) -> None:
    """Rewrite module.json for a release asset and for the uploaded zip."""
    path = ROOT / "module.json"
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    data["version"] = version
    data["manifest"] = MANIFEST_URL
    data["download"] = DOWNLOAD_URL
    data["changelog"] = f"{REPO_URL}/releases/tag/{tag}"
    compatibility = data.setdefault("compatibility", {})
    compatibility["verified"] = "14"
    path.write_text(json.dumps(data, ensure_ascii=False, indent="\t") + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--release-tag",
        default=os.environ.get("RELEASE_TAG", ""),
        help="GitHub release tag, e.g. 14.2 or v14.2",
    )
    parser.add_argument(
        "--version",
        default=os.environ.get("RELEASE_VERSION", ""),
        help="Module version when no release tag is available",
    )
    args = parser.parse_args()

    tag = args.release_tag.strip()
    version = args.version.strip()
    if tag or version:
        if not tag:
            tag = version
        if not version:
            version = _version_from_tag(tag)
        update_manifest(tag, version)
        print(f"manifest: version {version}, changelog {tag}")

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
