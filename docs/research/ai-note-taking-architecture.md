> 第二轮架构分析 · 2026-11-03 · 由三个并行研究子会话各自深挖高星开源项目（README/docs 直读+gh api 星数与活跃度核实），回答"当前最优技术方案"；未核实项随文标注。

# AI 笔记的最优技术方案：从高星开源项目反推（2026-11）

调研方法：gh api 确认星数/最近 commit → 淘汰死项目 → 直读 README/architecture 文档提取范式。数据日期 2026-11-03。

## 0. 选样：活跃度筛查

| 项目 | 星数 | 最近 push | 状态 |
|---|---|---|---|
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | 78,139★ | 2026-11-02 | 极活跃 |
| [AFFiNE](https://github.com/toeverything/AFFiNE) | 74,155★ | 2026-11-02 | 极活跃 |
| [usememos/memos](https://github.com/usememos/memos) | 64,247★ | 2026-11-02 | 极活跃（self-hosted 时间线速记） |
| [Joplin](https://github.com/laurent22/joplin) | 57,007★ | 2026-11-03 | 活跃 |
| [思源 SiYuan](https://github.com/siyuan-note/siyuan) | 47,053★ | 2026-11-03 | 极活跃 |
| [Logseq](https://github.com/logseq/logseq) | 45,464★ | 2026-11-03 | 活跃（DB 版 beta） |
| [Reor](https://github.com/reorproject/reor) | 8,535★ | **2025-05-13 停滞** | 反例 |
| TriliumNext | 2,922★ | 2025-06-24 | 半死，弃选；Anytype 仓库 404 未核实 |

深挖四个：思源（块级数据库范式）、AppFlowy（CRDT 协作范式）、Logseq（文件→DB 演进）、Reor（AI-native 内嵌范式，反例）。

## 1. 思源 SiYuan——块级数据库 + 数据仓库快照同步

**范式**：所有内容为"块"，落盘 `.sy.json` + SQLite 块索引，支持块级引用/双链/嵌入；slogan 已改为 "From thought to insight, **with agents**"，README 明确定位"人与 AI 智能体协作的自托管知识工作空间"。生态拆分：lute（编辑引擎）/ dejavu（数据仓库）/ riff（间隔重复）/ petal（插件）。
**解决的痛点**：Markdown 无块级语义、检索靠全文；代价是格式绑定——官方 FAQ 明言"不支持第三方同步盘，否则数据可能损坏"，同步只能走 dejavu 快照仓库（官方云或 Docker 自建 S3/WebDAV）。

```
[编辑器 UI · Electron/移动端/鸿蒙]
        │ kernel HTTP API
[内核 Kernel (Go)]
   ├─ lute 编辑引擎(Markdown ⇄ 块 AST)
   ├─ SQLite 内容块索引(双链/引用/块查询)
   └─ riff 间隔重复
落盘: workspace/*.sy.json + SQLite
        │ dejavu 数据仓库(快照+端到端加密)
   ├─ 官方云 / 自建 S3/WebDAV(Docker)
   └─ ✗ 第三方同步盘 = 数据损坏
AI 层: 外接 OpenAI 兼容 API(自备 key) + agent 协作接口
```

## 2. AppFlowy——Flutter+Rust+CRDT，开源 Notion 的工程答案

**范式**：README "Built With: Flutter + Rust"。客户端 Flutter，核心逻辑 Rust（flutter_rust-bridge FFI），协作文档模型基于 Yrs（Rust 版 Yjs CRDT，代码库内 4 处 yrs 引用，未逐行核实依赖版本），本地 SQLite 离线优先，服务端 AppFlowy Cloud 可完整自托管。AI 是产品一等公民（ask AI、移动端 AI 摘要）。
**解决的痛点**：Notion 的"数据在别人云上 + 移动端弱"；CRDT 让离线编辑与实时协作共存，无手动冲突合并。

```
[Flutter 客户端 桌面/移动/Web]
        │ FFI
[Rust 核心 flowy-core]
   ├─ collab 文档模型 (Yrs/Yjs CRDT)
   ├─ 本地 SQLite(离线优先)
   └─ AI 模块(本地/云模型可切)
        │ WebSocket
[AppFlowy Cloud (Rust, 自托管) + Postgres]
   ⇄ 多端 CRDT 自动合并(无需锁/冲突解决)
```

## 3. Logseq——文件范式军团向数据库投降的样本

**范式**：大纲/outliner + 双链。旧版纯 Markdown/Org 文件本地目录（git 友好，同步靠网盘/iCloud，文件级冲突）；2026-07 发布 2.0 Beta（DB 版）：图数据进 SQLite，新增 RTC 实时协作（alpha）+ 新移动端。README 官方警告：beta"**可能丢数据**"，要求自动备份——工程上承认文件式做不了实时协作与移动体验。
**痛点**：文件格式无法支撑块级协作/移动离线；DB 版是自救，但两年重构窗口给了竞品机会（星数已被思源反超）。

```
旧版: [大纲编辑器] ─ [Markdown/Org 文件] ─ 本地目录 → 网盘/git(文件级, 易冲突)
DB版(beta): [大纲编辑器] ─ [SQLite DB graph] ─ RTC 实时协作(alpha) + 新移动端
                    ⚠ 官方标注: beta 可能丢数据, 须自动备份
```

## 4. Reor——AI-native 内嵌范式的先行者与墓碑

**范式**（README 原文，架构最清晰）：单目录 Markdown vault，每条笔记自动 chunk → Transformers.js 本地 embedding → LanceDB 本地向量库；语义搜索、相关笔记按向量相似度自动连接、RAG 问答喂 Ollama 本地 LLM（也支持 OpenAI 兼容 API）。金句："a RAG app with **two generators: the LLM and the human**"——人写笔记时侧边栏就是"检索生成器"。
**反例价值**：把模型栈整体绑进产品（Ollama+Transformers.js+LanceDB），模型迭代跟不上，2025-05 起零 commit。**范式赢了，产品死了**——同款架构被 Obsidian 插件（Copilot/Smart Connections 外挂式）继承并存活。

```
[Markdown 编辑器(单目录 vault)]
        │ 保存即自动 chunk
[Transformers.js 本地 embedding] → [LanceDB 本地向量库]
   ├─ 语义搜索(查询→向量→top-k)
   ├─ 相关笔记自动连接(相似度) → 侧边栏
   └─ RAG 问答: 检索上下文 → [Ollama 本地 LLM / OpenAI 兼容 API]
✗ 2025-05 起停滞: 内嵌全栈 = 跟不动模型节奏
```

## 5. 综合判断：2026 年 AI 笔记的最优技术组队

1. **数据层**：本地优先是共识（AppFlowy/AFFiNE/思源/Logseq 全部本地优先，AFFiNE README 原话 "data on your disk, in spite of the cloud"）。个人知识库选**纯 Markdown 文件为真相源**（AI 可直接读、git 可版本化、永不锁定）；团队协作才值得上**块级 DB + CRDT**（换实时协作，代价是格式绑定）。
2. **同步层**：CRDT（Yjs/Yrs 系）已是工程标准答案——AppFlowy、AFFiNE、Logseq RTC 三家独立收敛到它；单人用 git 或快照仓库（dejavu 式）即可，且不要在块级 DB 上叠网盘（思源官方警告）。
3. **AI 层**：**外挂可换压倒内嵌绑定**（Reor 之死 vs Obsidian 插件之活是自然实验）。最优组合：检索层本地化（本地 embedding + 本地向量库，隐私+离线），生成层可插拔（OpenAI 兼容 API，云/本地随时换），接口层走 MCP/agent 协议（思源 slogan "with agents" 代表的方向：笔记库成为 agent 可读写的记忆体）。
4. **一句话**：本地 Markdown vault + git/CRDT 同步 + 本地 RAG 检索 + 可插拔云端生成 + MCP agent 接口——这就是 2026 年开源社区用星数和代码投票出来的答案。

**未核实标注**：AppFlowy 的 yrs 依赖版本未逐行核对；思源 SiYuan_Arch.svg 架构图为图片未能直读，组件关系依 README 生态表推断；Anytype（gh 404）未纳入；AFFiNE/memos/Joplin 仅作背景星数，未深挖。
