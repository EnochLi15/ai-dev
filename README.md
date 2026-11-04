# ai-dev

Development workspace repository for the AI agent.

## 项目架构(这个仓库是什么、怎么运转)

ai-dev 是 DSH(DeepSeek Harness)agent 体系的工作区仓库:用户在微信下达指令,DSH 编排层生成工单并调度 worker 会话,worker 在本仓库的 git worktree 中作业;阶段性成果经质检后直接合入 main,并回推微信。本仓库同时有私有全量镜像 `EnochLi15/ai-dev-private`(2026-11-04 建立,含全部工单分支)。

```
              ┌────────────── 微信(用户) ──────────────┐
              │  日常指令 · 反馈 · 每日晨报推送(07:00)   │
              └────────────────┬───────────────────────┘
                               ▼
        ┌──── DSH 编排层(触发→路由→工单/会话/子代理) ────┐
        │  worker 在 git worktree 中作业;交付回微信/合库  │
        └────────────────┬───────────────────────────────┘
                         ▼
        ┌──────────── ai-dev 仓库(GitHub) ───────────────┐
        │  main(阶段性成果直接合入,所有者 2026-11-02 授权)  │
        │  + agent/* 工单分支  ·  私有镜像 ai-dev-private   │
        └───┬───────────┬──────────────┬─────────────┬───┘
            ▼           ▼              ▼             ▼
      morning-brief/  docs/research/   ontology/     docs/architecture/
      晨报流水线       调研生产线        知识库预研     媒体生成设计
      collect.py      多会话并行深研    企业KB参考架构  图片/PPT生成设计
      8信源→六问筛选   (两轮已验证)     +开源调研      DSH插件清单
      →九节成刊→质检
            │           │              │             │
            └─ 质检(零幻觉/回源核对) → 归档 main → 微信推送 ─┘
```

### 四条内容生产线

| 生产线 | 位置 | 状态 |
|---|---|---|
| AI 晨报 | [morning-brief/](morning-brief/) | ✅ 每日 07:00 定时出刊:`collect.py` 8 信源采集 → 六问筛选 → 九节栏目 v0.2 成稿 → 零幻觉质检(数字/日期/链接回源核对)→ 归档 main → 当日微信推送提醒;GitHub 趋势台账跨期去重 |
| 调研生产线 | [docs/research/](docs/research/) | ✅ 按需触发,多会话并行深研,已验证两轮(工具/实践调研 + 高星开源项目架构分析) |
| 知识库预研 | [ontology/](ontology/) | 📐 企业 Ontology 知识库参考架构 + 开源调研(文档级,未实现) |
| 媒体生成设计 | [docs/architecture/](docs/architecture/) | 📐 图片/材料/PPT 生成端到端架构设计(文档级,未实现) |

## 目录导航

| 目录 | 内容 |
|---|---|
| [docs/architecture/](docs/architecture/) | 🎨 架构设计（显眼位置）：[图片/材料/PPT 生成端到端架构](docs/architecture/media-generation-pipeline.md)（[架构图](docs/architecture/media-generation-pipeline.svg)） |
| [docs/research/](docs/research/) | 🔍 调研记录：[OpenAI 图片生成接口与插件生态调研](docs/research/openai-image-generation.md) · [DSH 实用插件清单](docs/research/dsh-plugin-shortlist.md) · [AI 待办与日历](docs/research/ai-todo-calendar.md) · [AI 笔记实践](docs/research/ai-note-taking.md) · [个人知识库](docs/research/personal-knowledge-base.md) · [架构分析：AI 待办/日历](docs/research/ai-todo-calendar-architecture.md) · [架构分析：AI 笔记](docs/research/ai-note-taking-architecture.md) · [架构分析：知识库](docs/research/personal-knowledge-base-architecture.md) |
| [ontology/](ontology/) | 📐 本体（Ontology）企业知识库预研：架构设计（首选阅读 [ontology/docs/architecture.md](ontology/docs/architecture.md)）+ 开源项目调研 |
| [morning-brief/](morning-brief/) | AI 晨报：制作方案、信源调研与每日存档 |

> 约定：文档与实现分离；阶段性成果由 agent 直接合入 main（所有者 2026-11-02 授权）。
