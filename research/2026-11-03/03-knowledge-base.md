# AI 时代的个人知识库（PKM）· 2026-11 调研（子会话 3/3 原始产出）

## TL;DR
1. 2026 年工程师的主流形态已收敛为「本地 Markdown 文件夹 + git + AI/agent 作为读写者」：Obsidian 是头部壳，files.md 这类极简 md 工具（HN 730 赞）和 AI-first 挑战者（OpenKnowledge，381 赞）都在抢同一生态位。
2. 方法论热（PARA/Zettelkasten/MOC）明显退潮：近期高赞讨论的共识是「组织不是瓶颈，检索和输入才是」，结构从给人导航的超链接图转向给 agent grep 的扁平短页。
3. 最热的方向不是"知识库软件"而是"agent 记忆文件格式"：markdown 页 + YAML frontmatter + SQLite 索引成为事实范式（memoryfields、OKF、CLAUDE.md/AGENTS.md），用户实测普遍否定重型 RAG 管道和图遍历。

## 一、知识库形态与组织法现状
- **形态**：Obsidian（vault = 本地 md 文件）仍是头部，官方 2026 年密集补齐工程能力：CLI（[2026-02-10](https://news.ycombinator.com/item?id=46961430)）、Sync headless client（[2026-02-28](https://news.ycombinator.com/item?id=47197267)，587 赞）、插件架构重构（[2026-05-12](https://obsidian.md/blog/future-of-plugins/)，452 赞）。极简派崛起：[files.md](https://github.com/zakirullin/files.md)（"local-first, LLM-friendly, own your data as plain local files"，[2026-05-18](https://news.ycombinator.com/item?id=48179677)）；AI-first 派：[OpenKnowledge](https://github.com/inkeep/open-knowledge)（Inkeep 出品，[2026-06-25](https://news.ycombinator.com/item?id=48675435)）。视觉派（Heptabase/Canvas）仍是小众对比话题（[2026-10-28](https://www.fluxlinks.com/blog/obsidian-canvas-vs-heptabase)）；Notion 数据库派在 HN 工程师工作流里出场率低。
- **方法论**：PARA 上一次上 HN 是 2022-2023（[fortelabs](https://fortelabs.co/blog/para/)），2026 年无新热度；Zettelkasten 教程仍有稳定流量（[2026-04-09](https://news.ycombinator.com/item?id=47700556)）。真实讨论转向幻灭：unattributed.cc（[2026-07-28](https://news.ycombinator.com/item?id=49084324)，257 赞）回应"PKM 到底产出了什么"的质疑；[Ask HN: hoard notes](https://news.ycombinator.com/item?id=46826277)（2026-01-30，235 赞/217 评）社区结论：痛点是"按需召回"而非组织，且"隐私/本地是硬性要求"；高赞答案直接说"Collecting was the bottleneck, not organizing"——减少输入比更好检索更重要。

## 二、工程师真实工作流（HN 一手实测）
- **Logseq 派**（appsoftware，[46826277](https://news.ycombinator.com/item?id=46826277)）：block 层级即结构，靠 Linked References 回溯，定期手工"修剪"重命名合并笔记；需要 brief 时整主题导出→LLM 汇总。明确反对 AI 代写："笔记只有是我写的才有意义"。
- **grep 派**（Neywiny）：项目旁 notes.txt + 全局 grep，"非常糙但够用"。
- **AI 园丁派**（Rob Dodson，[2026-02-08](https://robdodson.me/posts/i-gave-my-second-brain-a-gardener/)）：人只管往 daily note 倾倒，Claude Code 读整个 vault 制定组织方案、写 CLAUDE.md 固化规则、/process-daily skill 把碎片加工成结构化笔记——"让 AI 做认知劳动（打标签/链接/成形），不做思考（生成想法）"。同款：Claude Code + Obsidian second brain（[2026-05-03](https://canatak.substack.com/p/i-dont-need-to-know-everything-i)）。
- **链接收集**：自托管 Karakeep 存链接，AI 自动打标签+摘要+截图（[47128495](https://news.ycombinator.com/item?id=47128495)，2026-02-23）；flatnotes + cron 提交 git；Obsidian 存笔记、Karakeep 存文章成为常见分工。
- **反例（重要）**：Obsidian RAG 插件实测口碑差——mstump："没有一个插件做对了，扩展很脆"，改用 Cursor/自定义 bot；本地嵌入索引"7900xtx 上要跑 24 小时，直接放弃"（同帖）。

## 三、AI/agent 带来的变化
- **agent 记忆 = 文件格式**（当前最热）：Cal Paterson《Agent memory as a file format》（[2026-08-31](https://calpaterson.com/memoryfields.html)，191 赞）：记忆应是数据而非管道；格式 = md 短页（≤8KB/页，YAML frontmatter）+ 可选 SQLite 向量索引；agent 直接写 prose，不做 chunk/图谱——实测图遍历（Karpathy LLM-wiki 路线）需 N+1 次串行工具调用，慢且不可靠。Google OKF 格式 + SQLite FTS5 的 MCP memory（[2026-08-13](https://news.ycombinator.com/item?id=49286073)）、git-native OKF agent memory（[2026-09-05](https://news.ycombinator.com/item?id=49581240)）同范式；Karpathy wiki 模式 2026-04 起涌现大量实现（[llmwiki.app](https://news.ycombinator.com/item?id=47598413) 等）及批评文。Omnara（[2026-10-28](https://www.omnara.com/blog/agent-memory-is-in-the-wrong-place)）：记忆不该绑死单一 sandbox 文件系统。mem0 等"记忆层 SaaS"（2025-10 融资 $24M）2026 年 HN 热度被轻量文件方案取代；跨厂商格式尝试：Universal Memory Protocol（[2026-06-06](https://news.ycombinator.com/item?id=48428796)）。
- **平台记忆与反弹**：Claude Code memory 官方文档（[2026-02-26](https://code.claude.com/docs/en/memory)）、OpenAI "Dreaming"（[2026-06-04](https://openai.com/index/chatgpt-memory-dreaming/)）；但关闭记忆的帖子持续出现（[2026-02-24](https://every.to/also-true-for-humans/why-i-turned-off-chatgpt-s-memory)、[2026-10-21](https://huggingface.co/blog/dacorvo/the-ambiguous-state-trap)）。
- **边界之争**：知识库正在变成"人机共写"——AGENTS.md/CLAUDE.md 本身就是给 agent 的知识库（Dodson："与其给它建 second brain，不如让它替我建"）；反方：[Stack Overflow Blog](https://stackoverflow.blog/2026/03/19/ai-is-becoming-a-second-brain-at-the-expreme-of-your-first-one/)（2026-03-19）警告 AI 第二大脑侵蚀第一大脑，korin.uk（[2026-09-21](https://korin.uk/your-second-brain-wont-do-the-work)）"second brain 不代做工作"。结构上共识：为两个读者（人 + agent）设计，扁平短页优于深层链接图。

## 四、给 AI 开发者的落地建议
1. **库**：一个 git 管理的 markdown vault（Obsidian/裸文件均可），零数据库；frontmatter 只留 title/date/summary。
2. **组织**：原子短页（≤2000 token/页，超长即拆页）+ 扁平目录 + 少量 MOC 索引页；别建深层图谱——agent 图遍历实测低效（Cal Paterson）。
3. **AI 分工**：agent 做"园丁"（整理、打标签、合并、生成 daily brief），人做"作者"；组织规则写进 CLAUDE.md/AGENTS.md 让规则可复用。
4. **检索**：grep/FTS5 为底座，SQLite 向量索引做语义补充；不要上 pgvector+Neo4j+管道的重型方案，也别依赖单一厂商 memory API。
5. **输入治理**：优先减少采集（自选 RSS/AI 摘要），而非无限优化检索——这是 hoard 帖最高频的一手结论。

## 信源列表
- HN: unattributed.cc PKM (2026-07-28) https://news.ycombinator.com/item?id=49084324
- HN: Ask HN hoard notes (2026-01-30) https://news.ycombinator.com/item?id=46826277
- HN: Ask HN where save links (2026-02-23) https://news.ycombinator.com/item?id=47128495
- HN: files.md (2026-05-18) https://news.ycombinator.com/item?id=48179677
- HN: OpenKnowledge (2026-06-25) https://news.ycombinator.com/item?id=48675435
- HN: Obsidian Sync headless (2026-02-28) https://news.ycombinator.com/item?id=47197267
- HN: Future of Obsidian Plugins (2026-05-12) https://news.ycombinator.com/item?id=48109970
- HN: Obsidian CLI (2026-02-10) https://news.ycombinator.com/item?id=46961430
- Cal Paterson: Agent memory as a file format (2026-08-31) https://calpaterson.com/memoryfields.html
- Rob Dodson: second brain gardener (2026-02-08) https://robdodson.me/posts/i-gave-my-second-brain-a-gardener/
- HN: MCP Memory OKF+FTS5 (2026-08-13) https://news.ycombinator.com/item?id=49286073
- HN: OKF Agent Memory git-native (2026-09-05) https://news.ycombinator.com/item?id=49581240
- Omnara: Agent Memory Is in the Wrong Place (2026-10-28) https://www.omnara.com/blog/agent-memory-is-in-the-wrong-place
- OpenAI: ChatGPT memory Dreaming (2026-06-04) https://openai.com/index/chatgpt-memory-dreaming/
- Claude Code memory docs (2026-02-26) https://code.claude.com/docs/en/memory
- HN: Universal Memory Protocol (2026-06-06) https://news.ycombinator.com/item?id=48428796
- HN: Zettelkasten in Obsidian (2026-04-09) https://news.ycombinator.com/item?id=47700556
- HN: Canvas vs Heptabase (2026-10-28) https://news.ycombinator.com/item?id=50274139
- SO Blog: AI second brain (2026-03-19) https://stackoverflow.blog/2026/03/19/ai-is-becoming-a-second-brain-at-the-expense-of-your-first-one/
- every.to: turned off ChatGPT memory (2026-02-24) https://every.to/also-true-for-humans/why-i-turned-off-chatgpt-s-memory
- canatak: Claude Code + Obsidian (2026-05-03) https://canatak.substack.com/p/i-dont-need-to-know-everything-i
- TechCrunch: mem0 $24M (2025-10-28) https://techcrunch.com/2025/10/28/mem0-raises-24m-from-yc-peak-xv-and-basis-set-to-build-the-memory-layer-for-ai-apps/
- 未验证项：Tana/Capacities/Logseq 2026 年官方动态（未搜到近期一手信源）；Notion AI 工程师采用率（无量化数据）。
