#!/usr/bin/env python3
"""Build cn.json without mixed dotted/nested key loss.

For shared keys, a translation matching an audited v14 English snapshot takes
precedence over a legacy alias. Equal-priority entries retain the historical
folder-name order (last wins). Every conflicting value is recorded for review.
"""
import json
from pathlib import Path
from localization import expand, flatten, read_json

ROOT = Path(__file__).resolve().parent.parent

def merge_files(mod_dir, records):
    current = {r["id"] for r in records if r["status"] == "source_ready"}
    merged, owners, priorities, sequence = {}, {}, {}, {}
    collisions = []
    files = sorted(mod_dir.rglob("cn.json"), key=lambda p: p.relative_to(mod_dir).as_posix())
    if not files:
        raise ValueError("No module cn.json files found")
    for order, path in enumerate(files):
        relative = path.relative_to(mod_dir)
        module_id = relative.parts[0]
        data = read_json(path)
        if not isinstance(data, dict):
            raise ValueError(f"Not a JSON object: {path}")
        source = mod_dir / module_id / "en.json"
        fresh = flatten(read_json(source)) if module_id in current and len(relative.parts) == 2 and source.exists() else {}
        for key, value in flatten(data).items():
            rank = int(key in fresh)
            wins = key not in merged or rank >= priorities[key]
            if key in merged and merged[key] != value:
                collisions.append({"key": key, "previous": owners[key], "incoming": relative.as_posix(), "winner": relative.as_posix() if wins else owners[key]})
            if wins:
                merged[key], owners[key], priorities[key] = value, relative.as_posix(), rank
                sequence[key] = order
    # A v14 object can replace a legacy scalar (or vice versa). JSON cannot
    # represent both at the same property, so apply the same priority rule.
    removed = set()
    for key in sorted(merged):
        if key in removed:
            continue
        parts = key.split(".")
        for end in range(1, len(parts)):
            parent = ".".join(parts[:end])
            if parent not in merged or parent in removed:
                continue
            child_wins = (priorities[key], sequence[key]) >= (priorities[parent], sequence[parent])
            winner, loser = (key, parent) if child_wins else (parent, key)
            collisions.append({"key": key, "parent_key": parent, "type": "parent_child", "previous": owners[parent], "incoming": owners[key], "winner": owners[winner]})
            removed.add(loser)
            if not child_wins:
                break
    for key in removed:
        del merged[key]
    return expand(merged), collisions, len(files)

def main():
    audit = ROOT / "docs" / "v14-audit.json"
    records = read_json(audit)["modules"] if audit.exists() else []
    merged, collisions, count = merge_files(ROOT / "fvtt mod汉化", records)
    (ROOT / "cn.json").write_text(json.dumps(merged, ensure_ascii=False, indent="\t", sort_keys=True) + "\n", encoding="utf-8")
    report = ROOT / "docs" / "merge-conflicts.json"
    report.parent.mkdir(exist_ok=True)
    report.write_text(json.dumps(collisions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Merged {count} files; {len(flatten(merged))} keys; {len(collisions)} shared-key conflicts recorded")

if __name__ == "__main__":
    main()
