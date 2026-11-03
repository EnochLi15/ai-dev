> 第二轮架构分析 · 2026-11-03 · 由三个并行研究子会话各自深挖高星开源项目（README/docs 直读+gh api 星数与活跃度核实），回答"当前最优技术方案"；未核实项随文标注。

# 待办/日历:当前最优技术方案——高星开源项目深挖(2026-11-03)

第一轮产品对比(见 ai-todo-calendar.md)是背景。本轮结论:**领域没有"一个赢者通吃的 app",胜出的是分层架构**——SaaS 数据源 + MCP 标准访问层 + agent 编排 + 人在回路 UI。两个 28k★ 明星项目同在 2026 年商业化失败,反而验证了这一点。

## 1. cal.com / Cal.diy — 排期基础设施([repo](https://github.com/calcom/cal.com) 49,663★,今日仍有 push)

- **架构**:Turborepo monorepo,Next.js + tRPC + React + Tailwind + Prisma + Daily.co(README "Built With")。核心抽象是 **event-type(可预订的事件模板)**:用户把"我有空的时间"建模为数据,而非日历截图。
- **痛点**:Calendly 闭源、数据不在自己手里;自建排期(时区、重叠、改期)极易做错。
- **为何胜出**:API-first + 可自托管,让"排期"变成可编程原语,任何 agent 都能调用。
- **2026 新事实**:社区版已分裂为 [Cal.diy](https://github.com/calcom/cal.diy)——剥离全部企业功能(Teams/SSO/Workflows)、纯 MIT、无需 license key。README 明确警告社区版仅限个人非生产用途。**开源排期 = open-core 商业版 + 纯净社区 fork 并存**。

```
访客 ──选 event-type──▶ Next.js 前端 ──tRPC──▶ Prisma(Postgres)
                          │                      │
                          │                 可用时段计算:接入
                          ▼                 Google/Outlook/Apple Cal
                     Daily.co(视频)          │
                                                 ▼
agent/第三方 ──REST API──▶ booking(创建/改期) ──▶ Webhook 通知双方
```

## 2. vibe-kanban — AI agent 执行编排([repo](https://github.com/BloopAI/vibe-kanban) 28,577★;公司 bloop 2026-04-10 关闭,转社区维护)

- **架构**:"计划层 kanban + 执行层 workspace"双层。每个 issue 开一个 workspace,给 coding agent(Claude Code/Codex/Gemini CLI 等 10+)配 branch+terminal+dev server;人审查 diff、行内评论回喂 agent,满意后发 PR。
- **痛点**:工程师在 AI 时代的核心工作变成"规划+审查",散落在 CLI 里没有统一界面。
- **范式被验证**:2025-06 首发,率先做出多 agent、diff 评论、live preview——这些功能"如今已被视为理所当然"([官方告别信](https://www.vibekanban.com/blog/shutdown))。
- **死因(关键数据)**:"绝大多数是免费用户,找不到让我们兴奋的商业模式";远程功能(issues/评论/项目)将移除,转**全本地架构**。agent 编排是刚需,但**不构成独立商业产品**。

```
人 ──建 card──▶ [Kanban 计划层] ──派发──▶ [Workspace 执行层]
                     ▲                      agent×N: branch+终端+dev server
                     │ 审查 diff/行内评论          │
                     └──────产出回灌───────────────┘
                                    满意 ──▶ PR ──▶ GitHub
```

## 3. Doist/todoist-mcp — 官方 AI 访问层([repo](https://github.com/Doist/todoist-mcp) 562★,今日活跃;同类 [google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) 3,469★,10-30 活跃)

- **架构**:三形态一体——①npm 工具函数库(`findTasksByDate`/`addTasks`)可直嵌 Vercel AI SDK;②`npx` 本地 MCP server;③托管 streamable HTTP `https://ai.todoist.net/mcp` + OAuth,官方 Claude Code 插件一条命令接入。
- **痛点**:此前 agent 读写个人任务系统没有可靠通道,靠逆向 API/脆弱爬取。
- **为何胜出**:**待办厂商亲自把自家产品变成 agent 的工具**。google_workspace_mcp 同理:自然语言直控 Calendar/Tasks/Gmail,OAuth 2.1 + 无状态部署可组织级托管。MCP 已成事实标准。

```
Claude/Cursor/自研 agent
   │ MCP 协议(stdio 或 streamable HTTP+OAuth)
   ▼
 todoist-mcp ──工具调用──▶ Todoist REST API ──▶ 任务数据库
 g-workspace-mcp ──────▶ Google Calendar/Tasks API
   ▲
人 └─ 自然语言:"把明天的深度工作排进上午" ── agent 读日历→写任务→回写日历
```

## 4. Huly — 全能开源 PM 的教训([hcengineering/platform](https://github.com/hcengineering/platform) 28,045★,仓库已冻结;社区接盘 [Platform-Collective/platform](https://github.com/Platform-Collective/platform) 仅 134★)

对标 Jira 的"All-in-One"(Chat/PM/CRM/HRM/ATS),README 已挂"仓库冻结+Hosted Huly 因无资金关闭"。**启示:大而全的开源生产力平台,商业化和社区接续都极难**。另一侧证:[claude-task-master](https://github.com/eyaltoledano/claude-task-master) 28,295★(PRD→任务分解→喂 agent 的 AI 原生范式)自 2026-04 起停滞。

## 5. 综合判断:2026 年怎么组队

1. **数据与计算层:不自造**。日历用 Google/Outlook API(排期场景直接上 cal.com/Cal.diy 的可用时段引擎);任务落 Todoist/Linear 等成熟系统。
2. **访问层:一律 MCP**。官方 MCP 优先(todoist-mcp),没有官方就用社区 MCP(google_workspace_mcp);工具粒度要细(增/查/改/移动日期各自独立工具)。
3. **编排层:LLM agent + 人在回路看板**。借鉴 vibe-kanban 双层结构:agent 自动排期只出"提案",人审查后落库——这正是第一轮 HN 共识(全自动如 Motion 忘勾完成即垃圾排期)的工程解。
4. **别做的事**:不做全家桶(Huly 教训)、不做独立编排商业产品(bloop 教训)、不押注单厂商闭源排期(cal.diy 存在的理由)。

*未核实项:各项目内部模块细节仅来自 README/官方公告,未逐行读源码;vibe-kanban 社区版路线图当时"数周内发布",现状未核实。*
