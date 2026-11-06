#!/usr/bin/env python3
"""Validate the skill package structure, frontmatter and distribution zips.

Usage:
    python scripts/validate_skill.py
    python scripts/validate_skill.py --packages

Exit code: 0 on success, 1 on any validation failure.
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "narrative-design"
SKILL_MD = SKILL_DIR / "SKILL.md"
DIST = ROOT / "dist"

STANDARD_FIELDS = {
    "name", "description", "license", "compatibility", "metadata", "allowed-tools",
}
WORKBUDDY_REQUIRED = {
    "name", "display_name", "display_name_en", "description",
    "description_zh", "description_en", "version", "author",
}
MEDIA_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".mp4", ".m4a", ".mp3", ".wav", ".srt", ".vtt"}
TIMESTAMP_RE = re.compile(r"\[\d+:\d+(?:\.\d+)?,\d+:\d+(?:\.\d+)?,\d+\]")
REFERENCE_RE = re.compile(r"@((?:references|templates|scripts)/[A-Za-z0-9_.\-/]+)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (top-level keys, body) without external YAML dependencies."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    end = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = index
            break
    if end is None:
        return {}, text
    keys: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if match:
            keys[match.group(1)] = (match.group(2) or "").strip()
    return keys, "\n".join(lines[end + 1:])


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_source() -> list[str]:
    errors: list[str] = []
    if not SKILL_MD.is_file():
        return [f"missing {SKILL_MD}"]

    text = SKILL_MD.read_text(encoding="utf-8")
    keys, body = parse_frontmatter(text)
    if not keys:
        fail(errors, "SKILL.md has no parseable YAML frontmatter (first line must be ---)")
        return errors

    unexpected = set(keys) - STANDARD_FIELDS
    if unexpected:
        fail(errors, f"standard frontmatter contains non-spec fields: {sorted(unexpected)}")
    if keys.get("name") != SKILL_DIR.name:
        fail(errors, f"name '{keys.get('name')}' does not match directory '{SKILL_DIR.name}'")
    if len(keys.get("description", "")) < 40:
        fail(errors, "description is missing or too short; it must state purpose and triggers")
    if len(text.splitlines()) >= 500:
        fail(errors, "SKILL.md reached 500 lines; move knowledge into references/")

    for reference in sorted(set(REFERENCE_RE.findall(body))):
        if not (SKILL_DIR / reference).is_file():
            fail(errors, f"broken reference: @{reference}")

    for path in sorted(SKILL_DIR.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() in MEDIA_SUFFIXES:
            fail(errors, f"media/subtitle asset must not be shipped: {path.relative_to(SKILL_DIR)}")
        if path.suffix.lower() in {".md", ".py"}:
            content = path.read_text(encoding="utf-8", errors="replace")
            if TIMESTAMP_RE.search(content):
                fail(errors, f"verbatim transcript marker found in {path.relative_to(SKILL_DIR)}")

    for required in ("references", "templates", "scripts"):
        if not (SKILL_DIR / required).is_dir():
            fail(errors, f"missing directory: {required}/")
    if not list((SKILL_DIR / "references").glob("*.md")):
        fail(errors, "references/ contains no markdown files")
    return errors


def validate_zip(path: Path, required_fields: set[str], label: str) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"missing package: {path.name} (run scripts/build_packages.py)"]

    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            tops = {name.split("/")[0] for name in names if name}
            if tops != {"narrative-design"}:
                fail(errors, f"{label}: zip top level must be a single narrative-design/ folder, got {sorted(tops)}")
            entry = "narrative-design/SKILL.md"
            if entry not in names:
                fail(errors, f"{label}: {entry} is missing")
                return errors
            keys, _ = parse_frontmatter(archive.read(entry).decode("utf-8"))
            if not keys:
                fail(errors, f"{label}: SKILL.md frontmatter is not parseable")
                return errors
            missing = required_fields - set(keys)
            if missing:
                fail(errors, f"{label}: missing frontmatter fields {sorted(missing)}")
            if label == "standard":
                extra = set(keys) - STANDARD_FIELDS
                if extra:
                    fail(errors, f"{label}: non-spec frontmatter fields {sorted(extra)}")
            for extra_file in ("LICENSE", "NOTICE"):
                if f"narrative-design/{extra_file}" not in names:
                    fail(errors, f"{label}: attribution file {extra_file} is missing from the package")
    except zipfile.BadZipFile as exc:
        fail(errors, f"{label}: cannot read zip: {exc}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the narrative-design skill package")
    parser.add_argument("--packages", action="store_true", help="also validate the built zip files in dist/")
    args = parser.parse_args(argv)

    errors = validate_source()
    if args.packages:
        errors += validate_zip(
            DIST / "narrative-design-agent-skills.zip", {"name", "description"}, "standard"
        )
        errors += validate_zip(
            DIST / "narrative-design-workbuddy.zip", WORKBUDDY_REQUIRED, "workbuddy"
        )

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print(f"\n{len(errors)} validation error(s)")
        return 1
    scope = "source + packages" if args.packages else "source"
    print(f"OK: {scope} validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
