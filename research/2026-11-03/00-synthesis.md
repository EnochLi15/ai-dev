# 2026-11 AI 生产力三问：待办日历 · 记笔记 · 知识库（三会话并行调研合成）

> 调研方式：三个独立调研会话并行执行，只采信近 90 天一手信源（HN Algolia 全文检索 + 官网定价页/GitHub/TechCrunch 直抓），每条结论带链接带日期；查不到近期一手信源的一律标注"未验证"。合成时间：2026-11-03。

## 0 · 总览：三个领域收敛到同一个元趋势

1. **「文件 + git + agent 直读直写」正在赢过「SaaS 数据库 + 内置 AI 魔法」**。记笔记和知识库领域已明确收敛：本地 markdown 库因 agent（Claude Code/Codex）可直接读写文件而意外翻红，第一代 AI-native 独立应用（Reor 归档、Khoj/Saner 转型）大面积退潮。
2. **"AI 自动整理"被社区普遍证伪，真价值集中在两端**：输入端（语音/会议自动捕获）和输出端（按需检索/防御性排程）。中间的自动打标签/自动链接/自动重排，工程师群体要么嘲讽为噱头，要么因失控感弃用。
3. **付费情绪转向买断制与免费档**：订阅+AI 点数计费（Motion 式）引发反感；£2 买断小工具 118 赞、Reclaim 免费层口碑最稳、Gemini 免费晨报实用，都是同一信号。
4. **知识库正在"人机共写"**：CLAUDE.md/AGENTS.md 本身就是给 agent 的知识库；"为两个读者（人+agent）设计"成为组织原则，扁平短页优于深层链接图。

## 1 · AI 待办与日历：三分格局，工程师怕失控

**阵营表**（定价均为官方页 2026-11-03 核实）：

| 阵营 | 工具 | 定位 | 价格 | 一句话 |
|---|---|---|---|---|
| 全托管自动排程 | Motion | AI 全托管日历+项目 | ~$29/月起 + AI 点数/seat | AI 决定你何时做什么；口碑两极 |
| 全托管自动排程 | **Reclaim.ai**（被 Dropbox 收购，非 Google） | 防御 focus/habits/tasks | Lite 免费；$10-15/seat/月 | 不替换日历，在 Google/Outlook 上打可伸缩保护块；**口碑最稳** |
| 手动+AI | Akiflow | 键盘流捕获+排块 | $19/月（年付） | 聚合 Slack/Jira/GitHub 多源任务 + command bar |
| 手动+AI | Sunsama | 每日规划仪式 | $17-22/月 | 反自动化：每天只让你挑少量任务，防过载 |
| 手动+AI | Morgen | 统一日历+排块 | $10-19/月 | 多日历聚合+AI 建议，自称中间派（营销内容） |
| 日历原生 AI | **Gemini**（Calendar+Spark） | 免费 agent | 随 Workspace | 每天定时读邮件+日历+Drive 出晨报、语音建事件；**不会**替你重排任务块 |
| 原生 AI | Todoist Assist | 语音/文件→任务 | 免费层可用 | Ramble 语音意识流转任务 + PDF/照片抽任务 |

（Amie/Vimcal/Routine/Rise/Skedpal 未验证近期动态。）

