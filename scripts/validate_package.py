#!/usr/bin/env python3
"""Validate the package manifest and skill metadata without dependencies."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_FRONTMATTER_KEYS = {"name", "description"}


def parse_frontmatter(path: Path) -> dict[str, str]:
    """Read the deliberately simple, scalar-only SKILL.md frontmatter."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("frontmatter must start on the first line with '---'")

    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("frontmatter has no closing '---'") from error

    metadata: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"line {line_number} is not a key/value pair")
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if not key or not value:
            raise ValueError(f"line {line_number} has an empty key or value")
        if key in metadata:
            raise ValueError(f"duplicate frontmatter key: {key}")
        metadata[key] = value

    if not any(line.strip() for line in lines[end + 1 :]):
        raise ValueError("skill instructions are empty")
    return metadata


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    manifest_path = root / "package.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"package.json: {error}"]

    skills = manifest.get("skills")
    if not isinstance(skills, list) or not skills:
        return ["package.json: 'skills' must be a non-empty array"]
    string_skills = [skill for skill in skills if isinstance(skill, str)]
    unique_string_skills = set(string_skills)
    if len(string_skills) != len(unique_string_skills):
        errors.append("package.json: 'skills' contains duplicates")

    validated_skills: set[str] = set()
    for skill in skills:
        if not isinstance(skill, str) or not SKILL_NAME.fullmatch(skill):
            errors.append(f"package.json: invalid skill name: {skill!r}")
            continue
        if skill in validated_skills:
            continue
        validated_skills.add(skill)
        skill_file = root / skill / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill}/SKILL.md: declared skill is missing")
            continue
        try:
            metadata = parse_frontmatter(skill_file)
        except (OSError, UnicodeError, ValueError) as error:
            errors.append(f"{skill}/SKILL.md: {error}")
            continue

        unknown = set(metadata) - ALLOWED_FRONTMATTER_KEYS
        missing = ALLOWED_FRONTMATTER_KEYS - set(metadata)
        if unknown:
            errors.append(
                f"{skill}/SKILL.md: unsupported frontmatter keys: "
                f"{', '.join(sorted(unknown))}"
            )
        if missing:
            errors.append(
                f"{skill}/SKILL.md: missing frontmatter keys: "
                f"{', '.join(sorted(missing))}"
            )
        if metadata.get("name") != skill:
            errors.append(
                f"{skill}/SKILL.md: name must match its directory ({skill!r})"
            )
        description = metadata.get("description", "")
        if len(description) > 1024:
            errors.append(f"{skill}/SKILL.md: description exceeds 1024 characters")

    declared = unique_string_skills
    discovered = {
        path.parent.name
        for path in root.glob("*/SKILL.md")
        if path.parent.parent == root
    }
    for skill in sorted(discovered - declared):
        errors.append(f"{skill}/SKILL.md: skill is not declared in package.json")

    if manifest.get("license") == "MIT" and not (root / "LICENSE").is_file():
        errors.append("LICENSE: required when package.json declares the MIT license")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="package root (defaults to the repository containing this script)",
    )
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    print("Package and skill metadata are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
