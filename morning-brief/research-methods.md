# 业界 AI 晨报/资讯获取调研

> 验证时间：2026-11-02。方法说明：本环境 web_search 工具不可用（缺 API key），全部信源改用 curl 直接访问官网验证；被 Cloudflare/网络屏蔽的站点在文中注明。凡标注"无法验证"的均未采信其细节。

## 1. 英文 newsletter（表格：名称 | 链接 | 频率 | 侧重 | 亮点）

| 名称 | 链接 | 频率 | 侧重 | 亮点 |
|---|---|---|---|---|
| TLDR AI | https://tldr.tech/ai | 每工作日（官网 FAQ 自述） | 模型发布、研究论文、工具，工程向 | 110 万订阅者，官方定位"denser and engineering-focused"；每条 1-3 句摘要+原文链接，5 分钟读完，免费无墙，是英文 AI 日报的格式标杆 |
| Ben's Bites | https://www.bensbites.com/ | 每周约 3 期（archive：10-29/27/22/20/15/13） | AI 创业、产品、agent 实战 | 118,000+ 订阅，Substack 托管；近期主题聚焦"building with agents + 值得一试的工具"，偏创业者/Builder 视角 |
| Import AI（Jack Clark） | https://jack-clark.net/（订阅 importai.substack.com） | 周更（已至第 478 期，最新 2026-10-26） | AI 研究+政策深度周评，"runs on arXiv" | Anthropic 联合创始人执笔，每期精选 4-5 个研究/产业信号并写"why it matters"，是对冲碎片化日报的深度锚点 |
| AlphaSignal | https://alphasignal.ai/ | 日更（官网自述 "Daily AI Newsletter for Engineers"） | 论文、模型、仓库、发布（"The Front Page of AI"） | 网站本体是实时聚合看板（验证时 1-24h 内多条新帖）+ 社区 upvote 排序；工程向、可按 topic 检索全库，适合做"信号热榜" |
| Latent Space | https://latent.space/ | 主刊每周 2-3 次；子刊 AINews 每工作日（订阅页自述） | AI 工程：深度分析、播客、每日简报 | "By and for AI engineers"；AINews 每工作日简报+全量可搜索看板 news.smol.ai；另有社区新闻板、700+ 人物 wiki，既是 newsletter 也是社区基础设施 |
| The Rundown AI | https://www.therundown.ai/ | 日更（官网自述 "Daily AI News & Insights in 5 Minutes a Day"） | 大众向：新闻+why it matters+实操指南+工具榜 | 350 万+读者，英文 AI 日报中订阅量最大之一；团队化多作者署名，有 AI 大学/指南/工具库等衍生产品，商业化的样板 |
| Superhuman AI（Zain Kahn） | https://www.superhuman.ai/ | 日报（工作日）；sitemap 显示 2026-11-02 当日仍在更新 | 面向职场人的 AI 提效新闻+技巧 | 职场泛用户群最大的 AI 日报之一；官网有 Cloudflare 拦爬，但其 sitemap.xml 可验证（1243 个 URL） |
| Smol AI News（= Latent Space AINews 看板） | https://smol.ai/news/ | 每工作日（站内标签 "ainews: weekday roundups"） | 模型/工具/研究动态日报 | swyx 团队出品；把每工作日简报做成全量、可搜索、可按 upvote 排序的网页看板，是"日报+数据库"二合一的典范 |
| Interconnects（Nathan Lambert） | https://www.interconnects.ai/ | 每周 2-3 篇（archive：10-30/28/25/20） | 开源模型、RLHF/后训练、前沿实验室动向 | 87,000+ 订阅；作者本人训练模型，开源/后训练领域的一手技术判断，免费+付费分层 |
| Simon Willison's Weblog | https://simonwillison.net/ | 博客日更（11-02 当日有文）；另有月度付费 newsletter | LLM 实测、安全漏洞、coding agent、开源工具 | 每个新模型发布当天即出一手实测；月度信自嘲"Pay me to send you less"——个人过滤器型信源的极致样本 |
| Hacker Newsletter | https://hackernewsletter.com/ | 每周五（2010 年至今） | 人工精选 Hacker News 每周精华（含大量 AI 内容） | 60,000+ 订阅；"hand-curated"人工精选 HN 是其唯一卖点，证明"社区热榜+人工把关"模式的持久生命力 |

## 2. 中文渠道

