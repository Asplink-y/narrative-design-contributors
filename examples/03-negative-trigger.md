# Example 3 — negative trigger (should NOT trigger)

## User input

```
我在写一部线性长篇小说，第三章的对话节奏有点拖，帮我润色一下这段，
让两个人吵架更有张力，别改设定。
```

## Expected behaviour

The skill should **not** load. This is linear prose, not an interactive artefact: no branching options, no checks, no world/system design decision. Applying hub/return-path or skill-check rules here would be a category error.

If the user explicitly asks for the skill anyway, it should say the rules do not transfer and offer only the general note that `D-1` concerns camera/media differences, without forcing a checklist.

## Why this case exists

Over-eager triggering is the most common failure of knowledge-heavy skills. A short `description` that lists use cases *and* exclusions, plus negative eval cases, keeps the skill from hijacking ordinary writing requests.
