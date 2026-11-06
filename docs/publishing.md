# Publishing guide

## 1. Prepare the repository

```bash
cd narrative-design-skill
python scripts/validate_skill.py
python skills/narrative-design/scripts/check_dialogue.py --self-test
python scripts/build_packages.py
python scripts/validate_skill.py --packages
git init
git add .
git commit -m "feat: narrative design skill v1.0.0"
```

`dist/*.zip` is gitignored on purpose: packages belong to GitHub Releases, not to the source tree. Before committing, replace `author` in `scripts/build_packages.py` if you are publishing under your own name.

## 2. Create the GitHub repository

```bash
gh repo create narrative-design-skill --public --source=. --remote=origin --push
```

Or create an empty repository in the GitHub UI, then:

```bash
git remote add origin https://github.com/<you>/narrative-design-skill.git
git branch -M main
git push -u origin main
```

Recommended repository settings:

- Description: `An open Agent Skill for narrative design review and branching dialogue`
- Topics: `agent-skills`, `narrative-design`, `game-writing`, `worldbuilding`, `claude-code`, `workbuddy`
- Add `README.md` as the repository landing page; `README.zh-CN.md` is linked from the top.
- Enable Issues for inaccuracy reports (see `CONTRIBUTING.md`).

## 3. Cut a release

```bash
git tag -a v1.0.0 -m "v1.0.0"
git push origin v1.0.0
gh release create v1.0.0 \
  dist/narrative-design-agent-skills.zip \
  dist/narrative-design-workbuddy.zip \
  --title "v1.0.0" --notes-file CHANGELOG.md
```

Attach both zip files. Users of standards-compatible hosts need the first; WorkBuddy users need the second.

## 4. Install from a release

| Host | Command / action |
| --- | --- |
| Claude Code (personal) | `unzip narrative-design-agent-skills.zip -d ~/.claude/skills/` |
| Claude Code (project) | `unzip narrative-design-agent-skills.zip -d .claude/skills/` and commit the folder |
| WorkBuddy | Experts · Skills · Connectors → Skills → Add skill → Upload skill → choose `narrative-design-workbuddy.zip` |

After installation, start a **new** session and run one case from `examples/` to confirm the skill triggers. Testing inside the session where you authored the skill gives false positives because the instructions are already in context.

## 5. Version bumps

- Patch: wording fixes, new eval cases, linter bug fixes.
- Minor: new reference file, new lint rule, new output template.
- Major: change to the routing table or the three-part output contract.

Update `CHANGELOG.md`, `version` in `scripts/build_packages.py`, and the tag together. Keep the standard package's `name` stable (`narrative-design`) so slash-command and directory names do not break.

## 6. Pre-flight checklist

- [ ] `python scripts/validate_skill.py` and `--packages` both pass
- [ ] No transcript, subtitle, translated slide text or screenshot is present
- [ ] `NOTICE` names the talk, the speaker, the Bilibili uploader and the upload URL
- [ ] `author` in the WorkBuddy variant is correct
- [ ] Both zip files contain a single top-level `narrative-design/` directory
- [ ] At least one positive and one negative trigger case verified in a fresh session
- [ ] `LICENSE` applies only to original prose and code
