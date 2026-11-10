# P3 · 红队测试（四视角 + 逐条处置）

对象：ITU-T FG-TIDA 巴黎首会贡献件 v0.3 ｜ 时间：2026-11-10 ｜ 方式：4 个零上下文评审（fresh），本席裁决

## 一、四视角结论

| 视角 | 评审者 | 结论 | 要点 |
|---|---|---|---|
| G1 主席/程序 | `itu-g1-chair`（fresh） | BLOCKED（14 条：P0×1，P1×9，P2×4） | 自称 Filed 但无提交证据；会议标识写在 only::html 块会丢 PDF；Circular 日期口径；§2 非重复未回应；#15 未进参考文献；缺 Action requested；处置权措辞越权；A3 索取归属；署名/国别 |
| G2 技术 | `itu-g2-tech`（fresh） | PASS-WITH-FINDINGS（P1×3，P2×4） | 只证"记录自洽"不含信任边界（换 act 重算 digest 仍过）；类级占位记录通过；outcome/consulted 未在排除表点名；exit 3 死代码、determinism 不可证伪；RFC 8785 兼容说过强；四条/三条条件自相矛盾 |
| G3 竞争/风险 | `itu-g3-risk`（fresh） | BLOCKED（P0×1，P1×8，P2×3） | 仓库/tag 承诺未发布＝死引用；#60 标题不符；#15 当 issue 用；§2 越权自证；A1/A3 零增量易被"note and move on"；"Identical to"改名他人构念；硬编码 row 5；"third party can falsify"与"未验证"冲突 |
| G4 审计/回源 | `itu-g4-audit`（fresh，进行中） | 待回 | 逐条核 Circular/ToR/issue/日期/状态词 |

## 二、逐条处置（采纳 / 部分采纳 / 不采纳 + 理由）

