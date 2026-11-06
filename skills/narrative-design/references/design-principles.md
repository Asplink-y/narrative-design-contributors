# Narrative system design — system-stage reference

Loaded when the user designs skills, checks, companions, onboarding, or complains that choices feel meaningless.

## Framing question

Not "how much can we write" but "**how does writing support art and the rest of the game**". A team that can produce a million words still has to decide where those words are necessary.

## Principles

**D-1 · Text density follows the camera.** The closer the camera, the less the prose must describe. A top-down game with almost no animation budget needs writing to narrate posture, expression and action; a first-person game behaves more like a screenplay, leaning on direct speech and leaving room for animation, performance and art to show detail.

- How to apply: fix camera and animation budget first, then set a per-node word budget.
- Anti-pattern: porting a text-heavy top-down style into a close-camera game and burying the animation work.

**D-2 · Redefine the companion.** Any voice that persistently speaks to the protagonist can do a companion's job: skills, mental faculties, people from the character's past. In the source project, two dozen psychology-oriented skills interject during conversations and effectively become companions, while only one conventional companion exists.

**D-3 · Let narrative design hold the player's hand.** Two recurring player problems: asking a friend how to build/play a character before starting, and returning after months to a quest log that no longer makes sense. Ask which narrative element plays the role of that friend. Working answers:

- Skills that hint at the next step and remind the player of the main thread.
- A companion who is the protagonist's opposite: an exaggerated, side-quest-prone lead needs a grounded foil to restate the main case, recap steps already taken, and list the options now available.

Anti-pattern: treating onboarding as purely a UI/journal problem when the fiction could carry it.

**D-4 · Scale of reactivity.** Ask whether a decision reflects the protagonist's actual standing in the world, and whether it is abstract or situation-specific. Many games open with large questions about the value of a life or the nature of good and evil. Reach those later.

- Preferred order: small, mundane, influenceable decisions first — a morning routine (coffee first, news while drinking, meditation, or straight out the door) — because players relate to ordinary life, not to world-saving heroism. Big moral choices land harder once the connection exists.
- Anti-pattern: a first scene that asks the player to define their philosophy before they know who they are.

**D-5 · Failure is content.** Design checks so that failure is as interesting as success and remains part of the character, rather than closing a door and inviting a reload. See `dialogue-patterns.md` for the red/white/passive split.

**D-6 · Pressure and release.** A narrative with no moments of lost control can become exhausting. Cutscenes and quiet beats are legitimate tools for pacing, letting the player rest from reading and look at the art. The source speaker explicitly regretted using too few of them.

## System-stage checklist

- [ ] Text budget was derived from camera distance and animation capacity (D-1).
- [ ] At least one non-traditional voice supports the lead, or the decision to use only conventional companions is deliberate (D-2).
- [ ] A named narrative element owns onboarding, recaps and "what next" hints (D-3).
- [ ] Small situational decisions precede abstract moral ones (D-4).
- [ ] Every check type defines what failure does to the story (D-5).
- [ ] The pacing plan includes rest beats for a text-heavy game (D-6).

## Note on evidence

These come from one studio with no formal game-development training, working on one unusually wordy RPG. Treat them as prompts for questions, not as production rules; see `qa-insights.md`.
