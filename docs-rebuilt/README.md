# Rebuilt docx (base64 staging)

The three Paris contribution docx were rebuilt on 2026-11-10: one stale
header-table revision label corrected per file so each docx matches its
corrected source (see evidence-pack/publish-manifest.json, rebuild_note).
Byte sizes are unchanged; all other zip entries are byte-identical to
the previous builds.

They are staged here as base64 because this push channel carries text
only. To land them in `docs/`:

```
cd docs-rebuilt
for f in *.b64; do base64 -d "$f" > "../docs/${f%.b64}"; done
```

Expected SHA-256 after decode:
- FG-TIDA-WG1-Cdra-InputDoc-v0.3.3.docx — dd3a493693e13c924a58902269045a0dcc4cae6db2f1e1e8c85a7f1802207619
- FG-TIDA-WG2-Ibea-InputDoc-v0.1.3.docx — d5b2a6ef3e5cdfa14429d520c2592ffc392610848fdfffc4e680fa4f6dbd2c3f
- FG-TIDA-WG0-UseCases-v0.1.3.docx — 6f7acd532ab02e4bccb00530705b84a9e21e0a68b44295f829c15bf100ba427f
