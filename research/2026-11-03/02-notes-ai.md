# 2026-11「大家用 AI 怎么记笔记」调研报告（子会话 2/3 原始产出）

## TL;DR
1. 格局三分：大而全（Notion）稳、本地 markdown（Obsidian）因 agent 直接读写文件而意外翻红、第一代 AI-native 笔记应用（Reor 已归档、Khoj/Saner 转型）大面积退潮——"AI-native 独立应用"这条路线 2026 年基本被证伪。
2. 工程师主流玩法是「纯 markdown 库 + AI 编码 agent 直读直写」：Obsidian Copilot 插件干脆转型为"在 Obsidian 里跑 OpenCode/Codex/Claude Code"，笔记库变成人和 agent 的共享记忆。
3. AI 的真价值集中在两步：捕获（语音/会议自动转写，Granola 模式）和检索/联动（agent 按需读库），中间的"AI 自动整理/自动链接"被社区普遍认为是噱头。

## 工具格局（2026-11）
- **大而全**：Notion 官方方向是让 agent 把 Notion 当共享记忆（官方博客《Building Shared Memory for AI Agents in Notion》，2026-08-19）；Google Workspace 已对部分客户默认开启 AI 会议笔记（2026-08-18）。
- **本地文件**：Obsidian 生态最活跃：Smart Connections（5.5k star，本地 embedding 语义搜索，10-10 更新）、Fast Find 插件（fzf+embeddings 混合搜索，2026-10-29）、甚至有人把 Gemma 4 E4B 用 WebGPU 塞进 Obsidian（2026-09-09）。Logseq 在流失用户（"Leaving Logseq for Obsidian"，2026-10-19）。
- **AI-native 新物种**：多数死了或转型——Reor 仓库 2025-05 已 archived；Khoj 转型研究工作bench Open Paper/Pipali；Saner.ai 转型"ADHD 个人助理"。新一代是**给 agent 用的笔记本**：Hubble（开源，"for you and your agents"，HN 151 赞，2026-07-29）、Lapse（MCP 共享记忆笔记，2026-08-05）、Mnemoloci（专为 Claude Code 的 markdown 第二大脑，2026-10-20）。
- **语音/会议**：Granola 2M 格式扩张到全平台+语音输入；Google 2026-10-08 发布本地优先竞品 AI Edge Foresight（离线 EmbeddingGemma 2 740M）；开源侧 meetcap（本地实时转写+agent 可驱动，11-01 仍在更新）。

## 工程师真实工作流（HN 近 90 天一手讨论）
- **"哑 markdown 就够了"派**：257 赞热帖《Note-Taking and PKM》（2026-07-28）高赞评论：教科书笔记打进"一个 dumb markdown 文件"、全文搜索即可，复杂 PKM 系统是焦虑产物；配套反思文《Your Second Brain Won't Do the Work》（2026-09-21）。
- **agent 直读直写派**：Obsidian Copilot 描述已改为"Run agents in Obsidian - OpenCode, Codex, Claude Code etc."（11-03 仍在更新）；Hubble 帖子里用户直接说"大多数 LLM 都乐意直接吃 markdown 文件"（2026-07-29）；Emacs 党 45 赞帖照旧用 org-mode 不搬家（2026-10-07）。
- **agent 记笔记给人看**：Agents Workbook 让 Claude Code/Codex 自动写工作笔记（2026-08-18）；"32 个 Claude Code 会话 96.8% token 花在重读历史"（2026-07-30）从反面证明笔记/记忆层对 agent 的价值。
- 团队向：OzBrain（93 赞，agent 与团队共享知识库，2026-08-21）、Almanac YC S26（2026-08-31）。

## AI 的真实价值点 vs 噱头
- **真价值①捕获**：会议/语音→结构化笔记，Granola/Google Foresight/meetcap 三方（含一个免费开源）验证，且方向是本地/离线化。
- **真价值②检索与联动**：agent 在你提问时读你的库（RAG/全文搜索），社区接受度高；SQLite 压缩 markdown 上下文的 benchmark 帖（2026-10-27）说明 token 成本是真实驱动力。
- **噱头：AI 自动整理/自动链接/自动标签**：热帖中普遍被嘲讽为"生产力安慰剂"，用户实测结论是"搜索+agent 按需取用"胜过"预先组织"。

