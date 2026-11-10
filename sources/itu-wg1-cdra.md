# Lifecycle Trust for Agentic AI: A Registry–Evidence–Gates Coordination Framework

**ITU-T FG-TIDA — Input Document for the First Meeting (Paris, 30 November – 1 December 2026)**

| Field | Value |
|---|---|
| Document type | Contribution (Input Document) |
| Proposed handling | for action |
| Agenda item | To be allocated by the FG |
| Document ID | To be assigned by TSB |
| Source | Xinghua Zhao, independent expert (China) |
| Contact | zhaoxinghua07@126.com |
| Date | 2026-11-10 (revision v0.3.3) |
| Related FG work | Terms of Reference §3.1 (Terminology and definitions), §4.1 (Use cases and requirements analysis), §4.3 (Trust framework(s) and lifecycle management) |
| Pages | 5–6 (estimated; typeset length to be confirmed) |
| IPR | The author asserts no IPR claim over this contribution; it is offered for the Focus Group's use under the ITU-T A.7 / ITU common patent policy. |

> Status: content complete. Submission for the meeting is through the Focus Group's GitHub space using the ITU-T FG contribution template (Circular T25-TSB-CIR-0179).

---

## 0. Summary of what is proposed

The Terms of Reference of the ITU-T Focus Group on Trust and Identity for Humans and Agentic AI (FG-TIDA) already lists objectives on terminology (§3.1), use cases (§3.3) and deliverables spanning use-case and requirements analysis (§4.1) and trust frameworks and lifecycle management (§4.3). Contributors are arriving with separate vocabularies for three things that every agentic system needs: identification, evidence, and authorisation. This contribution offers **three coordination terms** — *Registry*, *Evidence*, *Gates* — each with a minimal record-completeness check, plus **three minimal use cases** written so they can be entered in the existing use-case work without modification. It proposes **no new work item, no new mandate, and no preferred technology**. The request (§4) is threefold: adopt the terms as coordination terms, enter the use cases, and indicate which existing deliverable should host the narrative.

## 1. Problem statement

Agentic AI systems are beginning to take actions that cross organisational boundaries: they invoke services, commit transactions, and make decisions whose effects persist after the interaction ends. Current standardisation work describes, in separate tracks, how such an actor is identified, what evidence accompanies an action, and who authorises a transition. What is missing is not another component but a **common way to say how the three fit together** — so that a registry maintained by one working group can be queried by another, an evidence record produced by one actor can be checked by a third party, and a gate enforced at one boundary can be recognised at the next.

This contribution proposes no new technology and no new mandate. It proposes a **coordination vocabulary of three primitives** and a mapping onto work already listed in the Terms of Reference, so that contributions arriving from different participants describe the same lifecycle in the same words. If the group prefers, the terms can be recorded as *working definitions* pending glossary consolidation — the value lies in the shared wording, not in the provenance of the wording.

## 2. Proposal: three composable primitives

| Primitive | Working definition (proposed for the FG glossary) | What it makes possible |
|---|---|---|
| **Registry** | A queryable, versioned record of which actors, artefacts and decisions exist, with an identifier, an owner, a version and the basis on which registration was made (the basis is recorded, not verified by the check). | Any party can ask "does this actor exist, who owns it, which version is current" without bilateral agreements. |
| **Evidence** | A record that a *specific action* occurred, carrying at minimum a source, a date (YYYY-MM-DD), and a stated attribution. | Records can be checked for completeness after the fact; whether the act occurred, or whether the attribution is authentic, is out of scope and requires a signature or other anchor. |
| **Gates** | A defined transition point where a change requires a decision: trigger → assessment → authorisation → review, with machine-proposed and human-authorised steps recorded. | Evolution of an agent or a model becomes an auditable event rather than a silent update. |

Three properties are intended and should be tested by the group:

1. **Composability** — each primitive is usable alone; none requires the other two to be adopted first.
2. **Non-exclusivity** — the framework describes *relations between* existing mechanisms; it does not designate a preferred registry technology, evidence format, or gate policy.
3. **Checkability** — each primitive has a minimal **record-completeness check** (Annex A): it verifies that the required fields are present and internally consistent, and it does **not** verify signature authenticity. A claim of conformance can therefore be falsified at the level of record completeness by a third party, rather than only asserted.

Three readings this document is written to avoid: that it proposes a new work item (it does not — §3 maps it onto existing clause-level work); that it prefers a particular technology or vendor (it does not — §2 property 2); and that a passing check constitutes approval of anything (it is a record-completeness check, not a certification — Annex A boundary sentence).

### 2.1 Minimal use cases (one per primitive)

