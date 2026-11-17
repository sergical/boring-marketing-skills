import json, re, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def readme_catalog():
    """Skill names from the README tables: rows that start with | `skill-name` |."""
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    return set(re.findall(r"^\| `([a-z0-9-]+)` \|", text, flags=re.M))


class Smoke(unittest.TestCase):
    def test_version_is_consistent(self):
        v = (ROOT / "_system" / "VERSION").read_text().strip()
        pj = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
        mp = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
        self.assertEqual(pj["version"], v)
        self.assertEqual(mp["plugins"][0]["version"], v)
        for sk in sorted((ROOT / "skills").glob("*/SKILL.md")):
            self.assertIn(f"version: {v}", sk.read_text(), sk)

    def test_skills_match_readme_catalog(self):
        on_disk = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        catalog = readme_catalog()
        self.assertEqual(len(catalog), 34)
        self.assertEqual(sorted(catalog - on_disk), [], "in the README but not on disk")
        self.assertEqual(sorted(on_disk - catalog), [], "on disk but not in the README")

    def test_frontmatter_is_strict_yaml_safe(self):
        # npx skills add skips a skill whose plain scalar holds ": " or " #".
        for sk in sorted((ROOT / "skills").glob("*/SKILL.md")):
            fm = sk.read_text(encoding="utf-8").split("\n---", 1)[0]
            for line in fm.splitlines()[1:]:
                m = re.match(r"^([A-Za-z_-]+):\s+(.*)$", line)
                if m and m.group(2)[:1] not in "\"'[{|>":
                    with self.subTest(skill=sk.parent.name, key=m.group(1)):
                        self.assertNotIn(": ", m.group(2))
                        self.assertNotIn(" #", m.group(2))


if __name__ == "__main__":
    unittest.main()
