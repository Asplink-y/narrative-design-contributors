# Branching dialogue — patterns reference

Loaded when the user writes, restructures or reviews dialogue options, nodes, or skill checks.

## P-1 · Tools shape what you can build

Writing tools split into those that **show the branch tree** and those that do not.

| Kind | Examples | Consequence |
| --- | --- | --- |
| Purpose-built, visual | articy:draft, Twine | preferred; free tiers are enough to start |
| General-purpose, non-visual | Word, Excel | if unavoidable, keep a separate whiteboard/Miro diagram |
| Generic visual surface | Miro, whiteboard | partial mitigation |
| In-house tool | built for interactive storytelling | should also be visual |

The source team's claim is causal: they could not have achieved their level of reactivity without seeing the shape of the dialogue. Flag/variable work and the "only two exits" discipline are manageable on a diagram and fragile in a spreadsheet.

- Anti-pattern: promising high reactivity while writing large trees in a non-visual tool.

## P-2 · A sense of security

Players must always know where they are in a conversation, where new questions appear, and how to leave. Early in the source project, writers play-testing each other's scenes felt a kind of claustrophobia — no idea where they were or how to get out — and later made a joke of it in the game itself.

Also communicate **where an option leads**. The cheap test is to have several people play the scene and ask one question: "was there a moment when you expected your character to say something else?" Solo developers should ask exactly that during playtests.

## P-3 · Reward, do not dump

The working slogan: *always get the player out of the dialogue*. Give a task, let the player go and do something, and unlock the long backstory when they return. Put lore and long branches behind checks, and treat **new dialogue options after a completed task** as the reward.

- Anti-pattern: a character explains their entire history at first meeting.

## P-4 · Vary the rhythm

Think of option sets as a musical phrase. Fixed counts, fixed ordering and labelled moral stances ("good / neutral / evil", always in that order) let players stop reading and start pressing buttons. Vary the number of options, mix questions and statements across different nodes, and avoid a predictable slot for each stance.

## The skeleton

**P-5 · Greeting → Main hub → branch → return.** The greeting appears once and establishes the character. New questions appear in the main hub; it is also the single convergence point for flag/variable work. Keep only a small controlled number of exits (two in the source project: an early leave during the greeting, and a leave from the hub).

**P-6 · Names and options carry two kinds of information.**

- A displayed name tells the player about the NPC *and* about the protagonist's assumptions. A short description ("the girl in the orange parka") can replace a name, and the displayed label may evolve as the relationship develops.
- Options are best read as **thoughts in the protagonist's head**: competing ideas arguing with each other, not a list of positions the character simultaneously endorses. The player can change their mind today.

**P-11 · Passive check.** A skill interjects on its own and opens a new option. Example shape: a shy NPC + an empathy note ("they're nervous") → a gentler option appears → a different outcome. No dice roll is presented to the player.

## Six structure atoms

| Atom | Rule ID | Behaviour |
| --- | --- | --- |
| **River** | P-7 | Carries the story forward. **Never mix a question with stance-taking statements in the same option set** — players almost always pick the question, because people want more information and avoid committing. If you want players to build a character through statements, keep the set all-statements. |
| **Whirlpool** | P-8 | A "wait, what…?" aside that lets the player ask one more thing without derailing the conversation, then returns to the option they skipped. Use one stable wording convention so players learn the hidden rule intuitively. In the source example, an encyclopedia note about a name with no accent opens the aside, and the conversation folds back to the original question. |
| **Red check** | P-9 | A check that cannot be retried. Failure must still move the story and become part of the character — embarrassment, an offensive line, a wildly misjudged tone — never a locked door that invites a reload. Give the player a way to react to the disaster (P-9b): a shocked option, a companion's comment, or a later chance to reflect. The source speaker said their own game could have done more of this. |
| **White check** | P-10 | A retryable check. Failure is temporarily uneventful; the player can explore, talk, level the skill or learn something and try again later. |
| **Hub** | P-10 | Inside a main hub, group questions about one topic so the hub stays small and everything returns to it. |
| **Leave option** | P-5 | One explicit, predictable exit, counted among the controlled exits. |

Three check kinds follow from this: **passive** (auto interjection, opens an option), **red** (one shot, failure advances), **white** (retryable, failure waits). Differentiate them in the design document before writing any of them.

## Anti-patterns (lintable subset)

| ID | Pattern | Caught by linter |
| --- | --- | --- |
| A-1 | Every node has the same option count, in the same moral order | yes |
| A-2 | Questions and statements mixed in one set | yes |
| A-3 | More than two exit points, or an unmarked exit | yes |
| A-4 | A long lore branch reachable at first greeting | heuristic |
| A-5 | Red check failure with no consequence or no reaction | yes |
| A-6 | Non-visual tool used for a large tree | manual |
| A-7 | Negative outcome with no reflection option | yes |
| A-8 | Character names used as plain labels only | manual |

`scripts/check_dialogue.py` implements the "yes" rows. Its JSON schema is in `@templates/dialogue-skeleton.md`.

## Dialogue-stage checklist

- [ ] Tree is authored in a visual tool, or has a maintained diagram (P-1).
- [ ] Hub, return paths and the two exits are visible in the diagram (P-5).
- [ ] Playtest feedback on "where did you expect this to lead" was collected (P-2).
- [ ] Long backstory is gated behind a task or a check (P-3).
- [ ] Option counts and tones vary between nodes (P-4).
- [ ] No question is mixed with stance statements in the same set (P-7).
- [ ] Whirlpool asides use one wording convention and return to a skipped option (P-8).
- [ ] Every red-check failure advances the story and offers a reaction (P-9, P-9b).
- [ ] Passive, red and white checks are distinguishable in the design doc (P-10, P-11).

## Closing principle

Every good conversation needs a solid structure the writer can rely on. Patterns are not a substitute for voice — they are what frees the writer to spend attention on voice.
