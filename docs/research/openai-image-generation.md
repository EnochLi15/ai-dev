# 图片/材料/PPT 生成 — 调研全记录（OpenAI Images API · 插件生态 · 实践）

调研时间：2026-11-02 · 调研会话：openai-image-research（与晨报任务分开的新会话）

## 一、结论速览

| 问题 | 结论 |
|---|---|
| 能否对接 OpenAI 图片生成接口？ | **可以**。官方 Images API 现役模型为 GPT Image 系列（用户所说的 "image2" 即 `gpt-image-2`，2026-04 上线；最新为 2026-09-08 发布的 `gpt-image-2.5-flare` / `gpt-image-2.5-sunburst`） |
| 怎么对接？ | REST `POST /v1/images/generations`（Bearer API Key）或官方 SDK（openai-node 7.x / openai-python）；支持流式出图；编辑走 `/v1/images/edits` |
| 有没有现成插件？ | **有，且很多**。DSH 本身有官方插件体系：图像类 `dsh-image-gen`（1066★）等；通用桥接 `@deepseek-ai/dsh-mcp-client` 可接任何 MCP 生图服务器；另有直接用 ChatGPT 订阅（免 API Key）生图的插件 |
| 生成材料/PPT 的好实践？ | PPT：`pptwise`（本地可编辑 PPTX）/ `dsh-office-tools` / `dsh-univer-office`；材料：`dsh-fylar-office-editor`（Markdown→DOCX）、`bruce-md2word`、`gongwen-skill`（公文）；兜底方案 agent 直接调 `pptxgenjs` 生 PPTX（本环境已实测可行） |
| 主要限制 | 本机直连 `api.openai.com` 不通（DNS 污染，实测解析到无关 IP），需走中转/OpenAI 兼容端点或订阅 OAuth 通道 |

## 二、OpenAI 图片生成 API 现状（依据官方 OpenAPI 规范，2026-10-31 更新）

现役模型（`model` 参数）：
- `gpt-image-2.5-flare`（速度优先，日常出图，官方示例默认模型）/ `gpt-image-2.5-sunburst`（精度优先：精细编辑、产品视觉、角色一致性）；快照版 `gpt-image-2.5-*-2026-09-08`
- `gpt-image-2`（快照 `gpt-image-2-2026-04-21`）
- `gpt-image-1.5`、`gpt-image-1-mini`（轻量）、`chatgpt-image-latest`
- 已退役：`gpt-image-1`（2026-10-23 关停）、`dall-e-2/3`（2026-05-12 退役）→ 新接入不要再用 DALL·E

关键能力（来自规范 + 官方资料解读）：
- 端点：`POST /v1/images/generations`（文生图）、`POST /v1/images/edits`（图生图/编辑，支持多参考图、mask，multipart 或 JSON 传图）；返回始终为 base64
- `prompt` 最长 32000 字符；`n` 1–10 张
- `quality`：`low/medium/high/xhigh/max/auto`（xhigh、max 仅 2.5 系列支持）
- `size`：标准 `1024x1024 / 1536x1024 / 1024x1536`；gpt-image-2 起支持**任意分辨率**（宽高为 16 的倍数、宽高比 1:3–3:1、最高 3840×2160；超 2560×1440 为实验性）
- `background: transparent`（透明底，需 png/webp）、`output_format: png/jpeg/webp`、`output_compression`、`moderation: low/auto`
- `stream: true` + `partial_images`（0–3）支持**流式渐进出图**
- 2.5 系列相较 2.0：细节更清晰、编辑更精确、参考主体更稳定、延迟最高降 50%（官方口径，经第三方文章转述）

## 三、怎么对接

### 1) 直接调 API（最简单）
```bash
curl https://api.openai.com/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-image-2.5-flare",
    "prompt": "A cute baby sea otter",
    "n": 1,
    "size": "1024x1024"
  }'
```
官方 SDK：`openai`（Node/TS，v7.47.0，Apache-2.0）、`openai-python`，均有 `client.images.generate(...)` 及流式事件。

### 2) DSH 插件方式（推荐，见第四节）
在 DSH「设置 → 插件市场」安装图像插件，配置 Provider + API Key（或订阅登录）即可在对话里直接生图、改图。

