#!/usr/bin/env python3
"""Offline validation of the pinned v14 localization snapshots and release."""
import collections
import hashlib
import json
import re
from pathlib import Path
from localization import compatible_tokens, flatten, read_json

ROOT = Path(__file__).resolve().parent.parent

def main():
    errors = []
    files = list((ROOT / "fvtt mod汉化").rglob("*.json"))
    for path in files:
        def unique(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    errors.append(f"Duplicate JSON member: {path.relative_to(ROOT)}: {key}")
                result[key] = value
            return result
        try:
            json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique)
        except (ValueError, UnicodeError) as exc:
            errors.append(f"Invalid JSON: {path}: {exc}")
    audit = read_json(ROOT / "docs/v14-audit.json")
    folders = {p.name for p in (ROOT / "fvtt mod汉化").iterdir() if p.is_dir()}
    records = {r["id"]: r for r in audit["modules"]}
    if folders != records.keys():
        errors.append("Audit does not cover every module directory")
    ready = 0
    languages = {}
    for module_id, record in records.items():
        if record["status"] != "source_ready":
            continue
        ready += 1
        folder = ROOT / "fvtt mod汉化" / module_id
        source_text = (folder / "en.json").read_text(encoding="utf-8")
        if hashlib.sha256(source_text.encode()).hexdigest() != record["snapshot_sha256"]:
            errors.append(f"English snapshot changed without updating provenance: {module_id}")
        en, cn = flatten(read_json(folder / "en.json")), flatten(read_json(folder / "cn.json"))
        languages[module_id] = (en, cn)
        for key, value in en.items():
            if key not in cn:
                errors.append(f"Missing: {module_id}: {key}")
            elif isinstance(value, str) and not compatible_tokens(value, cn[key]):
                errors.append(f"Placeholder mismatch: {module_id}: {key}")
    patterns = {
        "HTML": r"</?[A-Za-z][^>]*>",
        "URL": r'https?://[^\s<>"\)]+',
        "inline code": r"`[^`\n]*`",
        "enrichment": r"(?:@|&)[A-Za-z][\w.:-]*\[[^\]]+\]",
    }
    review = read_json(ROOT / "docs/v14-translation-review.json")
    for row in review:
        en, cn = languages[row["id"]]
        key = row["key"]
        if not isinstance(en[key], str):
            continue
        for kind, pattern in patterns.items():
            if collections.Counter(re.findall(pattern, en[key])) != collections.Counter(re.findall(pattern, cn[key])):
                errors.append(f"{kind} mismatch: {row['id']}: {key}")
    manifest = read_json(ROOT / "module.json")
    for path in [l["path"] for l in manifest["languages"]] + manifest["esmodules"]:
        if not (ROOT / path).is_file():
            errors.append(f"Missing packaged file: {path}")
    if manifest["id"] != "zzz_mod_chn" or manifest["compatibility"]["minimum"] != "14":
        errors.append("Unexpected module id or Foundry minimum")
    if "verified" in manifest["compatibility"]:
        errors.append("Do not declare live verification before testing in Foundry")
    if errors:
        print("\n".join(errors))
        raise SystemExit(f"{len(errors)} validation error(s)")
    print(f"OK: {len(files)} JSON files, {len(records)} audited modules, {ready} pinned v14 sources, {len(review)} reviewed/queued changes")

if __name__ == "__main__":
    main()