| 名称 | 链接 | 频率 | 侧重 | 亮点 |
|---|---|---|---|---|
| 机器之心 | https://www.jiqizhixin.com/ + 微信公众号「机器之心」 | 日更（多平台分发） | 国内最老牌 AI 垂直媒体：论文解读、技术深度、产业报道 | 技术长文解读见长；注：官网对程序化访问当前仅返回"数据服务"页，正文建议经公众号/浏览器获取 |
| 量子位 | https://www.qbitai.com/ | 日更多篇（验证时当天 5-9 小时内已发 3+ 篇） | 大众向 AI 资讯：模型动态、公司新闻、AI 硬件 | 覆盖面广、时效快，中文 AI 快讯的主力源；WordPress 结构，抓取/订阅友好 |
| 新智元 | 微信公众号「新智元」（官网 ai-era.com.cn 本环境 DNS 无法解析） | 日更（公众号） | 综合 AI 资讯+海外动态编译 | 头部 AI 公众号之一；海外新闻中文化速度快，建议以公众号为准 |
| AI科技评论 / 雷峰网 | https://www.leiphone.com/ | 日更（验证时"今日更新 11 篇"，另有日更"雷峰早报"栏目） | 学术（顶会、论文）+产业深度报道 | "雷峰早报"是中文圈成型的每日科技早报栏目；学术视角与量子位互补 |
| 极客公园 / Founder Park | https://www.geekpark.net/（CF 拦爬）；https://founderpark.net/（200 已验证） | 日更 | 极客公园：科技媒体；Founder Park：AI/创业社区 | Founder Park 聚焦大模型创业生态（访谈、深度、榜单），中文 AI 创业圈信息密度最高的社区品牌之一 |
| 宝玉的分享 | https://baoyu.io/ + X @dotey | 博客周更上下（最新 2026-10-20；X 为主要快讯阵地） | AI 工程实践、Claude/Codex 生态、高质量英文内容的中文翻译 | 中文圈最勤的"AI 工程翻译/评述"节点之一，有 RSS（/feed.xml）；@dotey 时间线本身即高信噪比 |
| 歸藏（guizang） | https://guizang.ai/ + X @op7418 + 公众号 | 网站聚合按日资讯与深度长文；X 高频 | 前沿模型动态、AI 工具一手测评 | guizang.ai 把其 X 内容沉淀为可检索网站；中文 AI 工具/模型风向标人物 |
| AI产品榜（AICPB） | https://aicpb.com/ | 月度榜单 | 按用户量排行的全球/中国 AI 产品榜（ChatBot、AI Search、Vibe Coding 等细分） | 数据化追踪 AI 产品格局变化，做产品观察/选品参考时可直接引用 |
| 科技爱好者周刊（ruanyf/weekly） | https://github.com/ruanyf/weekly | 每周五（最近推送 2026-10-31） | 泛科技周刊：工具、文章、资源、言论 | 107,426 stars，GitHub 上最大的中文周刊；"开源协作式 newsletter"的代表 |

## 3. 社区与聚合器（怎么用最有效）

- **Hacker News**（API：https://hacker-news.firebaseio.com/v0/ 已验证可用）：AI 重磅新闻几乎必上首屏。不走网页走 API：topstories/beststories + item 过滤关键词，配 hn.algolia.com 检索历史热帖；"昨天 HN 首屏 AI 条目"本身就是高权重筛选器。
- **Reddit（r/LocalLLaMA、r/MachineLearning）**（本环境网络屏蔽无法直连验证）：r/LocalLLaMA 偏开源模型实测与八卦、泄露前兆；每天扫 Hot 前 20 + 关键词监控，"社区比媒体快半天"。
- **Product Hunt**（403 CF 拦爬、域名活跃）：AI 新产品每日榜；每日榜单过一遍 + 周榜汇总，用于"新产品/新工具"栏目。
- **X/Twitter 列表玩法**：关注对象拆列表（官方 lab 账号 / 研究者 / 记者 / builder）+ 定时抓取；AlphaSignal（实时聚合论文/仓库/模型/发布）与 Latent Space AINews（聚合 X/Discord 后出每工作日简报）证明"自建 X 情报管道 + LLM 摘要"已被产品化验证。
- **Hugging Face Papers 与 Trending Models**（经 hf-mirror.com 镜像验证）：Daily Papers 是社区 upvote 的每日论文榜，比 arXiv 裸流信噪比高；trending models 反映开源生态风向。每日扫前 10 + 前 10 做两个固定栏目。
- **GitHub Trending**（200 已验证）：每日热门仓库（可按语言过滤）；AI agent/LLM 工具经常霸榜。daily trending + 关键词过滤作"开源动态"栏目。
- **arXiv cs.AI / cs.CL 日报**（均 200；验证时 cs.AI 当日新收 186 篇）：裸流信息量过大，业界做法是叠加过滤器——HF Daily Papers（人工+upvote）、alphaXiv 式讨论热度、或 LLM 按主题/机构打分后再进晨报。

