# Dialogue skeleton and linter schema

## Skeleton

```
[Greeting]  (once; establishes the character; early leave available)
    |
    v
[Main hub] <----------------------------+
    |  River / Hub / White check / ...   |  every branch returns here
    |  [Whirlpool] -> aside -> back to skipped option
    |  [Red check] -> success OR failure, both advance
    |  [Passive check] -> interjection -> new option
    +--> [Leave option]  (exit)
```

Conventions to keep explicit in the design doc:

1. New questions appear only in the main hub.
2. Exits: one in the greeting, one in the hub. No others.
3. Flag/variable changes happen at the hub convergence, not scattered across branches.
4. Whirlpool asides share one wording convention (for example, starting with "Wait…" / 「等等…」).
5. Red checks are one-shot and their failure has both a consequence and a reaction option.
6. White checks can be retried after the player gains skill or information.

## JSON schema for `scripts/check_dialogue.py`

```json
{
  "title": "example hub",
  "nodes": [
    {
      "id": "greeting",
      "type": "greeting",
      "is_exit": true,
      "options": [
        {"text": "Hello.", "kind": "statement", "leads_to": "hub"}
      ]
    },
    {
      "id": "hub",
      "type": "hub",
      "options": [
        {"text": "Where are you from?", "kind": "question", "leads_to": "origin"},
        {"text": "I think you are lying.", "kind": "statement", "leads_to": "accuse"},
        {"text": "Leave.", "kind": "statement", "is_exit": true}
      ]
    }
  ],
  "checks": [
    {
      "type": "red",
      "node": "accuse",
      "failure_advances": true,
      "reflection_option": true,
      "retryable": false
    }
  ]
}
```

Field notes:

- `options[].kind`: `question` or `statement`. Omit it and the linter infers from a trailing `?` / `？` or a question word.
- `is_exit`: marks a node or an option as an exit.
- `checks[].type`: `passive`, `red`, `white`.
- `failure_advances`, `reflection_option`, `retryable` are booleans, relevant to red checks.

## Rules the linter reports

| Code | Finding | Trigger |
| --- | --- | --- |
| A-1 | Fixed option count across hubs / repeated stance order | all hub nodes share one option count ≥2, or a repeated `stance` sequence |
| A-2 | Question mixed with statements in one set | a node has ≥1 question and ≥1 statement |
| A-3 | Too many exits | exit count > 2 |
| A-5 | Red check failure mishandled | `failure_advances` false or missing |
| A-7 | No reflection after a negative outcome | `reflection_option` false or missing |

Exit code is `1` when any finding is present, `0` when clean, so CI can gate on it. Use `--self-test` to verify the linter's own cases without a data file.