### 3) MCP 方式（通用工具桥接）
DSH 官方插件 `@deepseek-ai/dsh-mcp-client`（BSD-3-Clause）可把任意 MCP 服务器的工具注册为模型原生工具（`mcp__<server>__<tool>`）。配一个生图 MCP 服务器即获得生图工具，例如：
```yaml
- id: mcp-image
  name: '@deepseek-ai/dsh-mcp-client'
  config:
    serverName: image
    transport: stdio
    command: npx
    args: ['-y', '<某个 OpenAI 图片 MCP 服务器>']
    env:
      OPENAI_API_KEY: !!js process.env.OPENAI_API_KEY
```
现成生图 MCP 服务器：`shinpr/mcp-image`（188★，支持 OpenAI GPT Image + Gemini + Seedream）、`lownamlee/gpt-image-2-mcp`（94★）、`Cripacx/mediagen`（51★，Claude Code/编码代理用生图 CLI+MCP）。管理界面可加 `dsh-mcp-manager-plus`。

### ⚠️ 网络前提（实测）
本环境直连 `api.openai.com` 不通：DNS 被污染（解析到 199.59.148.15 等无关 IP），TCP 连接失败。可行路径：
- 使用 OpenAI 兼容**中转端点**（`dsh-image-gen` 等插件原生支持「OpenAI Compatible（中转站）」Provider，可自定义 Base URL）；
- 或用 ChatGPT 订阅 OAuth 登录的插件通道（免 API Key，见下）；
- 或自备代理。国内已有大量中转/聚合服务（如 apimodels 等聚合站同时提供 GPT Image 2/2.5）。

计费按用量（token/张，随质量档位不同），官方定价页 openai.com/api/pricing 本机不可直接访问，接入前请以官方页为准。

## 四、现有插件（重点：DSH 官方插件市场 dsh-plugin.org，5882 个插件，全部人工验证）

### 图片生成
| 插件 | Star | 协议 | 说明 |
|---|---|---|---|
| `shanliuling/dsh-image-gen`（npm: dsh-image-gen） | 1066 | Apache-2.0 | 对话生图/连续修图、AI 画布、Studio 批量、多模型对比、画廊；Provider 支持 **OpenAI Images**、OpenAI Compatible 中转、Gemini、Seedream、Grok、GLM-Image、本地 ComfyUI；支持 ChatGPT/Grok/Google **订阅登录免 Key**；有「测试连接」「拉取模型」 |
| `wsl043/dsh-codex-subscription` | 340 | MIT | 直接用 ChatGPT/Codex 订阅（无需 API Key）做模型、搜索与图像生成 |
| `franksong2702/dsh-codex-connect` | 177 | Apache-2.0 | ChatGPT OAuth 接入 OpenAI 模型与图像生成 |
| `dickpy/dsh-imagegen` | 165 | Apache-2.0 | OpenAI 兼容接口文生图/图生图工作台、跨设备画廊 |
| `perrylink/dsh-draw` | 11 | Apache-2.0 | 单一 `image_generate` 工具统一调度 OpenAI Images、智谱 CogView 等，健康回退 |
| 其他 | — | — | `goodandready/dsh-image-gen`（FAL/Replicate/ComfyUI 8 后端+抠图放大矢量化）、`welsione/dsh-mmx-multimodal`（MiniMax 全家桶）、`mokuyoaxis/dsh-iris`、`huanlinoto/dsh-plugin-aigc-canvas`（节点画布） |

### PPT / 材料（文档）
| 插件 | Star | 协议 | 说明 |
|---|---|---|---|
| `dream-num/dsh-univer-office` | 654 | Apache-2.0 | Univer 办公环境：表格/文档/演示/多维表格，可导出标准 Office 文件 |
| `fylaropen/dsh-fylar-office-editor` | 263 | ⚠️ 未附协议 | Office 预览编辑 + 把 Agent 的 Markdown 回复直接生成 DOCX |
| `op7418/dsh-guizang-design` | 240 | ⚠️ AGPL-3.0 | 网页 PPT、图文卡片、排版设计 skill + 设计系统（歸藏设计） |
| `kw78/dsh-office-tools` | 41 | MIT | Word/Excel/PowerPoint 创建读取更新，支持 PPT 嵌图 |
| `omdsh-dev/dsh-office` | 30 | Apache-2.0 | Excel/PDF/PPT/Word 生成编辑 + 公式重算 |
| `liustack/pptwise` | 27 | MIT | 按内容本地生成**可编辑 PPTX**，无需注册/API Key |
| `linhut/gongwen-skill` | 98 | MIT | GB/T 9704 公文全流程（格式检查、模板、Markdown 转公文） |
| `bruc3van/bruce-md2word` | 5 | MIT | Markdown→Word：中文排版、Mermaid 转图、LaTeX 公式 |
| `huanlinoto/dsh-plugin-mineru` | 51 | ⚠️ 未附协议 | MinerU 文档解析（PDF/图/DOCX/PPTX→Markdown，反向输入用） |

