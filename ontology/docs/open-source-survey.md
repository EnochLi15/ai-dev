# 本体（Ontology）开源项目调研：企业/行业/项目知识库 + AI Agent 构建本体

调研日期：2026-11-02。数据来源：GitHub API（star 数、许可证、最近推送均为当日核实值）。
需求画像：为公司产品构建行业知识库 / 企业知识库 / 项目知识库；希望用 AI Agent 协助构建整个本体，作为语义层 + 知识库。

## 一、结论（TL;DR）

- **最贴合"Agent 帮我建本体 → 语义层 + 知识库"一体化**：[Helix Foundry](https://github.com/HelixDB/helix-foundry)（连数据源，让 Claude Code/Codex 等 Agent 起草本体并装载进图数据库，带血缘溯源）和 [Semantica](https://github.com/semantica-agi/semantica)（本体管理 + 上下文图 + RDF/LPG 双栈，MIT，社区最大）。
- **给 Data Agent 做语义层（MCP）**：[EvoOntology](https://github.com/ruc-datalab/EvoOntology)（人大出品，自动构建 + 持续进化本体层，Claude Code/Codex 插件即插即用，中文文档齐全）。
- **重治理、可审计的企业级底座**：[Utopia](https://github.com/deeplethe/utopia)（双时序知识图谱 + 本体内置，离线部署，有中文文档）、[TrustGraph](https://github.com/trustgraph-ai/trustgraph)（本体接地上下文图 + 策略运行时）。
- **本体变更治理**：[open-ontologies](https://github.com/fabio-rovai/open-ontologies)（类 Terraform：plan/apply/rollback 本体变更 + 影响面报告，Rust 单二进制）。
- **中文企业知识平台开箱即用**：[qKnow](https://github.com/qiantongtech/qKnow)（知识图谱+RAG+Bot，Spring Boot/Vue）；[Jonex](https://github.com/yuezhiai/jonex)（多模态解析 + 本体知识引擎）。
- **已有海量文档、想快速起步**：[GraphRAG](https://github.com/microsoft/graphrag) / [LightRAG](https://github.com/HKUDS/LightRAG) / [Neo4j LLM Graph Builder](https://github.com/neo4j-labs/llm-graph-builder)，先出图再收敛 schema 为本体。

## 二、分项详评

### A. 一体化平台（本体 + 知识库 + Agent 构建）

| 项目 | Star | 许可证 | 技术栈 | 最近推送 | 一句话定位 |
|---|---|---|---|---|---|
| [HelixDB/helix-foundry](https://github.com/HelixDB/helix-foundry) | 1,990 | Apache-2.0 | Go + Docker | 2026-11-02 | 连接公司数据库/工具/文档，让 Agent 起草本体并载入 HelixDB 图数据库；每个值可回溯到原始行/原文；支持云端或一条命令本地部署 |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | 14,396 | MIT | Python | 2026-11-02 | 图原生知识基础设施：企业数据摄取 → 上下文图/知识图谱 → 图分析 + 因果推理，内置 Ontology Hub 管理，RDF + LPG 双支持、W3C 标准兼容、决策全程可追溯 |
| [deeplethe/utopia](https://github.com/deeplethe/utopia) | 8,668 | Apache-2.0 | Rust | 2026-11-02 | 开源"企业世界模型"：双时态知识图谱（事实何时为真 vs 何时得知）、本体在基础层、被动学习 + 自治理、冲突检测/推理/决策均基于本体；离线部署；Agent 经 MCP 读写（写入需人工审核）。官方不希望被称作"开源版 Palantir" |
| [trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph) | 2,870 | Apache-2.0 | Python | 2026-10-28 | 面向 Agent 治理：把企业知识、系统、业务逻辑统一为本体接地的上下文图 + 策略运行时，约束 Agent 权限/范围/风险；单一平台内置 3 种 RAG；支持自选或行业标准本体 |
| [yuezhiai/jonex](https://github.com/yuezhiai/jonex) | 1,557 | 自定义（NOASSERTION，需审读） | Python+React | 2026-10-28 | 多模态解析引擎 + 本体驱动 LLM Wiki 的 AI-Ready 知识引擎：摄取、解析、领域知识编译、向量+图索引、溯源检索、反馈闭环一体；多租户 |
| [qiantongtech/qKnow](https://github.com/qiantongtech/qKnow) | 289 | Apache-2.0（GitHub 标记 NOASSERTION，含专业版，需审读） | Java(SB3)/Vue3 | 2026-10-16 | 中文企业知识智能化 Agent 平台：知识图谱、知识库 RAG、Bot 构建、行业 AI 应用标准化模块；文档/结构化数据/专家经验统一沉淀；有开源版演示站 |
| [u485349-coder/OpenFoundry](https://github.com/u485349-coder/OpenFoundry) | 154 | 需核实 | 早期 | 2026-04-23 | 开源 Palantir Foundry 替代（ontology-first 数据-运营平台），方向对口但活跃度低，仅建议关注 |

### B. 本体工程 / 语义层（Agent 友好）

| 项目 | Star | 许可证 | 定位 |
|---|---|---|---|
| [ruc-datalab/EvoOntology](https://github.com/ruc-datalab/EvoOntology) | 1,117 | MIT | 中国人民大学。首个面向 Data Agent 的自进化本体层：MCP 工具暴露版本化本体层，从数据自动构建、从执行轨迹持续进化；Claude Code/Codex 插件即插即用；解决表/文件/库异构的语义鸿沟 |
| [fabio-rovai/open-ontologies](https://github.com/fabio-rovai/open-ontologies) | 2,759 | MIT | 生产本体变更管理（Rust 单二进制）：像 Terraform 一样 plan/apply/rollback 本体变更，附爆炸半径报告与可校验证明；有中文 README 和浏览器试玩 |

### C. LLM 抽取建图（弱本体路线，适合起步）

| 项目 | Star | 许可证 | 定位 |
|---|---|---|---|
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | 36,529 | MIT | 微软图 RAG 标杆：从非结构化文本抽取实体/关系建图，社区分层摘要，全局问答强 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | 40,485 | MIT | 轻量图 RAG（EMNLP 2025）：双层检索，简单快速，易集成 |
| [neo4j-labs/llm-graph-builder](https://github.com/neo4j-labs/llm-graph-builder) | 5,295 | Apache-2.0 | Neo4j 官方：LLM 从非结构化数据建图，可自定义 schema（近似本体），有 UI。注意依赖 Neo4j（社区版功能受限） |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 140,909 | Apache-2.0（CLI） | 把代码库/文档建成可查询知识图谱，面向 coding agent 省 token；偏代码场景而非企业知识库，供参考 |

### D. 本体学习（研究向，可作算法组件）

- [monarch-initiative/ontogpt](https://github.com/monarch-initiative/ontogpt)（1,082★，BSD-3）：LLM 本体抽取（SPIRES 等），生物医学见长。
- [HamedBabaei/LLMs4OL](https://github.com/HamedBabaei/LLMs4OL)（193★）、[sciknoworg/OntoLearner](https://github.com/sciknoworg/OntoLearner)（126★）、[andylolu2/ollm](https://github.com/andylolu2/ollm)（64★，NeurIPS 2024）：LLM 本体学习框架/库，适合自研抽取管线时引用。

### E. W3C 标准栈（自建可控路线）

- 建模：[Protégé](https://github.com/protegeproject/protege)（1,623★，经典 OWL 编辑器）、[LinkML](https://github.com/linkml/linkml)（679★，Apache-2.0，YAML 建模一次生成 OWL/JSON-Schema/SQL/GraphQL 等，工程化体验好）、[microsoft/Ontology-Playground](https://github.com/microsoft/Ontology-Playground)（2,996★，MIT，零后端可视化本体设计器，适合画原型）。
- Python 库：[rdflib](https://github.com/RDFLib/rdflib)（2,545★）、[Owlready2](https://github.com/pwin/owlready2)（218★，OWL 面向对象操作 + 推理机挂接）、[kglab](https://github.com/DerwenAI/kglab)（695★，KG 构建抽象层）、[RDFLib/OWL-RL](https://github.com/RDFLib/OWL-RL)（181★，OWL2 RL 推理）。
- 存储/推理：Apache Jena Fuseki、Oxigraph、GraphDB Free、Virtuoso（均成熟，选型看运维偏好）。

## 三、选型建议（按场景）

1. **想最快验证"Agent 建本体 + 知识库"闭环** → Helix Foundry：Docker 一条命令起，用现成 coding agent 起草本体，血缘溯源开箱即用。
2. **要长期演进的标准底座、避免锁定** → Semantica（RDF+LPG 双栈、W3C 兼容、MIT）+ open-ontologies 做变更治理；也可 LinkML 建模生成多格式。
3. **主要给 Data/SQL Agent 当语义层** → EvoOntology（MCP 插件直接挂 Claude Code/Codex）。
4. **合规/审计要求高（合同、人事、金融）** → Utopia（双时序 + 证据链 + 离线部署）或 TrustGraph（策略运行时治理 Agent 行为）。
5. **中文团队、要开箱即用企业知识问答** → qKnow（中文文档、演示站）；Jonex 需先审其自定义许可证。
6. **文档量大、先要效果后要规范** → LightRAG/GraphRAG/llm-graph-builder 起步，运行 2-3 个月后再把涌现的 schema 人工收敛为本体，迁移到 A/B 类平台。

## 四、风险与注意

- **许可证**：Jonex、qKnow 均含商业版/自定义条款，商用前务必读 LICENSE 与开源版/专业版边界；Graphify 核心开源但主推云服务。
- **依赖绑定**：llm-graph-builder 绑定 Neo4j（社区版功能受限）；Helix Foundry 绑定 HelixDB。
- **成熟度**：OpenFoundry 活跃度低（最近推送 2026-04）；EvoOntology 为学术团队维护（论文 arXiv:2609.15779），生产采用需评估。
- **本体质量**：LLM 自动起草的本体必须有人工评审环节（Utopia 的"写入提案-人工审核"模式、open-ontologies 的 plan/apply 审批流都是为此设计），直接全自动会累积语义错误。