## 4. 一手信源清单

| 信源 | URL | 验证状态 |
|---|---|---|
| Anthropic Newsroom | https://www.anthropic.com/news | 200 ✅ |
| OpenAI News | https://openai.com/news/ | 403（CF 拦爬，页面存在；可用 GitHub org + 二手源替代） |
| Google DeepMind Blog | https://deepmind.google/discover/blog/ | 200（JS 渲染） |
| Meta AI Blog | https://ai.meta.com/blog/ | 本环境超时，无法验证 |
| Microsoft AI 新闻 | https://news.microsoft.com/ | 重定向已验证；目标站 403 CF |
| xAI News | https://x.ai/news | CF challenge，域名活跃 |
| Mistral News | https://mistral.ai/news/ | CF challenge |
| Qwen 官方博客 | https://qwenlm.github.io/blog/（已迁移）；https://qwen.ai 200 | 200，列出 Qwen3Guard 等近期文章 |
| DeepSeek 新闻/更新 | https://api-docs.deepseek.com/news/ | 200，含 V4.1、deepseek-agent 等条目 |
| Cursor Changelog | https://cursor.com/changelog | 200 ✅ |
| GitHub Copilot（GitHub Changelog） | https://github.blog/changelog/ | 200 ✅ |
| Claude Code Changelog | https://docs.anthropic.com/en/docs/claude-code/changelog | 200 ✅ |
| Windsurf Changelog | https://windsurf.com/changelog | 200（现为 "Devin Desktop changelog"，Windsurf 并入 Cognition/Devin 体系） |

## 5. 自动化流水线与工具

**RSS/AI 阅读器层**
- Folo（原 Follow）：https://folo.is/；开源仓库 [RSSNext/Folo](https://github.com/RSSNext/Folo)（39,215★，2026-11-02 当日仍在推送）。RSS+社交+播客统一收件箱，自带 AI 摘要，中文生态好。
- Feedly（https://feedly.com/）与 Inoreader（https://www.inoreader.com/）：老牌 RSS 聚合，均有 AI 过滤/摘要；本环境无法直连（000），仅列作主流选项。

**自动化编排层（低代码 + LLM）**
- n8n：https://n8n.io/（200）；模板库 13,821 个——可自建"RSS/API 抓取 → LLM 摘要 → 邮件/IM 推送"流水线。
- Make（https://www.make.com/，200）、Zapier（https://zapier.com/，200）：同类无代码编排，接入 beehiiv/Substack 与 Slack/飞书更便捷。