平台外开源参考：`presenton/presenton`（11.6k★，开源 AI 演示生成器，Gamma 替代）、`allweonedev/presentation-ai`（3.1k★）、`Akxan/ppt-agent-skill`、`code-on-sunday/slide-deck-generator`（编码代理生成本地 React 幻灯片）。

## 五、实践建议（图片 / 材料 / PPT）

### 生图工作流（官方指南 + 社区实践共识）
1. **探索阶段**：`gpt-image-2.5-flare` + `low/medium`，快速排除错误方向（横竖版、风格、构图一次只验证一个关键问题）
2. **约束锁定**：编辑指令写成「只改 X，保持 Y 不变」，每轮只改一类问题（背景/颜色/文案/构图分开迭代）
3. **终稿**：`gpt-image-2.5-sunburst` + `high/xhigh/max` 精修；透明底选 png/webp
4. 提示词六字段：用途 / 主体 / 场景动作 / 视觉语言 / 构图 / 约束；参考图「少而职责清晰」
5. 分辨率最后再拉高：高分辨率不修复构图与语义错误，先做对再放大

### PPT
- 要**可编辑的 .pptx**：`pptwise` 或 `dsh-office-tools`（原生 PPT 工具链）；兜底 `pptxgenjs`（本环境已实测：node + pptxgenjs 3.x 生成 44KB 合法 PPTX ✔）
- 要**视觉表现力**：`dsh-guizang-design` 的网页 PPT skill（AGPL 注意）或 HTML 幻灯片路线（slidev/marp 类）
- 平台化方案：`dsh-univer-office`（对话内建 Office 环境）

### 材料（文档）
- 日常汇报/材料：Markdown 交付 + `dsh-fylar-office-editor` 或 `bruce-md2word` 转 DOCX（中文排版友好）
- 公文：`gongwen-skill`（国标格式）
- 复用素材库：`dsh-plugin-mineru` 把已有 PDF/PPT/Word 解析成 Markdown 喂回模型

### 推荐组合（最小成本起步）
1. 装 `dsh-image-gen`：有 ChatGPT 订阅就直接 OAuth 登录生图；有中转就配 OpenAI Compatible Provider
2. 装 `pptwise` + `dsh-office-tools`（或 `dsh-univer-office`）覆盖 PPT/材料
3. 需要接入自有系统时再用 `dsh-mcp-client` + MCP 服务器走标准协议

## 六、开源与协议（2026-11-02 追问的完整答案）

| 项目 | 开源 | 协议 | 可否直接用 |
|---|---|---|---|
| DSH 本体（`@deepseek-ai/dsh` CLI） | ✅ github.com/deepseek-ai/deepseek-harness（269k★，公开） | MIT | npm 公开可装 |
| 官方插件包（`dsh-base`/`dsh-mcp-client`/`dsh-web-app`/`dsh-headless`） | ✅ 同一仓库 | BSD-3-Clause | npm 公开可装 |
| DSH Plugin Hub（社区插件市场） | ✅ dshplugin/dsh-plugin-hub（424★） | MIT | 免费 |
| dsh-image-gen / dsh-imagegen / dsh-draw / dsh-office / dsh-univer-office / dsh-codex-connect | ✅ | Apache-2.0 | 免费，生图需自配 Key/中转/订阅 |
| pptwise / dsh-office-tools / dsh-mcp-manager-plus / dsh-codex-subscription / gongwen-skill / bruce-md2word | ✅ | MIT | 免费 |
| dsh-guizang-design | ✅ | **AGPL-3.0**（商用/托管需注意传染性义务） | 免费但注意义务 |
| dsh-fylar-office-editor / dsh-plugin-mineru | 仓库公开 | **未附 LICENSE 文件**（默认保留所有权利） | 可装，商用前建议向作者确认 |
| OpenAI 官方 SDK（openai-node/python） | ✅ | Apache-2.0 / MIT | 免费（API 用量另计） |