## 给 AI 开发者的推荐组合
1. **主力**：Obsidian/markdown 库（纯文件、无专有格式）+ Claude Code/Codex 直接读写 + Smart Connections 或 Fast Find 做混合检索；想加 GUI 就装 Obsidian Copilot（agent 模式）。
2. **会议捕获**：meetcap（开源、本地、免费）或 Granola；产出直接落 markdown 进库。
3. **给 agent 的记忆**：MCP 方式挂载笔记库（Lapse/Markdown Locker 思路），或参考 Hubble 自建双接口。
4. 避坑：别投入 AI 自动组织类功能；Notion AI / Reflect / Tana / Craft / Apple Notes+Intelligence 近 60 天社区一手实测未检索到（未验证）。

## 信源列表
- HN《Note-Taking and PKM》257赞 97评 2026-07-28: https://unattributed.cc/note-taking-and-personal-knowledge-management (news.ycombinator.com/item?id=49084324)
- Hubble 151赞 2026-07-29: https://www.hubble.md/ (id=49091730)
- Google Foresight 本地优先，TechCrunch 2026-10-08: https://techcrunch.com/2026/10/08/google-releases-a-new-local-first-granola-competitor/
- Granola 官网（全平台+语音输入）: https://granola.ai
- Obsidian Copilot（跑编码 agent）: https://github.com/logancyang/obsidian-copilot
- Smart Connections: https://github.com/brianpetro/obsidian-smart-connections
- meetcap: https://github.com/seacen/meetcap
- Mnemoloci（Claude Code 二脑）2026-10-20: https://github.com/siris9476/mnemoloci
- Lapse MCP 笔记 2026-08-05: https://lapse.in (id=49179101)
- Reor 已归档: https://github.com/reorproject/reor ；Khoj 转型: https://khoj.dev ；Saner.ai: https://saner.ai
- Notion agent 共享记忆博客 2026-08-19: https://www.notion.com/blog/building-shared-memory-for-ai-agents-in-notion
- Google Meet 默认 AI 笔记 2026-08-18: https://workspaceupdates.googleblog.com/2026/07/new-google-meet-take-notes-for-me-settings-for-admins-and-end-users.html
- Emacs 不搬家 45赞 2026-10-07: https://baty.net/posts/2026/10/i-tried-to-move-my-notes-out-of-emacs-i-failed/ (id=49998350)
- Leaving Logseq 2026-10-19: https://michelenasti.com/2026/logseq-to-obsidian/
- Your Second Brain Won't Do the Work 2026-09-21: https://korin.uk/your-second-brain-wont-do-the-work
- OzBrain 93赞 2026-08-21: https://ozbrain.com (id=49394827)；Almanac YC S26 2026-08-31: https://usealmanac.com/ (id=49511007)
- Agents Workbook 2026-08-18: https://github.com/softcane/agents-workbook；32 会话 token 分析 2026-07-30: https://note.com/roten/n/nac8aef48851f
- Gemma4 in Obsidian 2026-09-09: https://github.com/itsyuimorii/obsidian-gemma4-litert-wiki；Fast Find 2026-10-29: https://www.ssp.sh/brain/obsidian-fast-find-10k-plugin/
- Markdown SQLite token 效率 2026-10-27: https://www.withnative.ai/research-and-posts/markdown-context-benchmark
- 公开二脑 660 笔记 2026-08-02: https://www.ssp.sh/brain/

（方法说明：以上均来自 HN Algolia API 近 90 天检索 + 官网/GitHub/TechCrunch 直接抓取；Reddit JSON 403 未用；Notion AI/Reflect/Mem.ai/Tana/Capacities/Craft/Apple Notes+Intelligence 近 60 天一手实测信源未找到，标注未验证。）
