# narrative-design-contributors

An open Agent Skill that turns narrative design into an executable review workflow: diagnose, rewrite, check. Dual-format packages for agent.

The skill in this repository is called **Narrative Design Workbench** (叙事设计工作台). It follows the [Agent Skills](https://agentskills.io) open standard and distils Helen Hindpere's Konsoll 2023 talk *How to build (un)believable worlds?* (lead writer on *Disco Elysium*) into a stage-routed checklist: worldbuilding, narrative-system design, branching dialogue, and review. It is an **executable review and rewrite workflow**, not a reading note.

[中文说明](README.zh-CN.md) · [发布指南](docs/publishing.md) · [署名与版权](NOTICE)

---

## What this is

- A skill that, given a setting bible, a skill system, or a chunk of branching dialogue, returns: **diagnosis → ready-to-paste rewrite → checklist result**.
- A small static linter that turns the talk's anti-patterns into machine-checkable rules.
- A dual-format repository: one standards-compliant skill package plus a script that emits a WorkBuddy-marketplace package from the same source.

## What this is not

- Not a general creative-writing course, not a novel/screenplay tutor, not a quest or level-design system.
- Not a validated theory. It is a single speaker's onboarding overview for one text-heavy, top-down RPG. Limitations are documented in `references/qa-insights.md` and repeated in `SKILL.md`.

## Install

| Target | How |
| --- | --- |
| Claude Code / any Agent Skills host | Copy `skills/narrative-design/` into `~/.claude/skills/` (personal) or `.claude/skills/` (project) |
| WorkBuddy | Run `python scripts/build_packages.py`, then import `dist/narrative-design-workbuddy.zip` via **Add skill → Upload skill** |
| Anything else | Read `skills/narrative-design/SKILL.md` and its `@references/` files directly — the package has no runtime dependency beyond Python 3 for the optional linter |

No network access, no API key, no credentials are required by the skill itself.

## Try it

```
Review this branching dialogue. All my hubs offer exactly three options:
agree / neutral / refuse, always in that order.
```

The skill should identify the fixed-option anti-pattern, rewrite a hub with mixed question/statement types and a return path, then tick the relevant checklist items.

More cases: [examples/](examples/) and [evals/evals.json](evals/evals.json).

## Repository layout

```
narrative-design-skill/
├── skills/narrative-design/     # the distributable skill (single source of truth)
│   ├── SKILL.md                 # frontmatter + routing + output contract
│   ├── references/              # loaded only when the matching stage is active
│   ├── templates/               # review report and dialogue skeleton
│   └── scripts/check_dialogue.py
├── scripts/
│   ├── validate_skill.py        # frontmatter/structure/reference checks (stdlib only)
│   └── build_packages.py        # builds the two distributable zip files
├── examples/                    # worked inputs with acceptance criteria
├── evals/evals.json             # trigger + behaviour test cases
├── docs/publishing.md           # GitHub release and marketplace upload steps
└── .github/workflows/validate.yml
```

## The workflow

1. Determine the user's stage: **setting / system design / writing dialogue / review**.
2. Load only the matching `@references/...` file.
3. Answer in three fixed parts: **diagnosis → concrete rewrite → checklist**.
4. Prefer examples from the talk (the orange-parka girl, Kim as the grounding foil, red/white checks) over invented ones.

## Build and validate

```bash
python scripts/validate_skill.py
python skills/narrative-design/scripts/check_dialogue.py --self-test
python scripts/build_packages.py
```

`build_packages.py` produces:

- `dist/narrative-design-agent-skills.zip` — 6-field standard frontmatter, for Claude Code and other hosts
- `dist/narrative-design-workbuddy.zip` — WorkBuddy frontmatter (`display_name`, `description_zh`, `author`, …), for marketplace upload

Both zip files contain a single top-level `narrative-design/` directory with `SKILL.md` at its root. That shape matters: a missing wrapper directory is the most common cause of package parsing failures.

## Provenance and license

This repository contains an independent, method-level distillation. It contains **no verbatim transcript, subtitle text, translated slide wording, or screenshots** from the talk. See [NOTICE](NOTICE) for full attribution. Code and original prose are [MIT](LICENSE); proper nouns are used for identification only.

If you plan to redistribute translated slides or subtitles, obtain permission from the respective rights holders first.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Please keep new material method-level and original, and add an eval case for any new trigger phrase.
