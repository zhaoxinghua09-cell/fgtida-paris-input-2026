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

## A later generation exists in `docs/` — read this before landing anything

The three builds above (WG1 v0.3.4 / WG2 v0.1.4 / WG0 v0.1.4, 2026-11-11) were
later bumped once more, to WG1 v0.4 / WG2 v0.2 / WG0 v0.2. `manifest-3items.json`
is the file that records this; the table in the top-level README and this page
both still describe the 2026-11-11 generation.

**What changed between the two generations: one line per document — the revision
label.** Extracted text of `word/document.xml` differs in exactly two lines each
(old label out, new label in), and the paragraph counts are identical: 155 / 138 /
355. Nothing else moved. Verified by extracting both builds and diffing the text.

Only the newer generation has `.b64` staging in this folder for all three. The
`.b64` files whose names match the current build are the ones to land; the
`v0.3.4 / v0.1.4 / v0.1.4` `.b64` files are kept so that what was filed on
2026-11-11 remains reproducible.

Expected SHA-256 of the three binaries currently in `docs/`, measured against
the published files on 2026-11-17 (all three matched `manifest-3items.json`):

- `FG-TIDA-WG1-Cdra-InputDoc-v0.4.docx` — 0fab8fe358d051e4aa9a750de548036b470ac954f99b297482a6486b3ec8b0b7
- `FG-TIDA-WG2-Ibea-InputDoc-v0.2.docx` — c9c6586dadf1a02e1a2aa577eabbff43a7cc54470c8f2fb38b65d60dab5bc6ac
- `FG-TIDA-WG0-UseCases-v0.2.docx` — 497be91d179e50951f1875202f904b5d8d13a03f607f088345c931e9b16cdc2f

Which of the two generations was actually filed is a question for the DataTracker
record, not for this repository. This repository keeps every generation so that
either can be reproduced and compared; it does not assert which one the
secretariat received.