## 七、2026-11-02 晚间追加（第二次续作）

### 1) 定时功能：本体无内置，但有现成插件（回答追问）
DSH 本体走「Everything is a Plugin」路线，无内置定时器；插件市场里有多个定时插件：
- `goodandready/dsh-cron`（13★）：原生定时任务与后台自动化，cron 表达式/间隔语法调度 shell、Node、Python、HTTP、SSH、Docker 及 **Agent 任务**
- `weibaohui/dsh-tasks`（10★）：cron 到点自动新建 agent 会话并提交提示词，带全屏管理界面与执行记录
- `cofy-x/dsh-cron`（6★）：持久化定时任务（cron/一次性时间点→幂等新会话），支持时区、补跑、任务中心
- `wujiaojue/dsh-later`（5★）：会话内 /schedule、/later 定时提醒，服务端准时送达
- `alpacachen/dsh-automation`（4★）：一句话调度一次性/周期 Agent 任务（RRULE）
- 晨报同类参考：`shangjian2023/dsh-rss-daily`（RSS→日报→webhook 投递微信/TG）、`bozhang1214/dsh-ai-brief`、`johnxu22786/rss-digest`
- 相关：`cloader/dsh-taskboard`（78★，任务看板+定时执行）、`kanadego/dsh-heartbeat`（28★，定时唤醒维护记忆）
具体「明早晚报是否触发」取决于晨报任务的配置状态，已在晨报会话核实。

### 2) dsh-image-gen 已安装（2026-11-02 23:30）
- 命令：`dsh plugin --profile superagent add dsh-image-gen@latest`（装的是 npm `dsh-image-gen@0.10.2`，package.json 记 ^0.10.0）
- 已写入 profile：bundles 追加 `dsh-image-gen`，依赖装好，**HMR 已热加载生效**（本会话运行时已出现 generate_image / edit_image 工具与图库/Studio 面板），无需重启
- 当前 Provider 默认 google（gemini-3.1-flash-image）；用户明日自行在「插件 → dsh-image-gen → 图像生成」配置 OpenAI Provider（OpenAI Images 或 OpenAI Compatible 中转）+ API Key，可点「测试连接」「拉取模型」
- 协议 Apache-2.0，免费

### 3) 端到端「模板生图→图片转PPT」业界方案（围绕 gpt-image-2）
三种主流路线：

**路线 A：图像模型整页视觉稿 → 打包 PPTX（用户描述的模式，最贴合）**
- `Anionex/banana-slides`（15.9k★，AGPL-3.0，活跃）：图像模型原生 AI PPT 应用；上传任意模板图片+素材智能解析，一句话/大纲自动成套，口头改指定区域，导出可编辑 PPT/视频；Docker 本地部署。基于 nano-banana / gpt-image
- `ningzimu/codex-ppt-skill`（7.6k★，MIT）：SKILL.md 格式 agent skill（Codex/Claude Code/OpenClaw 等）：大纲+视觉风格规划 → 逐页生成图片（gpt-image-2.5-flare 或任意 OpenAI 兼容生图端点）→ 本地脚本组装 .pptx
- `JuneYaooo/gpt-image2-ppt-skills`（1.4k★，Apache-2.0）：专为 OpenAI gpt-image-2 设计；一句话→16:9 高清整页图+打包 pptx；**可仿任意 .pptx 模板**出新内容；默认关的「可编辑模式」把视觉稿重建为 PowerPoint 原生文本/图形/图片层
- 典型流水线：参考模板/风格 → 每页提示词（版式+配色+文案区约束）→ gpt-image 出图（flare 探索、sunburst 终稿）→ python-pptx/脚本按 16:9 整页铺图组装 → 需要可编辑时用重建层

**路线 B：原生可编辑 PPTX（模板+代码生成）**
- `anthropics/skills`（186k★）：官方 Agent Skills 仓库，pptx/docx/xlsx 文档技能（OOXML 直接操作）
- `genspark-ai/genoffice`（11.6k★）：AI Office 套件 + CLI + agent skill，本地生成/编辑真实 docx/xlsx/pptx
- DSH 平台内：`pptwise`（本地可编辑 PPTX）、`dsh-office-tools`、`addsumtech/slides_maker`（648★，论文/代码/文档→可编辑 PPTX，模板库+交付前 critic 审查）