- **Registry, minimal case.** An agent acting on behalf of a human is registered at first use; the record holds an identifier, an owner, and a version. A counterparty queries the record before accepting the action. Failure mode addressed: an actor that cannot be attributed after the fact.
- **Evidence, minimal case.** A consequential decision (a release, a refusal, an escalation) produces one evidence item carrying source, date, and a stated attribution. An auditor checks the item without accessing the actor's internal systems. Failure mode addressed: a claim that carries no traceable origin.
- **Gates, minimal case.** A model or policy update is proposed; the transition is blocked until an assessment is recorded and a human authorisation exists; the release and the review are both logged. Failure mode addressed: an update that takes effect with no accountable decision.

The formal use-case entries are submitted in the separate WG0 contribution; the three cases above are term-level examples, not a second set of entries.

## 3. Mapping to the Terms of Reference

The framework is deliberately shaped to fit work already listed, rather than to propose new items. The mapping below uses the public Terms of Reference (https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx), and refers to clause numbers rather than to ToR Annex A item identifiers.

| ToR clause | Kind of work | What this contribution supplies |
|---|---|---|
| **§3.1** Terminology and definitions | Objective: harmonise concepts, terminology and working definitions | Definitions of *Registry*, *Evidence*, *Gates* as coordination terms, with the boundary sentence in Annex A that they describe relations, not technologies. |
| **§4.1** Use cases and requirements analysis | Deliverable: reports analysing selected use cases and associated technical requirements | Three minimal use cases (§2.1), each written so that it can be entered in that work without modification. |
| **§4.3** Trust framework(s) and lifecycle management | Deliverable: frameworks defining how trust is established, evaluated, maintained and revoked, including lifecycle considerations and human oversight | A lifecycle narrative — registration at first use, evidence at each consequential act, gate at each transition — usable as a chapter on cross-group coordination. |

Out of scope for this contribution, stated explicitly: agentic AI protocol design, AI governance policy positions, and digital identity content. Those are addressed by other participants; this document only supplies the coordination vocabulary between them.

## 4. Request to the Focus Group

Each request is written so that it can be accepted, amended or declined at the meeting without sending the document back for revision.

| # | Request | If accepted, the FG gets | If declined or deferred |
|---|---|---|---|
| R1 | Adopt *Registry*, *Evidence*, *Gates* in the FG work on terminology (§3.1) as **coordination terms**, with the Annex A definitions and the boundary sentence. | A shared vocabulary for cross-group contributions; no technology commitment required. | Terms remain working definitions in this document; carried to the second meeting (Geneva, 26–27 January 2027). |
| R2 | Enter the three minimal use cases into the use-case work (§4.1), attributed to this contribution. | Three entries usable as-is, each tied to one failure mode. | Cases stay in §2.1 and can be re-submitted in whatever register format the group decides on. |
| R3 | Indicate the **intended host** for the lifecycle narrative — §4.3 framework text or a working-group draft. | Text prepared in the right form for the second meeting. | Narrative remains available; form is adapted once the host is known. |


**Non-duplication (ToR §2, Rec. ITU-T A.7).** This contribution does not reopen
work already under way in ITU-T SG17 or in the Focus Group. It supplies a
record-level vocabulary and check on top of the threads already published in the
FG's GitHub space; where a thread already covers a point, this document defers to
it. The Focus Group and the SG17 Chair remain the judges of whether any overlap
exists, under ToR §2.

This input document formalizes the contribution recorded in the FG's GitHub space as themes#39 (with its archive thread themes#38); it does not reopen that thread, and the FG remains the judge of overlap under ToR §2.

Further references, with permanent links:

- themes#5 — https://github.com/FG-TIDA/themes/issues/5
- themes#42 — https://github.com/FG-TIDA/themes/issues/42
- themes#43 — https://github.com/FG-TIDA/themes/issues/43
- themes#59 — https://github.com/FG-TIDA/themes/issues/59
- themes#60 — https://github.com/FG-TIDA/themes/issues/60

## 5. References and attribution

- ITU-T FG-TIDA, Terms of Reference — public text at https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx (clauses §3.1, §3.3, §4.1, §4.3 cited above). The TIES-restricted document [295-PLEN] is cited by document number only and is not relied on for any quotation.
- ITU-T FG-TIDA, Circular T25-TSB-CIR-0179, Geneva, 8 October 2026 (DMS Date 2026-10-05; posted 2026-10-19) — public text at https://www.itu.int/md/T25-TSB-CIR-0179/en. Its paragraph on contributions states the submission route and the 23 November 2026 deadline.
- **M. Barbosa, DEUSPROOF** (deusproof.com) — the author thanks DEUSPROOF for a worked state-at-date example with RFC 3161 and OpenTimestamps receipts and for pointing to the project's open-source verifier (https://github.com/deusproof/verifier), which the project describes as an offline verifier. The example informed the framing of Annex B. This acknowledgement is a source attribution only: it is not a validation of this contribution by DEUSPROOF, not an endorsement by the author of DEUSPROOF or its verifier, and not a recommendation of any product or provider. The author has no commercial relationship with DEUSPROOF. No validation result is claimed on DEUSPROOF's behalf.
- Reproducible material: the three record-completeness checks in Annex A are specified at the level of field presence and field semantics; a formal schema is proposed as a next step. The public location of the contribution package is given in Annex B.

