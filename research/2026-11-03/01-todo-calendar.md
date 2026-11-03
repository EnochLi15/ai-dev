# AI 待办/日历工具调研（2026-11-03）

## TL;DR
1. 市场三分：**全托管自动排程**（Motion/Reclaim 系）、**手动 time-blocking + AI 辅助**（Akiflow/Sunsama/Morgen，工程师主流口味）、**日历原生 AI**（Gemini：免费但只会建事件/晨报，不会替你重排任务）。
2. 重要纠正：Reclaim.ai 是被 **Dropbox** 收购（2024-08，非 Google），收购后独立运营、定价不变、新增 Outlook 支持与 AI agent/MCP 连接器，免费层厚实，是 2026 口碑最稳的"防御型"选择。
3. 工程师圈情绪：对 Motion 式"AI 重排我一天"的失控感与订阅+AI 点数计费的反感明显；HN 更买账买断制小工具与 DIY 路线（LLM CLI + ics）。

## 工具格局表
| 阵营 | 工具 | 定位 | 价格（官方页核实 2026-11） | 一句话 |
|---|---|---|---|---|
| 自动排程 | Motion | AI 全托管日历+项目 | ~$29/月起 + AI 点数/seat（官方 pricing 页已改 credits 制） | AI 决定你何时做什么，会议一变全天重排；口碑两极 |
| 自动排程 | Reclaim.ai (Dropbox) | 防御 focus/habits/tasks | Lite 免费；Starter $10、Business $15/seat/月 | 不替换日历，在 Google/Outlook 上打可伸缩的保护性时间块 |
| 自动排程 | Skedpal / Trevor AI | 自动 time-blocking | 未核实 / 有免费层 | Trevor 免费、学习用户排程习惯（lindy.ai 2026-09-09） |
| 手动+AI | Akiflow | 键盘流捕获+排块 | $19/月（年付，官方页） | 聚合 Slack/Jira/GitHub 等多源任务 + command bar；"AI 半成品"（lindy.ai 2026-09-18） |
| 手动+AI | Sunsama | 每日规划仪式 | $17-22/月（官方页） | 反自动化：每天只让你挑少量任务进日历，防过载 |
| 手动+AI | Morgen | 统一日历+排块 | $10-19/月（官方页） | 多日历聚合+AI 建议，自称 Motion/Reclaim 中间派（官方博客 2026-10-01，营销内容） |
| 手动+AI | Amie / Vimcal / Routine | 颜值 / 键盘速度 / 一体化 | **未验证近期动态** | 2026-09 后未见一手讨论（Vimcal 仅 lindy 榜单提及） |
| 原生 AI | Gemini（Calendar + Spark） | 免费 agent | 随 Workspace | "每天 7 点读邮件+日历+Drive 出晨报"、Gmail 触发器、语音建事件；不能自动重排任务块（Google 帮助文档 2026-10） |
| 原生 AI | Todoist Assist | 语音/文件→任务 | 免费层可用，Pro 无限 | Ramble 语音意识流转任务（TechCrunch 2026-01-21）+ Capture Assist 从 PDF/照片抽任务（2026-11-01 评测） |

Things 3：无官方 AI，生态靠第三方（**未验证近期动态**）。Rise：**未验证近期动态**。Notion Calendar：仍有第三方集成动态（HN 2026-08-20 Superhuman 集成帖）。

## 工程师真实用法（一手讨论）
- **买断制小工具受捧**：Show HN: OwnTime（£2 买断的"优先级时间预算"App，2026-09-01，118 赞）评论区是工程师口味标本——愿为买断制付费、吐槽"文案一股 AI 味"、要 time-boxed todo 而非 AI 代管。https://news.ycombinator.com/item?id=49528506
- **DIY 派**："No AI calendar needed. LLM CLIs and ics are all you need"（2025-10-17）：用 LLM CLI + ics 自建，不上订阅。https://news.ycombinator.com/item?id=45615015
- **Motion 负面口碑**（二手转述 Reddit）：$600/月 Business 档不值、AI 点数使账单上浮 20-40%、日历随机重排不遵偏好（Morgen 博客 2026-10-01，竞品博客需打折读）；Lindy 编辑实测 3 周弃 Motion 转 Reclaim，理由"全天被重排的焦虑"（2026-09-09）。
- **Reclaim 正面口碑**："15 分钟配好、安静守住 focus time 不乱动"；多篇横评同结论：个人选 Reclaim、重度团队选 Motion（thebusinessdive 2026-01-05、lindy.ai 2026-09-09）。
- 常见工作流：任务捕获用语音（Todoist Ramble）或键盘（Akiflow/快捷键）→ 排程交给 Reclaim 防御式占位或 Sunsama 手动日规划 → 晨间 briefing 交给 Gemini 定时任务。

## 推荐（分场景）
- 会议多、要保深度工作时间：**Reclaim**（免费起步/$10 月）
- 要 AI 全托管、预算充足：**Motion**（$29+/月，须接受重排与点数计费）
- 键盘流、任务源分散：**Akiflow**（$19/月年付）
- 防过载、要仪式感：**Sunsama**（$17-22/月）
- 零成本：**Gemini 晨报 + Todoist Ramble 语音捕获**
- 极客：LLM CLI + ics 自建

## 信源列表
- HN: OwnTime 118 赞帖及评论 2026-09-01 https://news.ycombinator.com/item?id=49528506
- HN: No AI calendar needed 2025-10-17 https://news.ycombinator.com/item?id=45615015
- HN: Ask HN What Todolist App Has the Best UI 2026-02-18 https://news.ycombinator.com/item?id=47066297
- Dropbox 收购 Reclaim: TechCrunch 2024-08-22 https://techcrunch.com/2024/08/22/dropbox-acquires-index-ventures-backed-ai-scheduling-tool-reclaim-ai ；官方 https://reclaim.ai/blog/dropbox-acquires-reclaim
- Reclaim 定价/功能（2026）: https://reclaim.ai/compare/google-gemini-alternative ；ZoomInfo Review 2026 https://pipeline.zoominfo.com/sales/reclaim-ai-review
- Motion vs Reclaim 横评（用户实测）: lindy.ai 2026-09-09 https://lindy.ai/blog/motion-vs-reclaim ；thebusinessdive 2026-01-05 https://thebusinessdive.com/reclaim-vs-motion
- Motion 负面口碑转述（Reddit via 竞品博客）: Morgen 2026-10-01 https://morgen.so/blog-posts/motion-vs-reclaim
- 20+ 排程工具横评: lindy.ai 2026-09-09 https://lindy.ai/tools/ai-appointment-setter ；AI schedule generators 2026-09-18 https://lindy.ai/blog/ai-schedule-generator
- 官方定价页（2026-11-03 抓取）: usemotion.com/pricing（已改 AI credits 制）、akiflow.com/pricing（$19/月年付）、sunsama.com/pricing（$17-22/月）、morgen.so/pricing（$10-19/月）
- Gemini 日历/定时任务: Google 帮助文档 https://support.google.com/gemini/answer/15305236 、https://support.google.com/gemini/answer/17094710
- Todoist Ramble: TechCrunch 2026-01-21 https://techcrunch.com/2026/01/21/todoists-app-now-lets-you-add-tasks-to-your-to-do-list-by-speaking-to-its-ai ；Capture Assist 中文评测 2026-11-01 https://xlrocket.blog/2026/11/01/todoist-task-capture-assist-评测