**路线 C：HTML 中间态**
- `chuspeeism/dashi-ppt-skill`（10.3k★）：浏览器可编辑演示，导出 HTML/PDF/PPTX
- `Hasasasa/html-to-editable-pptx`（94★）：HTML 幻灯片→真可编辑 PPTX（原生文本框而非截图），Claude Code/Cursor/Codex skill + Python CLI
- DSH 平台内：`dsh-guizang-design`（AGPL）网页 PPT skill
- 佐证：本环境已实测 node + pptxgenjs 生成合法 PPTX（44KB）

**推荐组合**：在 DSH 内用已装的 dsh-image-gen（明天配好 OpenAI Provider）出整页视觉稿，再装 pptwise 或 dsh-office-tools 组装/精修可编辑 PPTX；要开箱即用的独立应用选 banana-slides（注意 AGPL），要 skill 形态直接抄 gpt-image2-ppt-skills / codex-ppt-skill 的工作流（MIT/Apache，可商用）。

### 4) 定时插件已安装（2026-11-02 23:36，第三次续作，用户委托「直接帮我装」）
- 选择 **@weibaohui/dsh-tasks v0.5.11**（MIT，10★，2026-10-31 更新）：cron 到点自动新建 agent 会话并提交提示词——与晨报场景完全对口；带可视化 cron 选择器（预览最近 5 次执行）、全屏管理页（设置 → 定时任务）、每任务保留最近 20 次执行记录、可「立即运行」、可绑定工作区/指定模型；可选通知推送（开始/完成/失败推送 IM，需另配 dsh-im 投递插件，支持免打扰时段）
- 安装命令：`dsh plugin --profile superagent add @weibaohui/dsh-tasks -w`；插件管理器自动带上官方依赖 `@deepseek-ai/dsh-experimental-schedule-bundle@0.2.0-rc.1`（Schedule 任务页与时间上下文的官方可选 bundle）
- 兼容性核对：要求 DSH ≥0.1.7-rc.2（本机 0.2.1-rc.3 ✓）、Node ≥22.5（本机 24.22.2 ✓）；peer 警告（cordis/dsh-agent 等）为 DSH 插件常规形态，宿主运行时提供
- 未选中备选：goodandready/dsh-cron（13★，偏运维：shell/HTTP/SSH/Docker 六种运行时+多渠道推送）、cofy-x/dsh-cron（6★，持久化幂等但要另装 dsh-automation 两件套，且标称 0.1.x 线兼容）
- 使用：设置 → 定时任务 → 新建（标题+提示词+cron，如每天 8:00 `0 8 * * *`）→ 启用；执行出的会话在侧栏工作区下可回看。晨报的具体定时任务由晨报会话/用户配置

### 追加信息来源
- dsh-image-gen README 安装/升级章节；`dsh plugin` 实际执行输出（2026-11-02）
- GitHub 仓库元数据与 README（banana-slides / codex-ppt-skill / gpt-image2-ppt-skills / anthropics/skills / genoffice / dashi-ppt-skill / html-to-editable-pptx / slides_maker，均 gh api 核对 star 与协议）
- DSH Plugin Hub 目录本地检索（定时/晨报类）
- OpenAI 官方 OpenAPI 规范（github.com/openai/openai-openapi，2026-10-31 推送）：模型清单、参数、退役说明、官方 curl 示例
- npm 包元数据：`@deepseek-ai/dsh`、`@deepseek-ai/dsh-mcp-client`（含配置 README）、`dsh-plugin`、`openai`
- DSH Plugin Hub 目录（api.dsh-plugin.org/plugins.zh.json，5882 条，2026-11-02 拉取）+ 各插件 GitHub 仓库 License 字段（gh api 逐仓核对）
- `shanliuling/dsh-image-gen` README（Provider 支持矩阵）
- 博客园《GPT Image 2.5 上手指南：Sunburst 与 Flare 怎么选》（2026-09-20，含官方资料转述与工作流实践）
- Bing 检索（百度百科 GPT-Image-2.5 Flare 词条、apimodels 聚合站模型目录等，作旁证）
- 本环境实测：api.openai.com 连通性（DNS 污染诊断）、pptxgenjs 本地生成 PPTX 验证