*No trademark, no DOI, no canonical identifier is asserted in this document. Views are those of the named individual expert and do not represent any organisation.*

## 6. Handling note

This document is submitted **for action**, no later than **23 November 2026**, in accordance with the contribution paragraph of Circular T25-TSB-CIR-0179. Participants are reminded that **pre-registration closes on 20 November 2026** and is required for both on-site and remote participation. If the group prefers to record this as information rather than discuss it, the requests in §4 stand and are carried forward to the second meeting.

---

## Annex A — Proposed glossary entries and record-completeness conditions

| Term | Proposed definition | Minimal check (falsifiable) |
|---|---|---|
| Registry | A versioned, queryable record of actors, artefacts and decisions, with owner and registration basis. | A record that lacks an identifier, an owner, or a version fails the check. |
| Evidence | A record that a specific act occurred, carrying source, date, and a stated attribution. | An evidence set that is required but empty fails; an item missing source, date, or a stated attribution fails. Authenticity of the attribution is **not** verified by this check. |
| Gates | A transition point requiring assessment and human authorisation, both recorded. | A governance record with no gate, or with no recorded assessment or no recorded human authorisation, fails the check. |

**Field notes (minimal semantics, so the checks are reproducible without a schema):**

- `identifier` — an opaque string, unique within the namespace of the registering authority. Namespace governance is out of scope for this check.
- `owner` — the entity accountable for the actor; a string, not a URI.
- `version` — a monotonic label; comparison semantics are out of scope.
- `date` — an ISO 8601 calendar date (`YYYY-MM-DD`); comparison is by that lexical form.
- `stated attribution` — a declared signer or source label carried with the item; it is recorded, not verified.
- `required` — declared by the record itself (the `evidence.required` flag), not by an external policy document.

A record exercising all three, in the form used for the checks described in Annex A:

```json
{"subject":{"identifier":"agent-01","identity":{"owner":"org-a","version":"1.2"}},
 "evidence":{"required":true,"items":[{"source":"pol-42","date":"2026-11-09","stated attribution":"org-a"}]},
 "governance":{"gates":[{"id":"release-7","assessment":{"by":"tool-x","at":"2026-11-09"},
                         "human_authorisation":{"by":"reviewer-y","at":"2026-11-09"}}]}}
```

The three conditions are checked against one record in a single pass; the failing primitive is reported with the prefix of its term. Exit status: `0` when all three conditions hold, non-zero when at least one fails.

Boundary sentence, to be carried with every result: *a passing result means the three record-completeness conditions above are satisfied; it is not a certification, an endorsement, a verification of authenticity, or a regulatory acceptance.*

## Annex B — Reproducibility and its current limit

- The three checks in Annex A are specified above at the level of field presence and field semantics, so that an independent party can re-implement them from this document; the record format is the JSON example shown and the exit-status convention is stated with it. **No implementation of these three checks is provided in this package.** The WG2 contribution contains a checker for a different property (act-content binding) and is not an implementation of these checks. The public location of the contribution package is the contribution repository (https://github.com/zhaoxinghua09-cell/fgtida-paris-input-2026), tag v1.3.
- **Known limitation, stated rather than hidden:** the record-completeness check does not verify signature authenticity, and the external worked example cited in §5 is published material, not a pinned endpoint for this document. The checks are specified so that a third party can re-implement them; no independent party has yet done so, and no validation is claimed.

## Annex C — terminology boundaries

This annex records the boundaries that travel with the three terms, so that a
glossary entry cannot be read as a technology commitment.

- **Registry** names the record of actors, artefacts and decisions, together
  with who registered them and when. It does not introduce a new record type
  or encoding, and it does not designate a registry technology. Related
  existing work: the conferral record discussed in themes#5.
- **Evidence** is a record that a specific action occurred, carrying source,
  date and a stated attribution. It does not add a new signature requirement
  and does not introduce a grading scale; grading is discussed in themes#42
  and themes#43.
- **Gates** is the input side of a decision point. The decision and its values
  remain those of themes#60; the term does not introduce a fail-closed binary.
- **No term is claimed as novel, adopted or agreed.** The labels are offered
  for the glossary only if the group finds them useful; naming and ownership
  stay with the existing threads.
- **Checkability boundary:** the record-completeness check (Annex A) verifies that required fields are present and internally
  consistent. It does not verify signature authenticity, and a passing result
  is not a certification.