**工程师真实情绪（一手）**：OwnTime（£2 买断，[HN 118 赞 2026-09-01](https://news.ycombinator.com/item?id=49528506)）评论区是标本——愿为买断制付费、要 time-boxed todo 而非 AI 代管；DIY 派直言 "LLM CLIs and ics are all you need"（[2025-10-17](https://news.ycombinator.com/item?id=45615015)）；Motion 负面口碑集中在"全天被随机重排的焦虑"+AI 点数使账单上浮 20-40%（Reddit 二手转述，竞品博客需打折读）；Reclaim 正面口碑："15 分钟配好、安静守住 focus time 不乱动"（[lindy 实测 2026-09-09](https://lindy.ai/blog/motion-vs-reclaim)）。

**常见工作流**：语音/键盘捕获（Todoist Ramble / Akiflow）→ 排程交 Reclaim 防御占位或 Sunsama 手动日规划 → 晨间 briefing 交 Gemini 定时任务。

**分场景推荐**：会议多保深度工作 → Reclaim（免费起步）；AI 全托管预算足 → Motion（须接受重排+点数）；键盘流任务源分散 → Akiflow；防过载仪式感 → Sunsama；零成本 → Gemini 晨报 + Todoist Ramble；极客 → LLM CLI + ics 自建。

## 2 · 记笔记：哑 markdown 复辟，AI-native 独立应用退潮

**格局三分**：大而全（Notion，官方方向是把 Notion 做成 agent 共享记忆，[2026-08-19](https://www.notion.com/blog/building-shared-memory-for-ai-agents-in-notion)）；本地文件（Obsidian 生态最活跃）；AI-native 新物种（第一代死伤殆尽：Reor 归档、Khoj 转型研究工作台、Saner 转 ADHD 助理；新一代是"给 agent 用的笔记本"：[Hubble](https://www.hubble.md/)（HN 151 赞）、[Lapse](https://lapse.in)（MCP 共享记忆）、[Mnemoloci](https://github.com/siris9476/mnemoloci)（Claude Code 二脑））。

**工程师主流玩法**：「纯 markdown 库 + 编码 agent 直读直写」——Obsidian Copilot 插件干脆转型为"在 Obsidian 里跑 OpenCode/Codex/Claude Code"（[repo](https://github.com/logancyang/obsidian-copilot)，11-03 仍在更新）。"哑 markdown 就够了"派：257 赞热帖（[2026-07-28](https://news.ycombinator.com/item?id=49084324)）高赞评论——教科书笔记打进一个 dumb md 文件、全文搜索即可，复杂 PKM 是焦虑产物。

**真价值 vs 噱头**：✅ 捕获（会议/语音→结构化笔记：Granola、[Google Foresight 本地优先](https://techcrunch.com/2026/10/08/google-releases-a-new-local-first-granola-competitor/)、开源 [meetcap](https://github.com/seacen/meetcap)）；✅ 检索联动（agent 按需读库）；❌ AI 自动整理/链接/标签（被普遍嘲讽为"生产力安慰剂"）。

**推荐组合**：Obsidian/markdown 库 + Claude Code 直读直写 + [Smart Connections](https://github.com/brianpetro/obsidian-smart-connections)（本地 embedding）或 Fast Find（fzf+embeddings 混合）检索；会议捕获用 meetcap（开源本地）或 Granola，产出直接落 md 进库。

## 3 · 知识库：方法论退潮，"agent 记忆文件格式"成最热范式

**形态收敛**：本地 markdown vault + git（Obsidian 头部壳；极简派 [files.md](https://github.com/zakirullin/files.md) HN 730 赞、AI-first 派 [OpenKnowledge](https://github.com/inkeep/open-knowledge) 381 赞）。方法论（PARA/Zettelkasten/MOC）热度退潮，[Ask HN hoard notes](https://news.ycombinator.com/item?id=46826277)（235 赞/217 评）社区结论："**Collecting was the bottleneck, not organizing**"——痛点是按需召回而非组织，隐私/本地是硬性要求。

**最热方向：agent 记忆 = 文件格式**。Cal Paterson《[Agent memory as a file format](https://calpaterson.com/memoryfields.html)》（191 赞）：md 短页（≤8KB）+ YAML frontmatter + 可选 SQLite 向量索引；agent 直接写 prose，不做 chunk/图谱——图遍历需 N+1 次串行工具调用，实测慢且不可靠。同范式：Google OKF + FTS5 的 MCP memory（[2026-08-13](https://news.ycombinator.com/item?id=49286073)）、git-native OKF（[2026-09-05](https://news.ycombinator.com/item?id=49581240)）。mem0 等"记忆层 SaaS"热度被轻量文件方案取代。反例：Obsidian RAG 插件实测口碑差（"没有一个做对了，扩展很脆"）。

**AI 园丁派工作流**（Rob Dodson，[2026-02-08](https://robdodson.me/posts/i-gave-my-second-brain-a-gardener/)）：人只管往 daily note 倾倒，Claude Code 读整个 vault 制定组织方案、把规则写进 CLAUDE.md 固化、skill 把碎片加工成结构化笔记——"AI 做认知劳动（打标签/链接/成形），不做思考（生成想法）"。

**给 AI 开发者的落地建议**：git 管理 markdown vault 零数据库；原子短页（≤2000 token）+ 扁平目录 + 少量 MOC 索引；组织规则写进 CLAUDE.md/AGENTS.md；检索 grep/FTS5 为底座、SQLite 向量做补充，不上 pgvector+Neo4j 重型方案；**优先治理输入（减少采集）而非优化检索**。

## 4 · 给你的一页落地组合（AI 开发者视角）

- **待办/日历**：Reclaim 免费档守住深度工作块 + Todoist Ramble 语音捕获 +（可选）Gemini 定时晨报。想要全托管再考虑 Motion。
- **记笔记**：git 管理的 markdown 库（Obsidian 或裸文件）为唯一事实源；Claude Code/Codex 直读直写；会议用 meetcap 转写落库。
- **知识库**：与笔记同一个库；扁平短页 + CLAUDE.md 写组织规则；grep/FTS5 检索，向量做补充；把"给 agent 的记忆"（frontmatter 短页）作为一等公民设计。
- **共同原则**：文件 > SaaS；买断/免费 > 点数订阅；AI 管捕获和检索，人管想法和取舍。

---
*子会话原始报告（含完整信源列表）存于本仓库 `research/` 目录：01-todo-calendar.md、02-notes-ai.md、03-knowledge-base.md。*
