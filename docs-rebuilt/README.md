# Corrected docx (base64 staging)

The three Paris contribution docx were rebuilt on 2026-11-10 (header
revision labels) and **corrected on 2026-11-11**: the contact email in
all three was wrong for the ITU context — it carried the author's W3C
address (zhaoxinghua07@126.com) instead of his ITU address
(zhaoxinghua06@126.com). The correction revision bumps the labels to
WG1 v0.3.4 / WG2 v0.1.4 / WG0 v0.1.4, dated 2026-11-11. Extracted-text
diff against the previous builds: only the contact lines and the
date/revision lines differ; all other zip entries are byte-identical.

They are staged here as base64 because this push channel carries text
only. To land them in `docs/`:

```
cd docs-rebuilt
for f in FG-TIDA-WG1-Cdra-InputDoc-v0.3.4.docx.b64 FG-TIDA-WG2-Ibea-InputDoc-v0.1.4.docx.b64 FG-TIDA-WG0-UseCases-v0.1.4.docx.b64; do base64 -d "$f" > "../docs/${f%.b64}"; done
```

(The v0.3.3 / v0.1.3 .b64 files still in this folder are the superseded
pre-correction builds — do not land those.)

Expected SHA-256 after decode:
- FG-TIDA-WG1-Cdra-InputDoc-v0.3.4.docx — 47deb02b57cd9a85de2e9ad66172c72899e7568d91404eb840b61ecb8ed90c1e
- FG-TIDA-WG2-Ibea-InputDoc-v0.1.4.docx — 6c67b46f79f5847b4c87f7e7ecea2fa2d2b21a0a3ddd470521893f01377e1203
- FG-TIDA-WG0-UseCases-v0.1.4.docx — 2feaf85281a73ac13658c1ec56bbdcf7c68bac04aa671a6a54cd7959ab508afc