| ID | 来源 | 发现 | 处置 | 落地 |
|---|---|---|---|---|
| R1 | G1-F1 | 状态写 "Filed" 但无提交证据 | 采纳 | 改为 "Draft for filing"（index History + Status 行） |
| R2 | G1-F2 | 会议标识/封面字段在 `.. only:: html` 块内，PDF 丢失 | 采纳 | 移除条件块；加 ITU 式封面表（Title/Source/Contact/Date/Meeting/Agenda item/Action requested/Status） |
| R3 | G1-F3 | Circular 日期口径 | 采纳 | 参考文献改为 "dateline Geneva, 8 October 2026（DOCX 本身）；落地页另有 Date 2026-10-05 / Posted 2026-10-19" |
| R4 | G1-F4 | 未回应 ToR §2 的 A.7 非重复条款 | 采纳 | Foreword 增补非重复声明；措辞改为"offered for the FG's determination" |
| R5 | G1-F5 | 引用 themes#15 但参考文献无条目 | 采纳 | 核实 #15 实为 PR（Provenance of Authority）；从线程表删行，参考文献改列 PR #15 |
| R6 | G1-F6 | 缺 "Action requested" | 采纳 | Abstract 后加 A1/A2/A3 三行 |
| R7 | G1-F7 | 自行规定处置方式（越权） | 采纳 | 改为 "disposition is for the meeting to decide" |
| R8 | G1-F8 | A3 索取 hosting 与交稿时间 | 采纳 | A3 降为 "note that the narrative is available" |
| R9 | G1-F9 | 可读性/术语未释义 | 部分采纳 | Abstract 缩短；关键术语（canonicalization、TOCTOU、pen）在正文首现处加释义；不再逐句重写 |
| R10 | G1-F10 | 署名与会别歧义 | 采纳 | Source 改 "Mr Xinghua Zhao, independent expert, in his individual capacity"；国别仅在 Contact 行 |
| R11 | G1-F11 | A.7 未标版本 | 采纳 | 参考文献写 "A.7 (08/24)"（ITU 页面核实 in force） |
| R12 | G1-F12 | 标题与内容范围不一致 | 采纳 | 标题扩为 "Act-content binding in the decision record and three candidate coordination terms" |
| R13 | G1-F13 | "Input document" 与 ITU 用语不一致 | 采纳 | 封面与正文统一为 "Contribution to the first meeting of ITU-T FG-TIDA" |
| R14 | G1-F14 | ≡/≈ 符号与 Unicode 风险 | 采纳 | 全部改为 "Identical to / Close to" 文字 |
| R15 | G2-F1 | 只证记录自洽，不含信任边界 | 采纳 | 第四章新增 Preconditions（binding 决策时固定 + 记录受保护），并在 03 章与 Annex B.4 声明边界 |
| R16 | G2-F2 | 类级占位记录通过 | 采纳 | 增加 instance-level 规则；脚本拒绝 `*`/`any` 等占位（exit 2）；自测加向量 |
| R17 | G2-F3 | outcome/consulted 未在排除表点名 | 采纳 | 规范化表新增"Excluded fields"行；Non-goals 明写决策值不在 digest 内 |
| R18 | G2-F4 | exit 3 死代码、determinism 不可证伪 | 采纳 | exit 3 改为"浮点值不可按 byte rule 规范化"（真实可触发）；自测加 float 向量；A.4 改述覆盖范围 |
| R19 | G2-F5 | RFC 8785 兼容说过强 | 采纳 | 取消 JCS 采用：byte rule 自定（码点排序、禁浮点）；RFC 8785 降为 related work，明确"未采用" |
| R20 | G2-F6 | 四条/三条条件矛盾 | 采纳 | 统一为"四条条件" |
| R21 | G2-F7 | 线程状态未回源 | 采纳 | 状态列改为 "open (observed 2026-11-10)"；标题逐字引 |
| R22 | G3-1 | 仓库/tag 承诺未发布＝死引用 | 采纳 | 改为 "to be published before the filing"；tag 说明"发布时创建；此前以封面 SHA-256 为不可变引用" |
| R23 | G3-2 | #60 标题不符 | 采纳 | 逐字引 #60 实际标题 |
| R24 | G3-3 | #15 当 issue 用 | 采纳 | 同 R5 |
| R25 | G3-4 | §2 越权自证 | 采纳 | 同 R4：改为"提交 FG 裁定" |
| R26 | G3-5 | A1/A3 零增量易被吸收 | 采纳 | 增加"若采用请记录本件为来源"的请求；把可检验产物（property+check）保持为主 ask（A2） |
| R27 | G3-6 | "Identical to"改名他人构念 + 重复病句 | 采纳 | 改 "An alias for"；命名/所有权留 #5 与术语工作；删除重复句 |
| R28 | G3-7 | 硬编码 #60 row 5 | 采纳 | 改为引"copy consulted / recency / reachability"原文 + 观察日期 |
| R29 | G3-8 | "falsify"与"未验证"冲突 | 采纳 | 改为 "re-run and verify"；措辞与 Annex B.4 一致 |
| R30 | G3-9 | 投稿资格依据缺失 | 采纳 | Foreword 补 Circular §5 + A.7 参与依据 |
| R31 | G3-10 | Circular 引证核对失分 | 采纳 | 同 R3，三层日期并列说明 |
| R32 | G3-11 | 无受理主体/议程位 | 部分采纳 | 增加"suggested: A1→术语工作，A2→#60 讨论"；议程项仍写 "to be allocated"（不越权替 FG 决定） |
| R33 | G3-12 | "Gate input" 裁定 #59 语义 | 采纳 | 措辞加 "as read in this contribution" |

## 三、红队合议

- 四视角中三席已回（G4 进行中）；P0 共 2 条（G1 状态声明、G3 未发布引用），均已修复。
- 修复后须**全文复评**（不得抽查），复评结论入 `expert-signoff.md`。


---

## 附：三件提交集口径（2026-11-10 13:10）

本证据包服务于 **ITU 巴黎三件提交集**（不是单件）：

| # | 件 | DOCX 字节 | SHA-256 | ToR |
|---|---|---|---|---|
| 1 | WG1/CDRA Registry–Evidence–Gates | 43,205 | `2c32d9c4…32073f` | §3.1/§4.1/§4.3 |
| 2 | WG2/IBEA 门禁三字段 + act-content binding | 42,392 | `a229ae38…8d0e8` | §3.4/§4.2/§4.4 |
| 3 | WG0/用例三件 | 43,434 | `ef3ba3d1…c2059` | §3.3/§4.1 |

- 格式：**ITU-T Focus Group document template**（`Doc-FocusGroup_Document.docx`，46,499 B，sha256 `b81ae0c5…5aeb58`）。
- 本包中单件（v1.0 act-content binding）的调研/回源/红队结论，对三件集**部分适用**：act-content binding 已并入 #2 的 Annex；三术语已并入 #1。
- 三件的逐件差异见 `work/itu-paris-3items/manifest-3items.json`。
