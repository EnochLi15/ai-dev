> 调研日期 2026-11-03 · 由三个并行研究子会话分别完成（待办/日历、笔记、知识库），方法=HN Algolia+社区讨论+厂商页+GitHub API，未核实项随文标注。

# 个人知识库（PKM）2025–2026 现状调研：采集→组织→检索闭环与 AI

调研日期 2026-11-03。来源：HN Algolia（story+评论）、GitHub API（星数为当日实测）、Bing/中文源（受限，见文末）。

## 一、四种主流路线

**① 本地 Markdown 库 + AI 检索**（Obsidian 系）。Obsidian 本地 md 文件库仍是社区图腾（[2020 Show HN 1087 分](https://news.ycombinator.com/item?id=23324598)）。AI 侧靠插件：[Smart Connections](https://github.com/brianpetro/obsidian-smart-connections) 5.5k★（写时自动找相关笔记，替代手工链接）、[Obsidian Copilot](https://github.com/logancyang/obsidian-copilot) 7.9k★——其定位已变成 "Run agents in Obsidian - OpenCode, Codex, Claude Code"，即 agent 直接住进笔记库。一体化应用 [Reor](https://github.com/reorproject/reor) 8.5k★，但 2025-05 后无提交，实际停滞。适合：数据主权、长期主义、已有大量文字资产者。

**② 云端一体化**（Notion/语雀/Apple Notes + AI）。Notion AI 面向团队协作。值得注意的反向信号：HN 老用户从 Obsidian/Notion 退回 Apple Notes（[0x4e 评论](https://news.ycombinator.com/item?id=49084324)："Apple Notes + Reminders 够用了，手机端语音转录是最好用的"）。适合：非折腾党、协作场景、苹果生态用户。

**③ 专用 AI 知识库**（喂料→问答/生成）。Google NotebookLM 2026-07 更名 Gemini Notebook（[HN 371 分](https://news.ycombinator.com/item?id=48936451)），音频概览曾是破圈功能（[907 分](https://news.ycombinator.com/item?id=41693087)）。开源自托管：[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) 67.9k★（最活跃，local-first agent）、[Khoj](https://github.com/khoj-ai/khoj) 38k★（"AI second brain"，2026-08 仍活跃，已加 automations/deep research）。[Quivr](https://github.com/The-Vibe-Company/quivr) 39.6k★ 但已转型为"内容流→搜索与监控引擎"，不再是纯 second brain。适合：专题研究、一次性大料消化（论文/访谈/合同）。Saner 在 GitHub 已检索不到（诚实标注：查无此项目）。

**④ 仓库即知识库**（工程师向）。Foam（[HN 396 分](https://news.ycombinator.com/item?id=25760066)）、Dendron（[259 分](https://news.ycombinator.com/item?id=29998680)，已停更）、Markdown Oxide 等基于 VSCode/纯文本 + git。2026 年的新形态是"md 仓 + 常驻 coding agent"：agent 记忆文件（如 CLAUDE.md、handoff 账本）本身就是知识库条目。适合：开发者，知识即代码，版本化、可 grep、agent 可直接读写。

## 二、实践共识（社区真实声音）

**捕获：摩擦趋近于零、多入口而非单库。** [al_borland](https://news.ycombinator.com/item?id=44402470)：iOS Shortcuts 一键带时间戳追加 + Siri/CarPlay 开车语音捕获 + Reminders 当收集箱；Obsidian 只留给工作。语音转写被反复点名为最低摩擦入口。

**组织：2025–2026 主旋律是"反整理"。** [I deleted my second brain](https://news.ycombinator.com/item?id=44402470)（2025-06，598 分）是标志性帖子：sixpackpg 自认"沉迷建造系统而非产出成果"；latexr 的名言"写了永远不会读的笔记，和不写一样无用"。2026-07 Brennan《What have note-taking/PKM apps accomplished, really?》引发大反驳（[回应帖 257 分](https://news.ycombinator.com/item?id=49084324)），Obsidian CEO kepano 亲自下场："问笔记软件成就了什么，就像问相机成就了什么"。具体最小化方案：scuol 的"每日 journal 页 + ≤3 层标签体系，内容只进 journal"；olooney 试遍 Evernote/OneNote/Obsidian 20 年，回归纯文本 + 一个 TODO.md；godot 极端派干脆完全不存档。

**AI 检索对"要不要整理"的冲击：** 共识方向是"少整理、多检索"——Towaway69 自述 "thought hoarder"，称 LLM 对把堆积笔记重新组织/连接/打包成想法有直接价值；Smart Connections 的存在意义就是自动找关联替代手工双链。但需诚实标注：HN 并无"AI 检索全面替代分类"的压倒性结论，反工具化情绪同样强烈，多数高赞评论主张"系统简单到不值得优化，写就是了"。

## 三、知识库 × Agent 记忆（新趋势）

Claude Projects（[2024-06 推出](https://news.ycombinator.com/item?id=40790911)）= 人工策展的静态项目知识；ChatGPT memory = 自动累积的过程记忆，但 HN 反应偏冷且负面（[I turned off ChatGPT's memory](https://news.ycombinator.com/item?id=47132001) 19 分；[memory dossier](https://news.ycombinator.com/item?id=44052246) 24 分）。社区隐性共识是**分工而非替代**：agent 记忆存"过程与偏好"（自动、易失、低信噪比），知识库存"沉淀资产"（人工策展、可检索、可交接）。2026 年融合形态是 agent 常驻知识库：Obsidian Copilot 跑 Claude Code/OpenCode 即例证；本调研所用 DSH 框架的 auto-memory（日志/项目笔记/交接账本分层落盘）是同一思路的工程化实现——agent 记忆按"可归档知识"标准写，反向成为知识库。

## 四、推荐组合

- **普通用户**：Apple Notes（或 Notion）多入口捕获（快捷指令+语音）+ Gemini Notebook 做专题消化（上传源材料→问答/播客复习）。零维护成本。
- **开发者**：markdown 仓（Obsidian 或纯 VSCode + git 管理）+ Smart Connections（库内关联检索）+ Khoj/AnythingLLM 自托管 RAG（跨库问答）+ coding agent 常驻读写（Obsidian Copilot 或 CLAUDE.md 约定），journal 式追加、不分类、靠检索。

## 检索受限说明

中文源（Bing 中国区）仅返回"知识"词条类泛结果，未获 2026 年中文社区（语雀/飞书/Wolai）的一手实践讨论；Capacities/Tana 在 HN 无有效热度信号（Tana 仅 9 分旧帖），其用户共识无法从本渠道验证。
