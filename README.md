# ITU-T FG-TIDA Paris input documents (v1.2)

Three contributions for the first meeting of the ITU-T Focus Group on Trust and
Identity for Humans and Agentic AI (FG-TIDA), Paris, 30 November - 1 December 2026.

- **Source**: Xinghua Zhao, independent expert (China), individual capacity
- **Format**: ITU-T Focus Group document template (Doc-FocusGroup_Document.docx)
- **Status**: filed 2026-11-11 via the TIDA DataTracker (records
  fg-tida-contribution-3 / -4 / -5, "Awaiting review"); not adopted, agreed or
  endorsed. Current builds are the corrected revisions below (contact email
  corrected to the author's ITU address); the earlier builds must not be used.
- **Supersedes**: v1.1 (2026-11-10)

| # | Document (corrected build) | Working group | ToR |
|---|---|---|---|
| 1 | `FG-TIDA-WG1-Cdra-InputDoc-v0.3.4.docx` | WG1/CDRA | 3.1 / 4.1 / 4.3 |
| 2 | `FG-TIDA-WG2-Ibea-InputDoc-v0.1.4.docx` | WG2/IBEA | 3.4 / 4.2 / 4.4 |
| 3 | `FG-TIDA-WG0-UseCases-v0.1.4.docx` | WG0/use cases | 3.3 / 4.1 |

The corrected builds are staged under `docs-rebuilt/` as base64 with hashes in
the manifests (see `docs-rebuilt/README.md`); decode them over `docs/` to land
the binaries.

## Run the checks

The WG2 contribution ships a dependency-free checker (Python standard library
only) for the act-content binding its record format defines:

```
python tools/act_content_check.py tools/record.json    # exit=0, binding satisfied
python tools/act_content_check.py --selftest           # 7 vectors, SELFTEST OK
```

Any Python 3 interpreter works; use `python3` instead of `python` on systems
that do not provide a `python` alias.

Expected output: see `tools/expected-output.txt`. The WG1 contribution's
Annex A states the record-completeness conditions (Registry, Evidence, Gates)
that this checker operationalises for the gate record.

**Which version is authoritative**: `main` is the authoritative branch. Tag
`v1.2` (7d82f5d, 2026-11-11) is the corrected-build revision; `main` carries
further red-team fixes committed after that tag, so `main` is never behind it.
The earlier `fix/version-consistency` pull request was closed on 2026-11-15
rather than merged: it conflicted and still carried the superseded
v0.3.3 / v0.1.3 binaries.

Fingerprints: see `manifest-3items.json`. Evidence pack: `evidence-pack/`.

Submission channels (dual route, identical information): (1) TIDA DataTracker —
filed 2026-11-11, records fg-tida-contribution-3 (WG1), -4 (WG2), -5 (WG0);
(2) TSB Circular 179, paragraph on contributions (FG GitHub space, ITU-T FG
contribution template) — filing in preparation with the corrected builds only.

The DataTracker record numbers above are internal reconciliation references for
the author and the ITU secretariat; they do not resolve to a public page. Public
verification of what was filed is this repository — tag `v1.2.1` (or later) and
the hashes in `manifest-3items.json`.
