import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_package import validate


class ValidatePackageTests(unittest.TestCase):
    def create_package(
        self, root: Path, skills: list[str], *, license_name: str = "Apache-2.0"
    ) -> None:
        (root / "package.json").write_text(
            json.dumps({"skills": skills, "license": license_name}),
            encoding="utf-8",
        )
        for skill in skills:
            directory = root / skill
            directory.mkdir()
            (directory / "SKILL.md").write_text(
                f"---\nname: {skill}\ndescription: Une description utile.\n---\n\n# Instructions\n",
                encoding="utf-8",
            )

    def test_accepts_a_valid_package(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.create_package(root, ["example-skill"])
            self.assertEqual(validate(root), [])

    def test_reports_missing_declared_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.create_package(root, [])
            (root / "package.json").write_text(
                json.dumps({"skills": ["missing-skill"]}), encoding="utf-8"
            )
            self.assertIn(
                "missing-skill/SKILL.md: declared skill is missing", validate(root)
            )

    def test_reports_non_string_skill_without_crashing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "package.json").write_text(
                json.dumps({"skills": [{"name": "not-a-string"}]}), encoding="utf-8"
            )
            self.assertIn(
                "package.json: invalid skill name: {'name': 'not-a-string'}",
                validate(root),
            )

    def test_validates_a_duplicated_skill_only_once(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.create_package(root, ["example-skill"])
            (root / "package.json").write_text(
                json.dumps({"skills": ["example-skill", "example-skill"]}),
                encoding="utf-8",
            )
            (root / "example-skill" / "SKILL.md").write_text(
                "---\nname: wrong-name\n---\nBody\n", encoding="utf-8"
            )

            errors = validate(root)

            self.assertEqual(errors.count("package.json: 'skills' contains duplicates"), 1)
            self.assertEqual(
                sum("missing frontmatter keys: description" in error for error in errors),
                1,
            )
            self.assertEqual(sum("name must match" in error for error in errors), 1)

    def test_reports_name_mismatch_and_unknown_key(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.create_package(root, ["example-skill"])
            (root / "example-skill" / "SKILL.md").write_text(
                "---\nname: another-name\ndescription: Text.\nversion: 1\n---\nBody\n",
                encoding="utf-8",
            )
            errors = validate(root)
            self.assertTrue(any("unsupported frontmatter keys" in e for e in errors))
            self.assertTrue(any("name must match" in e for e in errors))

    def test_requires_license_file_for_mit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.create_package(root, ["example-skill"], license_name="MIT")
            self.assertIn(
                "LICENSE: required when package.json declares the MIT license",
                validate(root),
            )


if __name__ == "__main__":
    unittest.main()
