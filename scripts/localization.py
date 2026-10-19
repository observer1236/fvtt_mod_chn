"""Shared checks for Foundry's mixed dotted/nested localization dictionaries."""
import json
import re
from pathlib import Path

def flatten(data, prefix=""):
    result = {}
    for key, value in data.items():
        full = f"{prefix}.{key}" if prefix else key
        extra = flatten(value, full) if isinstance(value, dict) else {full: value}
        for name, item in extra.items():
            if name in result and result[name] != item:
                raise ValueError(f"Conflicting dotted/nested key: {name}")
            result[name] = item
    return result

def expand(data):
    result = {}
    for key, value in sorted(data.items()):
        node = result
        parts = key.split(".")
        for part in parts[:-1]:
            if part in node and not isinstance(node[part], dict):
                raise ValueError(f"Parent/child key conflict: {key}")
            node = node.setdefault(part, {})
        if parts[-1] in node and isinstance(node[parts[-1]], dict):
            raise ValueError(f"Parent/child key conflict: {key}")
        node[parts[-1]] = value
    return result

def tokens(text):
    if not isinstance(text, str):
        return []
    text = re.sub(r"(@(?:UUID|Compendium|Embed)\[[^\]]+\])\{[^{}]*\}", r"\1", text)
    return sorted(re.findall(r"\{\{[\w.]+\}\}|(?<!\{)\{[A-Za-z_][\w.-]*\}(?!\})|@(?:UUID|Compendium|Embed)\[[^\]]+\]|%(?:\d+\$)?[sdif]", text))

def compatible_tokens(source, target):
    expected, actual = tokens(source), tokens(target)
    # English plural suffixes do not carry data and have no Chinese equivalent.
    if isinstance(source, str) and re.search(r"\w\{s\}", source):
        expected = [t for t in expected if t != "{s}"]
        actual = [t for t in actual if t != "{s}"]
    return isinstance(target, str) and expected == actual

def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))