**开源 AI 日报工作流（均经 GitHub API 验证 stars/活跃度）**
- [imsyy/DailyHotApi](https://github.com/imsyy/DailyHotApi)（4,103★）：今日热榜 API，聚合各平台热榜，支持 RSS 模式与 Vercel 部署——中文"热榜聚合"数据源层。
- [kevinho/clawfeed](https://github.com/kevinho/clawfeed)（2,401★，2026-05 后未推送）：聚合 Twitter/RSS 出结构化摘要+web 仪表盘。
- [leiting-eric/DailyBrief](https://github.com/leiting-eric/DailyBrief)（385★，2026-11-01 仍活跃）：GitHub 热门+X 热文等 23 个数据源聚合 + LLM 中文摘要，支持 GitHub Actions 定时部署——与"AI 晨报"最对口、仍在密集维护。
- [polyrabbit/hacker-news-digest](https://github.com/polyrabbit/hacker-news-digest)（754★）:newspaper: "Let LLM Summarize Hacker News for You"。
- [discus0434/nook](https://github.com/discus0434/nook)（289★）：每日聚合博客/Reddit/GitHub 并摘要的 web app。
- [Rion-Wu-tech/ai-daily-briefing](https://github.com/Rion-Wu-tech/ai-daily-briefing)（178★，10-20 活跃）：AI/Web3 自媒体每日早报生成工具。
- [wildlifechorus/condenseit](https://github.com/wildlifechorus/condenseit)（93★，10-20 活跃）：自托管——RSS/YouTube/网站 diff/Google News/HN/Reddit/GitHub Releases/播客 → Ollama/OpenRouter 摘要 → 按评分学习偏好 → 浏览器读报。隐私优先的完整参考实现。
- [frankzch/ai-news-brief](https://github.com/frankzch/ai-news-brief)（21★，10-12 活跃）：370+ 信源 → LLM 过滤打分 → SimHash+pgvector 去重 → 中英双语摘要。工程化最完整的去重/打分设计。
- [giftedunicorn/ai-news-bot](https://github.com/giftedunicorn/ai-news-bot)（27★）：Claude/DeepSeek + RSS + HTML 邮件日报机器人。

**知名 newsletter 的生产方式（有官方页面证据）**
- Latent Space AINews：署名编辑 + beehiiv 邮件 + news.smol.ai 全量可搜索看板——"自动化收集 + 看板沉淀 + 每工作日编辑发布"。
- The Rundown AI：具名作者团队 + 固定栏目（新闻/指南/工具/课程）——团队化人工编辑为主。
- TLDR AI：官网 FAQ 明确"每工作日、免费、5 分钟、摘要+原文链接"的编辑模式。
- Hacker Newsletter：2010 年起"hand-curated"人工精选。
- AlphaSignal：机器聚合+社区投票为核（"tracks every paper, repo, model, and release in real time"）。
- Simon Willison：日更一手实测 + 月度付费精选——个人专家过滤器模式。

## 6. 业界共性做法总结

1. **信源组合呈"金字塔"**：塔尖一手信源（官方博客/changelog）→ 中层人工编辑物（TLDR/Import AI/机器之心，做初筛和翻译）→ 底层原始流（arXiv/HN/GitHub Trending/HF Papers/X），只在需要提前量或验证时直接下探。
2. **筛选以"一手优先+交叉验证"为纲**：官方发布 > 实测者 > 编辑转述；同一事件需两个独立源再进晨报；社区热度（HN 首屏、HF upvote、Reddit Hot）作权重信号而非唯一标准。
3. **格式收敛于"5 分钟、分层、带链接"**：头条 1-3 条 + 一句话摘要 + 原文链接 + 固定栏目；TLDR 的"每条 1-3 句"与 Rundown 的"新闻+why it matters"是两种最常见模板；周报走"少而深+评论"。
4. **生成流程是"机器采集 → LLM 摘要 → 人工终审"三段式**：开源实现（DailyBrief、ai-news-brief、condenseit）均为多源抓取→LLM 打分/摘要/去重（SimHash/pgvector）→定时产出；商业 newsletter 保留人类编辑把关与署名。
5. **推送渠道多元但邮件为主干**：beehiiv/Substack 邮件；衍生网站看板（news.smol.ai）、TG bot、Obsidian/Notion/Slack。
6. **节奏"工作日晨发"是默认约定**（TLDR、AINews、AlphaSignal）；中文环境全周运转（量子位、雷峰早报）。
7. **去重与个性化是工程护城河**：SimHash+向量库去重、按评分学习偏好、社区 upvote 排序。
8. **商业模式"免费日报引流 + 付费深度/课程变现"**（Rundown AI University、Interconnects 付费层、Latent Space Pro）。

## 参考链接列表

- 英文 newsletter：tldr.tech/ai · bensbites.com · jack-clark.net · importai.substack.com · alphasignal.ai · latent.space · therundown.ai · superhuman.ai · smol.ai/news · interconnects.ai · simonwillison.net · hackernewsletter.com
- 中文渠道：jiqizhixin.com · qbitai.com · leiphone.com · geekpark.net · founderpark.net · baoyu.io · guizang.ai · aicpb.com · github.com/ruanyf/weekly
- 社区/聚合器：news.ycombinator.com · hacker-news.firebaseio.com/v0 · producthunt.com · huggingface.co/papers · github.com/trending · arxiv.org/list/cs.AI/recent · arxiv.org/list/cs.CL/recent
- 一手信源：anthropic.com/news · openai.com/news · deepmind.google/discover/blog · news.microsoft.com · x.ai/news · mistral.ai/news · qwen.ai · api-docs.deepseek.com/news · cursor.com/changelog · github.blog/changelog · docs.anthropic.com/en/docs/claude-code/changelog · windsurf.com/changelog
- 自动化：folo.is · github.com/RSSNext/Folo · feedly.com · inoreader.com · n8n.io/workflows · make.com · zapier.com 及上表所列开源项目
