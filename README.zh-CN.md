# 叙事设计工作台（Narrative Design Workbench）

一个遵循 [Agent Skills](https://agentskills.io) 开放标准的开源 Skill。它把《极乐迪斯科》编剧 Helen Hindpere 在 Konsoll 2023 的演讲《How to build (un)believable worlds?》提炼成**可执行的评审与改写工作流**，而不是一份读完就忘的笔记。

[English README](README.md) · [发布指南](docs/publishing.md) · [署名与版权](NOTICE)

## 它不是什么

- 不是通用创意写作课，不教线性小说 / 影视剧本，也不做任务与关卡数值设计。
- 不是经过验证的通用理论：它是一位讲者、一部作品、偏「超大量文本 + 俯视镜头」的入职总览。已知局限写在 `references/qa-insights.md`，`SKILL.md` 里也做了声明。

## 安装

| 目标平台 | 方式 |
| --- | --- |
| Claude Code / 任何支持 Agent Skills 的工具 | 把 `skills/narrative-design/` 复制到 `~/.claude/skills/`（个人）或 `.claude/skills/`（项目） |
| WorkBuddy | 先运行 `python scripts/build_packages.py`，再用「添加技能 → 上传技能」导入 `dist/narrative-design-workbuddy.zip` |
| 其他 | 直接阅读 `skills/narrative-design/SKILL.md` 及 `@references/` 引用的文件 |

Skill 本身不需要联网、不需要 API Key。只有可选的静态检查脚本需要 Python 3。

## 试一下

```
帮我评审这段分支对话：每个节点都固定是三个选项，赞成 / 中立 / 拒绝，顺序也不变。
```

期望输出：识别「固定选项」反模式 → 给出一版混合疑问句/陈述句、带返回路径的改写 → 勾选对应检查项。

更多用例见 [examples/](examples/) 与 [evals/evals.json](evals/evals.json)。

## 仓库结构

```
narrative-design-skill/
├── skills/narrative-design/     # 可分发的 Skill 包（唯一内容源）
│   ├── SKILL.md                 # frontmatter + 阶段路由 + 输出契约
│   ├── references/              # 仅在对应阶段按需加载
│   ├── templates/               # 评审报告模板、对话骨架模板
│   └── scripts/check_dialogue.py
├── scripts/
│   ├── validate_skill.py        # frontmatter / 结构 / 引用检查（仅标准库）
│   └── build_packages.py        # 生成两种发行包
├── examples/                    # 用例与验收标准
├── evals/evals.json             # 触发与行为测试
├── docs/publishing.md
└── .github/workflows/validate.yml
```

## 工作流

1. 判断用户所处阶段：**立项设定 / 系统设计 / 写具体对话 / 评审改稿**。
2. 只加载对应的 `@references/...` 文件。
3. 固定输出三段：**诊断 → 可直接使用的改写 → 检查清单勾选**。
4. 举例优先用演讲里的实例（橙衣女孩、金作为反衬角色、红/白检定），不要凭空造例子。

## 构建与校验

```bash
python scripts/validate_skill.py
python skills/narrative-design/scripts/check_dialogue.py --self-test
python scripts/build_packages.py
```

产出两个 zip：

- `dist/narrative-design-agent-skills.zip` —— 标准 6 字段 frontmatter
- `dist/narrative-design-workbuddy.zip` —— WorkBuddy 市场所需字段

两个包的顶层都必须是 `narrative-design/` 文件夹且 `SKILL.md` 位于其根目录；缺少这层目录是技能包解析失败的常见原因。

## 来源与许可

本仓库是**方法层面的独立提炼**，不含演讲的逐字稿、字幕文本、PPT 译文或截图。完整署名见 [NOTICE](NOTICE)。原创文字与代码采用 [MIT](LICENSE)，专有名词仅作识别用途。若要再分发翻译后的 PPT 或字幕，请先取得相应权利人授权。

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。新增内容请保持「方法化 + 原创表述」，并为新增触发词补一条 eval 用例。
