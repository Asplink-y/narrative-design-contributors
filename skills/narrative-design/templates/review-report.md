# Review report template

Copy this structure for part 3 of every review. Replace the bracketed text and delete unused sections. Do not paste the full checklist when only one stage was reviewed.

```markdown
## 诊断 Diagnosis
- [A-1] 每个节点都固定 3 个选项且好/中立/坏同序 → 玩家不再阅读，只是在按键。证据：`hub_03`, `hub_04`。
- [P-7] `hub_02` 把疑问句与表态陈述句混排 → 玩家会几乎总选疑问句。

## 改写 Rewrite
### hub_02（原 3 项 → 改为 2 项，全陈述句）
- 「我认为你在隐瞒那晚的事。」
- 「算了，先不谈这个。」→ Leave option

### 新增：Whirlpool 插问（统一以「等等…」开头）
- 「等等，你说的是哪艘船？」→ 回答后回到 hub_02

## 检查清单 Checklist
| 项目 | 规则 | 结果 |
| --- | --- | --- |
| 选项数量与顺序有变化 | A-1 / P-4 | WARN (fixed in rewrite) |
| 疑问句未与陈述句混排 | A-2 / P-7 | PASS |
| 退出点受控（≤2） | A-3 / P-5 | PASS |
| 长背景未在第一面倾倒 | A-4 / P-3 | PASS |
| 红检定失败有后果 + 反思出口 | A-5 / A-7 / P-9 | FAIL (no red check supplied) |
| 可视化结构图存在 | P-1 | not checked |
```

## Full four-stage checklist

Use these when asked for a complete audit. Mark `not checked` when the artefact was not supplied.

### A. Worldbuilding
- [ ] W-1 world type stated, expansion plan explicit
- [ ] W-3 ≥10 plot-independent named details
- [ ] W-4 unseen locations / unreachable characters / irrelevant history recorded
- [ ] W-5 a real-world story translated into the setting this cycle
- [ ] W-6 ≥3 genre tests, byproducts filed as NPCs or in-world documents

### B. System design
- [ ] D-1 text budget derived from camera and animation capacity
- [ ] D-2 one non-traditional supporting voice, or a deliberate choice against it
- [ ] D-3 a named element owns onboarding, recaps and next-step hints
- [ ] D-4 small situational decisions precede abstract moral ones
- [ ] D-5 every check type defines what failure does
- [ ] D-6 pacing includes rest beats

### C. Dialogue
- [ ] P-1 visual tool or maintained diagram
- [ ] P-2 playtest feedback on option expectations collected
- [ ] P-3 long backstory gated behind a task or check
- [ ] P-4 option counts and tones vary
- [ ] P-5 hub, return paths, ≤2 exits visible
- [ ] P-7 no question mixed with stance statements
- [ ] P-8 whirlpool convention consistent and returns correctly
- [ ] P-9 / P-9b red failure advances and offers a reaction
- [ ] P-10 / P-11 passive, red, white distinguishable

### D. Review process
- [ ] ≥3 people tried the scene, or `not checked` for solo projects
- [ ] Difficult-topic material (Q-1) had extra editing and varied readers, or is marked N/A
- [ ] Information load and rest beats (Q-2, D-6) assessed
- [ ] Negative outcomes have a reflection outlet (Q-6)
- [ ] `scripts/check_dialogue.py` run on the supplied JSON, or marked N/A
