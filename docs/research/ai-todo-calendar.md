> 调研日期 2026-11-03 · 由三个并行研究子会话分别完成（待办/日历、笔记、知识库），方法=HN Algolia+社区讨论+厂商页+GitHub API，未核实项随文标注。

# AI 管待办与日历:2025-2026 真实使用图景(调研 2026-11-03,来源:HN Algolia、厂商官网、cn.bing、gh api)

## 一、三类玩法分层

**① 全自动排期 AI(算法替你决定什么时候做什么)**
- **Motion**(usemotion.com):现已扩张为"AI SuperApp"(AI Projects/Tasks/Calendar/Meetings/Docs)。核心仍是优先级+时间估算+chunking 的自动排期算法([HN 细节描述](https://news.ycombinator.com/item?id=39032816))。
- **Reclaim.ai**:主打 Habits/专注时间/多日历同步的自动重排,官网明确列出 AI Focus Time、AI Habits、AI Buffer Time 等模块([reclaim.ai/pricing](https://reclaim.ai/pricing))。2024-08 被 Dropbox 收购。

**② AI 助手增强型(人主导规划,AI 做捕获/解析/建议)**
- **Sunsama**:每日引导式规划仪式+拖拽时间块,非全自动。HN 口碑最稳的一档(见下)。
- **Akiflow**:快速捕获+命令栏,创始人明确定位"intentional planning"对打 Motion 的"AI scheduling"([HN](https://news.ycombinator.com/item?id=33457139))。
- **Todoist**:Help Center 已设 "AI features" 分区 + Beta "Automations"(描述工作流即自动执行)([todoist.com/help](https://todoist.com/help))。
- **TickTick/滴答清单**:强 NLP 日期解析是传统卖点;AI 会员功能见第三节。

**③ 传统工具 + AI 补位**
- 开源基础设施:[cal.com](https://github.com/calcom/cal.com)(49.7k stars,"scheduling infrastructure for absolutely everyone")。
- 自建脚本:有用户只用 Reclaim 的日历合并、嫌 AI 烦,自建 [mightycalendar.com](https://news.ycombinator.com/item?id=47443310) 并通过 Google 审核;HN 常见"caldav + 十行脚本"调侃([例](https://news.ycombinator.com/item?id=41302030))。

## 二、真实社区共识(HN)

**Motion**
- 算法本身受认可:任务给紧急度+耗时+最小分块,它会自动排出"今天 3-4pm 做高优先级 B、明天上午补 A"([HN](https://news.ycombinator.com/item?id=39032816))。
- 贵:"prohibitively expensive" 是常见评价([HN](https://news.ycombinator.com/item?id=44999037));官网价格页 JS 渲染,具体数字**未核实**(公开资料常引 $19-34/月档)。
- 实操坑:忘记勾"完成",任务会不断重新塞进日历空档([HN](https://news.ycombinator.com/item?id=42274875));有付费用户因多日历同步功能被砍而流失([HN](https://news.ycombinator.com/item?id=43646638))。

**Reclaim**
- 收购公告下高赞忧虑:"这会是我末日开端的开端"——用户喜欢产品但不喜欢 Dropbox(HelloSign 先例)([故事帖 41302030](https://news.ycombinator.com/item?id=41302030));创始人 Lightbody 至 2026 年仍在 HN 一线答疑(可见 [48652201](https://news.ycombinator.com/item?id=48652201)、[46707627](https://news.ycombinator.com/item?id=46707627)),运营未死。
- 真实留存逻辑:老用户留下的理由是多日历合并+Habits,AI 排期反而不是刚需([vindex10](https://news.ycombinator.com/item?id=42990949)、[sph130](https://news.ycombinator.com/item?id=47443310));亦有"AI in hype only"的质疑([oneeyedpigeon](https://news.ycombinator.com/item?id=48024409))。

**Sunsama**
- 正面居多且具体:ADHD 用户称自动排槽+每周目标复盘"帮我保持正轨",但承认前几天学习曲线陡([HN](https://news.ycombinator.com/item?id=35855156));多人推荐其"daily ritual 把 time-blocking 变成习惯"([HN](https://news.ycombinator.com/item?id=41934273));有用户"整个公司迁移到 Sunsama"([HN](https://news.ycombinator.com/item?id=35588553))。
- 反面:也被吐槽"只解决一块拼图",目标-任务-习惯仍然割裂([HN](https://news.ycombinator.com/item?id=47641840));定价页 JS,具体价格**未核实**(常见说法 $16-20/月)。

## 三、中文场景(滴答清单)

- 官网升级页确认:Premium **¥139/年**,会员权益明确包含 "AI Features"(还有多日历视图、微信提醒等)([dida365.com/about/upgrade](https://www.dida365.com/about/upgrade))。
- AI 功能的具体能力清单**未核实**:帮助中心相关页 404,cn.bing 中文检索被广告污染,未拿到可靠评测。
- 国际版 TickTick 在 HN 口碑:免费档已够用("生活简单多了",[HN](https://news.ycombinator.com/item?id=49521812));有印度用户靠本地化定价年付极便宜([HN](https://news.ycombinator.com/item?id=47196592))。国际版独立 AI 助手页面 404,生成式 AI 助手现状**未核实**。

## 四、最终推荐

**个人轻量(免费/低价优先)**:滴答清单免费版或 TickTick(NLP 录入+日历视图)起步,真需要 AI 再上 ¥139/年会员;海外用户可选 Todoist(AI features 已入正档)。理由:HN 共识是全自动排期对个人"仪式感"价值有限,先把捕获做快最实在。
**团队重度(会议多、多日历)**:Reclaim.ai 为核心(多日历合并+Habits+专注时间防御是留存主力,价格低于 Motion,且创始人仍活跃维护)+ Linear/Notion 管任务。若团队愿意为"全自动排期+项目管理一体"付高价,再评估 Motion 全家桶——注意退订主因是价格与"忘记勾完成即垃圾排期"的维护负担。

---
*未核实项已随文标注;HN 链接均为可点开的具体评论/帖子。*
