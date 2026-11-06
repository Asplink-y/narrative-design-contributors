# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-11-06

### Added

- `skills/narrative-design/SKILL.md`: standards-compliant 6-field frontmatter, four-stage routing, fixed three-part output contract.
- Five reference files: worldbuilding, design principles, dialogue patterns, Q&A insights, glossary.
- Two templates: four-stage review report, dialogue skeleton.
- `check_dialogue.py`: static linter for fixed option counts, mixed question/statement options, excess exit points, and unhandled red-check failures; includes `--self-test`.
- `validate_skill.py`: frontmatter, structure and `@references/` resolution checks using only the Python standard library.
- `build_packages.py`: emits standard and WorkBuddy zip packages from one source.
- `evals/evals.json` trigger and behaviour cases, three worked examples, and CI workflow.
- Attribution and licensing documentation: `NOTICE`, `LICENSE`, `CONTRIBUTING.md`, `docs/publishing.md`.
