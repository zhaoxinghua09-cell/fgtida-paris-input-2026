# Technical re-verification (items 5–7 of the 11-item table)

Scope: the three v1.2 documents in this branch (WG1 v0.3.3, WG2 v0.1.3, WG0 v0.1.3).
Status values: PASS (evidence in the document), FAIL (defect), NV (not verified, with reason).
No claim of standard adoption; external standards comparison not performed where marked NV.

## WG1/CDRA (v0.3.3)

| Check | Status | Evidence / basis |
|---|---|---|
| Registry / Evidence / Gates defined | PASS | §2 definition table; each term has a one-line definition and a record-level completeness test |
| Evidence completeness vs authenticity separated | PASS | §2 Evidence row + Annex A boundary sentence: passing = three record-completeness conditions, "not a certification, endorsement or verification of authenticity" |
| Hash / signature / source / time boundaries stated | PASS | Annex A field list (identifier, source, date YYYY-MM-DD, stated attribution recorded not verified); Annex B limitation paragraph (no signature authenticity check) |
| Duplication with existing standards / other WGs | NV | Requires clause-level comparison with SG17 in-force texts and the other FG threads; not performed in this branch |
| Each technical claim has a basis and a verifiable method | PASS (method) / NV (external validation) | Annex A gives field-presence checks; Annex B states "reproducible in method, not against a pinned endpoint" |

## WG2/IBEA (v0.1.3)

| Check | Status | Evidence / basis |
|---|---|---|
| Actor / Authority / Effect support after-the-fact accountability | PASS | §2 three-field record + §4 worked example; each field answers who / on whose authority / did what |
| Revocation, expiry, scope change handling | FAIL (documented gap, not hidden) | §5 boundary + Annex C mapping; the document states scope is the record content, revocation timing is out of scope; noted as follow-up, not claimed as solved |
| Identity vs authority kept distinct | PASS | §2 separates Actor (identifier resolving to a registered instance) from Authority (the source that conferred the right) and explicitly says identity is not authority |
| Cross-system / cross-subject authority chains | NV | Federation-wide authority chain semantics not defined in this document; deferred (Annex C non-goals) |
| Independent third-party re-check possible | PASS (method) / NV (implementation) | Annex C states the binding is recomputable from the record; the checker is in tools/; no independent implementation ran it in this branch |

## WG0/UseCases (v0.1.3)

| Check | Status | Evidence / basis |
|---|---|---|
| Clear business context per case | PASS | three cases: delegated authority, gated update, mid-session revocation; each has context and actors |
| Inputs, outputs, expected results per case | PASS | each proposal has Action / Expected result / Success criteria fields |
| Repeatable test method | NV | no runnable test for the use cases; scenarios are described, not scripted |
| Measurable acceptance criteria | PASS (one example) / NV (others) | bounded interval now carries an example value ("within 15 minutes; the FG may set the value"); other criteria qualitative |
| Relation to FG-TIDA work items | PASS (ToR mapping) / NV (theme links) | ToR clauses cited per proposal; theme references added (themes#42/#43/#59/#60); issue text not re-verified here |

## Summary

- PASS: 10 checks; FAIL: 1 (WG2 revocation/expiry handling is out of scope, stated); NV: 5 (external duplication, cross-system chains, independent implementation run, use-case test method, theme-issue re-verification).
- No claim in the documents was found to assert ITU adoption, agreement or endorsement.
- FAIL and NV items are carried in the PR description and are author decisions, not silently closed.
