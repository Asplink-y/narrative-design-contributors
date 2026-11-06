# Example 2 — dialogue rewrite (should trigger)

## User input

```
帮我评审这段分支对话。每个节点都是三个选项：赞成 / 中立 / 拒绝，顺序固定。
主角第一次见到码头管理员时，管理员就把自己的身世、母亲、四十年前的罢工
全都讲了一遍。还有一个技能检定，失败就什么都没发生，玩家只能读档。
```

## Acceptance criteria

1. Cite `A-1` / `P-4` for the fixed three-option pattern and `A-2` / `P-7` if questions and statements are mixed.
2. Cite `A-4` / `P-3` for the first-meeting lore dump, and propose a task-gated return path.
3. Cite `A-5` / `P-9` for the no-consequence failure; convert it into a red check with an advancing failure branch plus a reflection option (`Q-6`), or into a retryable white check (`P-10`) — and state which one was chosen and why.
4. Provide **actual replacement option lines** and a small `Greeting → Main hub → branch → return` diagram.
5. Note that the number of exits should be small and controlled (`P-5`).
6. Include the checklist result with pass / warn / fail.

## Optional tooling

`sample-dialogue.json` in this directory is a machine-checkable version of the same problems. Run:

```bash
python ../skills/narrative-design/scripts/check_dialogue.py sample-dialogue.json
```

Expected: findings for `A-1`, `A-2`, `A-3`, `A-5`, `A-7`, exit code `1`.
