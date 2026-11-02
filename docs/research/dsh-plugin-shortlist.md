# DSH 实用插件清单（2026-11-03 精选）

> 来源：DSH Plugin Hub（dsh-plugin.org，5882 个插件，全部人工验证）按 Star/实用性精选。
> 安装命令模板：`dsh plugin --profile <profile> add <npm包名>`（本环境 profile 为 `superagent`）。

## 已装（本环境，2026-11-02/03）

| 插件 | 用途 |
|---|---|
| `dsh-image-gen`（1066★，Apache-2.0） | 对话生图/修图/画廊，OpenAI Images + 兼容中转（配 Key 后即用） |
| `@weibaohui/dsh-tasks`（10★，MIT） | cron 定时任务，到点自动开新会话执行（晨报等定时产出） |
| `@a9i5k4/dsh-auto-memory`（179★） | 三层跨会话记忆：每轮自动沉淀、智能检索、日历提醒 |

## 推荐补装（按场景）

### 信息获取（最优先）
| 插件 | Star | 协议 | 一句话 | npm 包 |
|---|---|---|---|---|
| ModSearch | 909 | MIT | 免 Key 联网搜索（网页/X），返回结构化 JSON 证据，无原生联网模型的刚需 | `@liustack/modsearch` |
| ModLens | 4713 | MIT | 纯文本模型外挂视觉：粘贴图片得 OCR/版面/元素定位结构化结果 | `@liustack/modlens` |

### 效率与监控
| 插件 | Star | 协议 | 一句话 | npm 包 |
|---|---|---|---|---|
| dsh-context | 3994 | Apache-2.0 | 上下文透视与管理：看清楚上下文组成/演进/压缩事件 | `dsh-context` |
| dsh-better-sidebar | 4821 | MIT | 右侧栏工作台：文件编辑、终端、Git 变更、子代理任务一栏全览 | `dsh-better-sidebar` |
| dsh-cost-meter | 598 | MIT | 会话/当日费用、预算、余额与 Token 用量热图 | `dsh-cost-meter` |

### 多端与协作
| 插件 | Star | 协议 | 一句话 | npm 包 |
|---|---|---|---|---|
| dsh-im | 3095 | MIT | IM 机器人接入（飞书/微信/钉钉等 9 渠道）；配 dsh-tasks 可把定时任务结果推到微信 | `@xmanrui/dsh-im` |
| dsh-pocket | 2670 | **GPL-2.0** | 手机扫码同步访问电脑上的 DSH，人在外面也能盯任务 | `dsh-pocket` |
| dsh-agent-teams | 2638 | MIT | 会话变队长：组建持久子代理团队、按依赖拆分任务协作 | `@nanmicoder/dsh-agent-teams` |
| deja-vu | 1261 | MIT | 把本机各 coding agent 的历史会话建索引，34 种 agent 跨工具复用 | `dsh-deja` |

### 模型与通道
| 插件 | Star | 协议 | 一句话 | npm 包 |
|---|---|---|---|---|
| dsh-plugin-subscriptions | 547 | MIT | 把 ChatGPT/Claude/Grok 订阅当 LLM Provider（OAuth 免 API Key） | `dsh-plugin-subscriptions` |

### 办公与交付（架构主链路配套，见 ../architecture/media-generation-pipeline.md）
| 插件 | Star | 协议 | 一句话 | npm 包 |
|---|---|---|---|---|
| pptwise | 27 | MIT | 本地生成可编辑 .pptx（阶段3推荐） | `@liustack/pptwise` |
| dsh-office-tools | 41 | MIT | Word/Excel/PPT 创建读取更新、PPT 嵌图（阶段3推荐） | `dsh-office-tools` |
| dsh-univer-office | 654 | Apache-2.0 | GUI 内 Univer 办公工作台（需人工精修时再装，阶段5） | `dsh-univer-office` |

### 有趣可选
| 插件 | Star | 协议 | 一句话 | npm 包 |
|---|---|---|---|---|
| dsh-bili-scroll | 1134 | MIT | 每天替你刷 B 站：按关键词筛出值得看的写成日报 | `dsh-bili-scroll` |
| dsh-meme | 485 | MIT | 表情包：纯文本斗图、情绪主动发图 | `dsh-meme` |

## 备注
- 星数为 dsh-plugin.org 目录 2026-11-03 数据；协议经 GitHub 逐仓核对。
- `dsh-pocket` 为 GPL-2.0，个人使用无碍，二开分发需注意传染性。
- 插件并非越多越好：每个插件会占用上下文（工具 schema）与内存（本机 2GB），按需安装；不用的可在设置里停用。
