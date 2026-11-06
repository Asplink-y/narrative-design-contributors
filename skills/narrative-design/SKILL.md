---
name: narrative-design
description: "Review and rewrite game worlds, narrative systems and branching dialogue, returning a diagnosis, ready-to-paste rewrite, and a checklist result instead of theory. Use when the user works on an RPG or interactive-fiction setting bible, a skill/check system, a dialogue tree, skill checks, player onboarding, or reactivity, or asks to review/critique a piece of game writing. Trigger phrases: 叙事设计, 世界观构建, 分支对话, 对白树, 技能判定, 红色检定, 白色检定, 可响应性, 玩法引导, RPG 编剧, narrative design, worldbuilding, branching dialogue, skill check, dialogue tree. Not for linear novels, screenplays, quest/level tuning, or general prose coaching."
license: MIT
compatibility: "Agent Skills compatible hosts. Python 3 is needed only for the optional dialogue linter. No network or credentials required."
metadata:
  version: "1.0.0"
  author: "narrative-design contributors"
  source: "Konsoll 2023, Helen Hindpere, How to build (un)believable worlds?"
  scope: "heuristics from one text-heavy top-down RPG; not a validated general theory"
---

# Narrative design workbench

## Scope and limits

This skill is a **review and rewrite workflow**, not a lecture. It distils one speaker's onboarding overview for a single, text-heavy, top-down RPG into checks and patterns. State the limitation whenever a user asks whether a rule is universal: it is a heuristic, and camera distance / animation budget changes how much text a scene needs (D-1).

Use it for: setting bibles, skill and check systems, branching dialogue, review of game writing.
Do not use it for: linear fiction or screenplay coaching, quest/level tuning, general prose editing.

## Step 1 — Classify the stage

Ask one short clarifying question if the stage is genuinely ambiguous; otherwise infer it and proceed.

| Stage | Typical signals | Load |
| --- | --- | --- |
| Setting | "build a world", "is this setting believable", lore bible, factions | `@references/worldbuilding.md` |
| System design | "design skills", "players get lost", "choices feel meaningless" | `@references/design-principles.md` |
| Writing dialogue | "write/review these options", "dialogue tree", "skill check" | `@references/dialogue-patterns.md`, `@templates/dialogue-skeleton.md` |
| Review / rewrite | "critique this", "what is wrong with this scene" | `@templates/review-report.md` plus the one reference matching the artefact |
| Applicability / edge cases | "does this apply to my first-person game", "is this proven" | `@references/qa-insights.md` |

Terminology questions go to `@references/glossary.md`. Load **one** reference by default; load a second only if the artefact spans two stages. Never load all references at once.

## Step 2 — Diagnose with rule IDs

Every claim in the diagnosis must cite a rule ID from the loaded reference (`W-*`, `D-*`, `P-*`, `Q-*`) and one concrete piece of evidence from the user's material. If a rule does not apply to their camera, genre or team size, say so instead of forcing it.

Rules marked **anti-pattern** are the highest-value findings: they are mechanically checkable and usually the real reason a scene feels flat.

## Step 3 — Answer in three fixed parts

1. **Diagnosis** — a short list: `rule ID · what was found · one line of evidence`. Put anti-patterns first.
2. **Rewrite** — ready-to-paste material: actual dialogue option lines, a node structure, or concrete setting entries. Never answer "make it richer" without showing the replacement text. Keep the user's voice and genre.
3. **Checklist** — tick the relevant items from `@templates/review-report.md` with pass / warn / fail. Mark untestable items as `not checked` rather than guessing.

If the user supplied a dialogue file, optionally run `scripts/check_dialogue.py <file.json>` (schema in `@templates/dialogue-skeleton.md`) and fold its findings into part 1.

## Step 4 — Ground examples

Prefer examples from the source material over invented ones: the orange-parka girl and the passive check that opens a gentler option, the companion who pulls an exaggerated protagonist back to the main case, the "wait, what?" aside that returns to a skipped option, red vs white checks. Use them as **illustrations of a pattern**, not as lines to copy.

## Prohibited

- Do not reproduce transcript lines, subtitles, translated slide wording, or screenshots from the source talk. See the `NOTICE` file shipped alongside this skill for attribution obligations.
- Do not present a single-work observation as a general law, and do not invent citations, studies, or quotes.
- Do not output a theory summary when the user handed you an artefact — they want a review.
- Do not silently change the user's setting facts. Propose additions as additions.

## Quick reference

Pattern names and their Chinese equivalents live in `@references/glossary.md`. The dialogue structure atoms are: River, Whirlpool, Red check, White check, Hub, Leave option; the three check kinds are passive, red, white. A hub returns to itself; the whole conversation has only a small, controlled number of exits.
