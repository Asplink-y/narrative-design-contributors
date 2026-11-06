# Contributing

## Ground rules

1. **Keep it method-level and original.** Describe a technique in your own words. Do not paste transcript lines, subtitle text, translated slide wording, or screenshots. See [NOTICE](NOTICE).
2. **One concept, one home.** Put a definition in exactly one reference file; link to it instead of repeating it. Terminology lives in `references/glossary.md`.
3. **Keep `SKILL.md` short.** It is loaded into context on every invocation and should stay under 500 lines (target: 100–150). New knowledge goes into `references/`, not into the routing layer.
4. **Every new trigger phrase needs an eval.** Add a case to `evals/evals.json` with `should_trigger` set correctly.
5. **Every new anti-pattern should be lintable.** If it can be checked mechanically, add a rule to `skills/narrative-design/scripts/check_dialogue.py` and a self-test case.

## Before opening a PR

```bash
python scripts/validate_skill.py
python skills/narrative-design/scripts/check_dialogue.py --self-test
python scripts/build_packages.py
```

All three must pass. CI runs the same checks on push and pull request.

## Adding a reference file

- Create it under `skills/narrative-design/references/`.
- Add a row to the routing table in `SKILL.md` saying **when** to load it, using `@references/<file>.md`.
- Keep each file roughly 100–200 lines; split it if it grows beyond that.
- State limitations alongside claims. Do not upgrade a single-work observation into a general law.

## Adding a language version

Translations of our own original prose are welcome. Translate the content, not the source talk, and add `description_<lang>` only to the WorkBuddy build variant.

## Reporting an inaccuracy

If the distillation misstates the talk, open an issue with a timestamp from the video and a short quote (a few words only) sufficient to locate the moment. Do not paste long excerpts.
