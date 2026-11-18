# STRUCTURE — 分层与改动代价

## 四层

| 层 | 位置 | 内容 |
|---|---|---|
| L1 源 | `sources-rst/{itu-wg0-usecases,itu-wg1-cdra,itu-wg2-ibea}.rst` | 三份投稿件的可编辑真源 |
| L2 产物 | `docs/*.docx`（3 件 × 3 版）、`docs-rebuilt/*.docx.b64` | 按 ITU 模板生成的成品与可重建副本 |
| L3 证据 | `evidence-pack/{citation-check,external-ai-review,redteam,publish-manifest}`、`evidence/account-table.md`、`manifest-3items.json` | 引用核查、外审、红队、发布清单、账号表 |
| L4 构建与校验 | `preview.ps1`、`requirements.txt`、`.github/workflows/{docs,Sync Github to Gitlab spec-template}.yml`、`tests/` | 生成、预览、CI、结构测试 |

## 改动代价

| 你想做 | 改哪里 | 必须重跑 | 必须同步 |
|---|---|---|---|
| 改一处论证 | `sources-rst/*.rst` | `preview.ps1` 生成 .docx → .b64 | `publish-manifest.json`、`CHANGELOG.md` |
| 出新版本 | rst 版本号 | 同上 | 保留旧版（不删除历史稿） |
| 换 ITU 模板样式 | 生成脚本 | 三份全部重建 | `docs-rebuilt/` 全部 |

## 边界

本仓是**一次会议的投稿材料**，不是长期规范仓。
长期规范出口在 `ai-passport-spec`；证据链格式在 `lgd-xverify`；本仓不与它们互借证据。
