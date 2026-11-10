# Re-verification of the 11 acceptance items (branch fix/version-consistency)

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | README version unified | PASS | README v1.2 == manifest v1.2 == filenames v0.3.3/v0.1.3 == DOCX cover revision |
| 2 | Markdown source version unified | PASS | sources/ revision lines set to v0.3.3 / v0.1.3 |
| 3 | DOCX consistency | PASS | manifest sha256 recomputed from the files in this branch; check_consistency.py |
| 4 | manifest completeness | PASS | 3 items, bytes + sha256; `.eml` as-sent set archived in `archive/AS-SENT-20261110T1351.md` |
| 5 | WG1 technical review | PASS (with NV) | docs/TECH-REVERIFICATION.md: definitions/completeness-vs-authenticity/boundaries PASS; external duplication NV |
| 6 | WG2 technical review | PASS (with FAIL+NV) | docs/TECH-REVERIFICATION.md: 3 fields/identity-vs-authority PASS; revocation-expiry FAIL (out of scope, stated); cross-system chains NV |
| 7 | WG0 case review | PASS (with NV) | docs/TECH-REVERIFICATION.md: context/inputs/outputs PASS; repeatable test method NV; interval example added |
| 8 | Three-file cross-check | PASS | `docs/CROSS-CONSISTENCY.md` |
| 9 | GitHub automation | PASS (new) | `.github/workflows/consistency.yml` runs positive + negative control on this branch |
| 10 | ITU submission conditions | PASS | Circular 179 §7; EWM DDP/email; deadline 23 Nov; pre-registration 20 Nov |
| 11 | Formal submission status | NOT VERIFIED | two emails sent 2026-11-10 13:51/13:53; no acknowledgement; status = emailed, awaiting acknowledgement |
