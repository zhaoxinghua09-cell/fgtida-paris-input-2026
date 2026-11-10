# P11 · 回源核验（citation-check）

对象：贡献件 v0.3 ｜ 核验日期：2026-11-10 ｜ 每行：主张 → 一手源位置 → 原文/事实 → 判定

| # | 主张 | 一手源 | 原文 / 事实 | 判定 |
|---|---|---|---|---|
| 1 | 投稿经 FG GitHub 页 + ITU-T FG contribution template，截止 23 Nov | Circular 179 DOCX §7 | "Contributions should be submitted through the focus group's GitHub page using the applicable ITUT Focus Group contribution template provided on the dedicated page, no later than 23 November 2026." | 成立 |
| 2 | "dedicated page" = `FG-TIDA/spec-template` | Circular 179 DOCX 超链接（`tools/docx-links.py` 解 rels） | 链接文字 "dedicated page" → `https://github.com/FG-TIDA/spec-template` | 成立 |
| 3 | "GitHub page" = `https://github.com/FG-TIDA/` | 同上 | 链接文字 "GitHub page" → `https://github.com/FG-TIDA/` | 成立 |
| 4 | 预注册 20 Nov，现场/远程均强制 | Circular 179 Key deadlines + §9 | "20 November 2026 — Pre-registration via online form"；§9 "mandatory for both in-person and remote participation" | 成立 |
| 5 | Circular 落款日期 | DOCX 信头 | "Geneva, 8 October 2026" | 成立（文档日期；网页另有 Posted 2026-10-19） |
| 6 | ToR §2 排除项 | ToR 公开页 §2 | "Agentic AI protocols / AI governance / Digital ID …" | 成立 |
| 7 | ToR §2 含 A.7 非重复条款 | ToR 公开页 §2 | "…particular attention will be paid to the A.7 clause « The subject is not already addressed by work underway in ITU-T study groups or other focus groups… »" | 成立 |
| 8 | ToR §3.1 术语 / §3.3 用例 / §4.3 信任框架与生命周期 | ToR 公开页 | 三节标题与正文逐字匹配 | 成立 |
| 9 | themes#60 标题 | GitHub issue #60（200） | "[Joint: WG2 + #59] Inputs the enforcement point reads at decision time, by object" | 成立 |
| 10 | themes#59 标题 | GitHub issue #59（200） | "[Theme] Agentic AI trust control plane (working group proposal, ToR A.2.7; seeded by #18, open to #5, #41, #42)" | 成立 |
| 11 | themes#42 标题 | GitHub issue #42（200） | "Evidence Grading for Verifier Decisions: Separating Evidence Quality from Authorization Validity" | 成立 |
| 12 | themes#43 标题 | GitHub issue #43（200） | "Contribution: Evidence-Graded Authorization Verdicts for Agentic AI (refined from themes#42)" | 成立 |
| 13 | PR #15 标题 | GitHub PR #15（200） | "Provenance of Authority for Agentic AI (originating issue #5)" | 成立 |
| 14 | themes#5 标题 | GitHub issue #5（200） | "[Theme] Provenance of Authority for Agentic AI" | 成立 |
| 15 | 撤回件状态 | wg1-cdra-charter #5（API 200） | "RETRACTED: Paris input contribution (posted in the wrong channel)"; state=closed; closed_at 2026-11-10T04:34:22Z | 成立 |
| 16 | A.7 现行版本 | ITU-T 页面（200） | "A.7 (08/24) … In force" | 成立 |
| 17 | DataTracker 可达性 | 2026-11-10 实测 | `fetch failed` | **不成立（NV）** |
| 18 | 本文档公开仓库可达性 | 未发布 | 404 预期 | **NV（发布后补）** |
| 19 | 校验脚本自测 | 本机实跑 | 7/7 PASS，exit 0 | 成立（本机实测） |

## 判定汇总

- 成立：16 条
- 不成立/NV：2 条（#17 DataTracker 不可达；#18 仓库未发布）
- 无"未标 NV 的推测"；无二手摘要当源。


---

## 附：三件提交集口径（2026-11-10 13:10）

本证据包服务于 **ITU 巴黎三件提交集**（不是单件）：

| # | 件 | DOCX 字节 | SHA-256 | ToR |
|---|---|---|---|---|
| 1 | WG1/CDRA Registry–Evidence–Gates | 43,490 | `cbf4232a…27a4d6` | §3.1/§4.1/§4.3 |
| 2 | WG2/IBEA 门禁三字段 + act-content binding | 42,930 | `e41a5ae9…7c3a68` | §3.4/§4.2/§4.4 |
| 3 | WG0/用例三件 | 43,908 | `9f58b9b1…6516f1` | §3.3/§4.1 |

- 格式：**ITU-T Focus Group document template**（`Doc-FocusGroup_Document.docx`，46,499 B，sha256 `b81ae0c5…5aeb58`）。
- 本包中单件（v1.0 act-content binding）的调研/回源/红队结论，对三件集**部分适用**：act-content binding 已并入 #2 的 Annex；三术语已并入 #1。
- 三件的逐件差异见 仓根 `manifest-3items.json`。

---

## 刷新附注（2026-11-10 晚，Muse 席）

- 附表指纹已刷新为公开仓 `docs/` 中交付版 docx 的实测值（仓 HEAD 5dd8b92）；原表所列为 v0.3.1 期中间构建，已被交付版取代。仓根 `manifest-3items.json` 的 docx 指纹与附表一致；其 source 指纹早于交付版源文件，待构建侧重建 docx 时一并重生，本次刷新未改动该文件。
- **#17 更新**：tida-datatracker.org 于 2026-11-10 晚在 Muse 席网络实测**可达**（站点与 /submit/ 路径可打开，注册为自助式）；作者报告其本地网络不可达。故 #17 原「fetch failed」为特定网络下的观测，不再记不成立，改为「可达性依网络而定」。
- **#18 更新**：三件集公开仓已发布并可达（https://github.com/zhaoxinghua09-cell/fgtida-paris-input-2026 ，未登录可读），#18 由 NV 转**成立**。
- 更新后汇总：成立 17 条；依网络而定 1 条（#17）；NV 0 条。
