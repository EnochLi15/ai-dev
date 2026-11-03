> 调研日期 2026-11-03 · 由三个并行研究子会话分别完成（待办/日历、笔记、知识库），方法=HN Algolia+社区讨论+厂商页+GitHub API，未核实项随文标注。

# AI 时代的笔记实践调研（2025–2026）

调研时间 2026-11-03。来源：HN Algolia（stories+comments）、Bing、GitHub API、厂商定价页。未能核实处已标注。

## 1. 主流工具矩阵

| 工具 | 定位 | AI 能力 | 本地/云 | 价格 |
|---|---|---|---|---|
| Obsidian | 本地 Markdown + 插件生态，事实标准 | 官方无内置 AI；插件补齐：Copilot（7.9k★，自带 OpenAI/Ollama key 的聊天+vault 问答）、Smart Connections（5.5k★，本地/远程 embedding 相关笔记+RAG）、obsidian-ai（把 Claude Code 等 agent 带进 Obsidian） | 本地优先 | 2025-02 起商用免费（[官方公告](https://obsidian.md/blog/free-for-work/)，[HN 282p](https://news.ycombinator.com/item?id=43117020)）；Sync 另收费；Smart Connections Pro 被用户吐槽 $300/年（[HN](https://news.ycombinator.com/item?id=49160219)） |
| Notion AI | 团队协作 all-in-one | Notion Agent、AI 会议纪要、跨应用 Enterprise Search；Free/Plus 仅 AI 试用 | 云 | Business $20/人/月起才含完整 AI（[定价页实测](https://www.notion.com/pricing)）；2026-01 曝出未修复的数据外泄漏洞（[HN 206p](https://news.ycombinator.com/item?id=46531565)） |
| Logseq | 开源大纲式+白板 | 无内置，靠插件 | 本地优先（开源） | 免费；2026-07 终于发 2.0 Beta（DB 版，[HN](https://news.ycombinator.com/item?id=48896229)），2026-04 宣布拆成两个版本；45.5k★，仍在活跃维护 |
| Reflect | 云端快速双链笔记，AI 原生卖点 | 内置 AI 编辑/聊天、Whisper 语音转写 | 云 | 付费订阅；官网 JS 渲染，本次未能核实具体价格（诚实标注） |
| mem | AI-native 笔记（AI 自动组织/关联） | 主打 AI 检索代替文件夹 | 云 | 本次未检索到 2025+ 有效讨论，细节未核实 |
| Heptabase | 白板+卡片式可视化研究笔记 | AI agent（Pro 仅 Gemini；Premium 可选 GPT/Claude）、AI credits 按月配额 | 云（本地导出） | Pro $8.99/月（年付）、Premium $17.99、Premium+ $53.99（[定价页实测](https://www.heptabase.com/pricing)） |
| 思源 SiYuan | 开源块级双链，中文生态 | 官方支持"AI 写作与问答，接 OpenAI API"（自备 key） | 本地优先，可 Docker 自建 | 免费+订阅（[GitHub 47.1k★](https://github.com/siyuan-note/siyuan)，星数已超 Logseq） |
| 语雀 | 阿里系团队知识库 | 有 AI 阅读/写作功能，本次检索被噪音淹没，未能核实 2026 现状 | 云 | 免费额度+会员 |
| flomo | 极简卡片速记，"无需格式无需排版，多级标签+每日回顾"（[官网](https://flomoapp.com/)） | 基本无 AI，反效率工具哲学 | 云 | 文字 memo 免费；PRO 价格官网 JS 渲染未核实 |

## 2. 真实习惯共识（社区一线声音）

- **Daily note 是最大公约数**，Zettelkasten 退居少数派实践。典型评论："daily log 降低摩擦——写之前不用想该归档到哪"（[HN](https://news.ycombinator.com/item?id=48957983)）；"从没用起 Zettelkasten，daily notes 更顺手，我的 vault 是日记+研究的混合体"（[HN](https://news.ycombinator.com/item?id=49456175)）；极简派直接 `nvim $(date +%Y/%m/%d).md` 用了五年（[HN](https://news.ycombinator.com/item?id=42990278)。
- **对 PKM 方法论本身出现反思潮**。2026-07 高分长文直接质疑 PKM 工具对真实产出的证据（[HN 257p/97c](https://news.ycombinator.com/item?id=49084324)），高赞评论自嘲"它支持我的学习，仅在于让我感觉自己在做对的事"。Zettelkasten 教程仍常上首页（[2026-04, 117p](https://news.ycombinator.com/item?id=47700556)）但更像内容营销。PARA/LYT 在 2025+ HN 几乎无独立讨论（检索确认，非采样偏差）。
- **"AI 之后还要整理吗"两派并存**。务实派："Obsidian + Claude Code + git，把组织规则写成 AI 可读的规则文件，所有笔记先进 Inbox"（[HN](https://news.ycombinator.com/item?id=46834250)）；"Smart Connections 做本地 embedding 索引，直接和自己的笔记聊天"（[HN](https://news.ycombinator.com/item?id=42990343)）。但整理派并未消失，且 AI 插件体验参差（"从没成功索引完我的 vault"，[HN](https://news.ycombinator.com/item?id=44964344)）。
- **反工具党持续壮大**：471p 的"Ditching Obsidian 自建"（[HN 559 评](https://news.ycombinator.com/item?id=44022448)）与 730p 的极简开源替代 [Files.md](https://news.ycombinator.com/item?id=48179677) 说明"越简单越好"是持续情绪。

## 3. 2025–2026 趋势

1. **Local-first 回潮但被泼冷水**：Ink & Switch 经典文 2025-07 再登 883p（[HN](https://news.ycombinator.com/item?id=44473135)）；同期的"为什么 local-first 没流行"（[505p/485c](https://news.ycombinator.com/item?id=45333021)）结论很冷静——用户不愿承担数据管理责任。
2. **个人 RAG / agent 接管 vault 成为标配玩法**：开源 AI-first 笔记 OpenKnowledge 381p（[HN](https://news.ycombinator.com/item?id=48675435)）；Enzyme 从 Obsidian 插件进化成"第一个 Obsidian MCP"（[HN](https://news.ycombinator.com/item?id=50221079)）；Hubble 直接定位"给你和你的 agents 用的笔记"（[HN](https://news.ycombinator.com/item?id=49091730)）。
3. **会议/语音自动进笔记全面铺开**：Granola 成事实标杆（连 Apple Watch 都上了，[HN](https://news.ycombinator.com/item?id=49089026)）；Google Meet 部分客户默认开启 AI 笔记（[官方](https://workspaceupdates.googleblog.com/2026/07/new-google-meet-take-notes-for-me-settings-for-admins-and-end-users.html)）；医生用 AI 病历笔记救职业倦怠（[HN 260p](https://news.ycombinator.com/item?id=40244165)）。丑闻同样教育市场：Fireflies 被曝早期是"两个人手动打字假装 AI"（[HN 119p](https://news.ycombinator.com/item?id=45934447)）。
4. **生态安全收紧**：Obsidian 插件被滥用投放 RAT（[HN 366p](https://news.ycombinator.com/item?id=48088576)），官方随即发布插件安全路线图（[Future of Plugins](https://news.ycombinator.com/item?id=48109970)）。

## 4. 推荐组合

- **轻量入门**：Obsidian（免费含商用）+ daily note 模板 + 全库一个 Inbox 文件夹，AI 用 Copilot 插件接自己的 API key（$0 起步）；中文速记场景加 flomo 收集碎片，周回顾时并入 Obsidian。
- **重度知识工作者**：Obsidian vault（git 版本控制+官方 Sync）做唯一事实源 + Smart Connections/自建 RAG 供检索 + Heptabase 做文献主题研究 + Granola 或 Whispering（开源本地听写，591p，[HN](https://news.ycombinator.com/item?id=44942731)）把会议/语音自动落成笔记 + Claude Code/MCP 让 agent 直接读写 vault。中文重度用户把编辑器换成思源（本地+Docker 自建+自备模型 key）。

**未核实项**（诚实标注）：Reflect 与 flomo 具体价格、mem 2026 现状、语雀 AI 功能细节——官网 JS 渲染或检索噪音导致，本次未确认。
