# 本体（Ontology）企业知识库预研

> 版本：v1（2026-11-02 起草，信源数据均经 GitHub API 当日核实）
> 目录约定：**文档与实现分开** —— `docs/` 放调研与设计文档，后续 PoC 代码放 `poc/`（所有者 2026-11-02 要求）。
> 归档约定：阶段性成果**直接合入 main**（仓库所有者 2026-11-02 授权：无需等待人工合并）。

## 📐 首选阅读：架构设计

→ **[docs/architecture.md](docs/architecture.md)** —— 选型结论（一个主平台还是全用）、架构图、每个组件的职责与衔接、解决的问题、落地节奏。

## 目录

| 文件 | 内容 |
|---|---|
| [docs/architecture.md](docs/architecture.md) | 参考架构设计：Semantica 主平台 + LinkML/open-ontologies 增强，Mermaid 架构图，三阶段落地 |
| [docs/open-source-survey.md](docs/open-source-survey.md) | 开源项目全景调研：一体化平台 / 本体工程 / LLM 建图 / 本体学习 / W3C 标准栈，含 star、许可证、活跃度与风险提示 |

## 一句话结论

**只用一个主平台（Semantica）起步，不拼全家桶**：1-2 周 PoC 验证"AI Agent 起草本体 + 语义层 + 带溯源问答"，1-2 个月引入 LinkML 本体即代码，本体进生产后再加 open-ontologies 变更治理。
