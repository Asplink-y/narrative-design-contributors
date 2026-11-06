#!/usr/bin/env python3
"""Build the two distributable skill packages from one source of truth.

    python scripts/build_packages.py
    python scripts/build_packages.py --author "Your Name" --version 1.0.1

Outputs:
    dist/narrative-design-agent-skills.zip   (6-field standard frontmatter)
    dist/narrative-design-workbuddy.zip      (marketplace frontmatter)
"""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "skills" / "narrative-design"
DIST = ROOT / "dist"
DEFAULT_VERSION = "1.0.0"
DEFAULT_AUTHOR = "narrative-design contributors"

WORKBUDDY_FRONTMATTER = """---
name: narrative-design
display_name: 叙事设计工作台
display_name_en: Narrative design workbench
description: "用于 RPG 与互动叙事的世界观构建、技能与检定系统设计、分支对话写作与评审。当用户提到叙事设计、世界观构建、分支对话、对白树、技能判定、红色检定、白色检定、可响应性、玩法引导、RPG 编剧时触发；输出诊断、可直接使用的改写文本与检查清单，不复述理论。"
description_zh: "把一场叙事设计演讲提炼成可执行的评审与改写工作流，覆盖世界观、系统设计、分支对话与检查清单。"
description_en: "An executable review and rewrite workflow for game worlds, narrative systems and branching dialogue."
examples_zh:
  - "帮我评审这段分支对话：每个节点都固定三个选项，赞成、中立、拒绝，顺序不变。"
  - "给我的 RPG 设计技能判定，失败也要能推动剧情。"
examples_en:
  - "Review this dialogue hub: every node offers the same three options in the same order."
  - "Design a skill check whose failure still moves the story forward."
version: {version}
author: "{author}"
---"""


def strip_frontmatter(text: str) -> str:
    """Keep only the Markdown body after a leading YAML frontmatter block."""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for index, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                return "\n".join(lines[index + 1:]).lstrip("\n")
    return text


def source_files() -> list[Path]:
    return [
        path for path in sorted(SRC.rglob("*"))
        if path.is_file()
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
    ]


def build(target: Path, frontmatter: str | None = None) -> None:
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in source_files():
            relative = path.relative_to(SRC).as_posix()
            data = path.read_bytes()
            if relative == "SKILL.md" and frontmatter is not None:
                body = strip_frontmatter(path.read_text(encoding="utf-8"))
                data = (frontmatter + "\n\n" + body).encode("utf-8")
            archive.writestr(f"narrative-design/{relative}", data)
        for name in ("LICENSE", "NOTICE"):
            extra = ROOT / name
            if extra.is_file():
                archive.writestr(f"narrative-design/{name}", extra.read_bytes())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build standard and WorkBuddy skill packages")
    parser.add_argument("--author", default=DEFAULT_AUTHOR, help="author for the WorkBuddy variant")
    parser.add_argument("--version", default=DEFAULT_VERSION, help="version for the WorkBuddy variant")
    args = parser.parse_args(argv)

    if not (SRC / "SKILL.md").is_file():
        print(f"error: missing {SRC / 'SKILL.md'}", file=sys.stderr)
        return 1

    DIST.mkdir(parents=True, exist_ok=True)
    standard = DIST / "narrative-design-agent-skills.zip"
    workbuddy = DIST / "narrative-design-workbuddy.zip"

    build(standard)
    build(workbuddy, WORKBUDDY_FRONTMATTER.format(version=args.version, author=args.author))

    for package in (standard, workbuddy):
        print(f"built {package.relative_to(ROOT)} ({package.stat().st_size:,} bytes)")
    print("run `python scripts/validate_skill.py --packages` to verify")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
