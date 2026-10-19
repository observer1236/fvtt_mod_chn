import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from localization import compatible_tokens, expand, flatten
from merge_cn import merge_files

class LocalizationTests(unittest.TestCase):
    def test_mixed_keys_keep_both_branches(self):
        flat = flatten({"MOD.name": "名称", "MOD": {"hint": "提示"}})
        self.assertEqual(expand(flat), {"MOD": {"name": "名称", "hint": "提示"}})

    def test_ambiguous_same_file_key_is_rejected(self):
        with self.assertRaises(ValueError):
            flatten({"MOD.name": "A", "MOD": {"name": "B"}})
        with self.assertRaises(ValueError):
            expand({"MOD": "A", "MOD.name": "B"})

    def test_old_alias_cannot_overwrite_current_v14_text(self):
        cache = Path(__file__).resolve().parents[1] / ".cache"
        cache.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=cache) as tmp:
            root = Path(tmp)
            for name, text in [("a-current", "新版"), ("z-legacy", "旧版")]:
                folder = root / name
                folder.mkdir()
                (folder / "cn.json").write_text(json.dumps({"MOD.label": text}), encoding="utf-8")
            (root / "a-current" / "en.json").write_text('{"MOD":{"label":"New label"}}', encoding="utf-8")
            result, conflicts, count = merge_files(root, [{"id": "a-current", "status": "source_ready"}])
            self.assertEqual(result["MOD"]["label"], "新版")
            self.assertEqual(conflicts[0]["winner"], "a-current/cn.json")
            self.assertEqual(count, 2)

    def test_data_placeholders_and_enriched_links(self):
        self.assertFalse(compatible_tokens("{count} for {name}", "{count} 项"))
        self.assertFalse(compatible_tokens("{{actor.name}}", "{{name}}"))
        self.assertTrue(compatible_tokens("@UUID[Compendium.a.b]{Open item}", "@UUID[Compendium.a.b]{打开物品}"))
        self.assertFalse(compatible_tokens("@UUID[Compendium.a.b]", "@UUID[Compendium.a.c]"))
        self.assertTrue(compatible_tokens("{count} level{s}", "{count} 层"))

    def test_current_child_replaces_legacy_parent_scalar(self):
        cache = Path(__file__).resolve().parents[1] / ".cache"
        cache.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=cache) as tmp:
            root = Path(tmp)
            for name in ("a-current", "z-legacy"):
                (root / name).mkdir()
            (root / "a-current/cn.json").write_text('{"MOD.Locked.Hint":"提示"}', encoding="utf-8")
            (root / "a-current/en.json").write_text('{"MOD.Locked.Hint":"Hint"}', encoding="utf-8")
            (root / "z-legacy/cn.json").write_text('{"MOD.Locked":"旧锁定提示"}', encoding="utf-8")
            result, conflicts, _ = merge_files(root, [{"id":"a-current", "status":"source_ready"}])
            self.assertEqual(result["MOD"]["Locked"]["Hint"], "提示")
            self.assertEqual(conflicts[0]["type"], "parent_child")

if __name__ == "__main__":
    unittest.main()
