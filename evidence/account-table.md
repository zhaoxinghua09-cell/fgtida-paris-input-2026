# P1 · 专家走流程与账号对表

件：ITU-T FG-TIDA 巴黎首会贡献件《Act-content binding in the decision record and three candidate coordination terms》（v0.3）

## 一、账号（单线程单 handle）

| 项 | 值 |
|---|---|
| 提交账号 | **理论号 `zhaoxinghua09-cell`**（显示名 Xinghua Zhao） |
| 允许用途 | ITU/W3C 提交与评论、标准参与件（`docs/PARTICIPATION-PROCESS.md` §12.2） |
| 禁止 | 产品号 `stevenzhao07`、评测号 `LGD-Eval` 进标准组织线程 |
| token 取用 | DPAPI 保险库 label（`gh-as.mjs` 注入子进程，不打印、不落盘） |
| 本件是否用 LGD-Eval | **否**（全文已清零品牌词：LGD / LGD-Eval / DEUSPROOF / SynomosAI / MedXpert） |

## 二、流程对表（S0–S9）

| 阶段 | 本件状态 | 证据 |
|---|---|---|
| S0 选题/认领 | 选题＝act-content binding（#60 决策记录行）+ 三候选术语 | 本目录 `src/doc/index.rst` |
| S1 一手源调研 | 已完成：Circular 179 §7 超链接定位模板与投递面；ToR §2/§3.1/§3.3/§4.3；5 个 themes 线程；PR #15 | `research.md`、`citation-check.md` |
| S2 草稿 | 已完成：spec-template 结构（index + 7 章 + 2 附录 + 图 + 脚本） | `src/doc/` |
| S3 红队 | 4 视角（主席/技术/竞争/审计）；G1/G2 已回，G3/G4 进行中 | `redteam.md`、`zero-context-review.md` |
| S4 外人实测 | URL 全绿；脚本可离线复跑；公开仓库待发布（NV） | `outsider-test.md` |
| S5 外部 AI | 待回执（非 E4，须披露） | `external-ai-review.md` |
| S6 单件授权 | 授权基础：用户 2026-11-10 指令"全面负责 ITU 贡献件的整理和提交"；**最终"发"待逐字确认** | `authorization.md` |
| S7 提交 | 通道已定：Circular 179 §7（FG GitHub 页 + spec-template）；DataTracker 当前不可达 | `publish-manifest.json` |
| S8 回执归档 | 未发生（未提交） | — |
| S9 复盘入库 | 本证据包 + 知识库登记 | 同步记录 |

## 三、身份口径

- 署名：**Mr Xinghua Zhao, independent expert, in his individual capacity**
- 国别仅出现在 Contact 行（China），不写机构、不写品牌。
- 声明：不代表任何组织；非工作组产出；未采纳、未同意、未背书。
