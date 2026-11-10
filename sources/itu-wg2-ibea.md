# Binding an Action to an Accountable Actor: What a Gate Must Carry

**ITU-T FG-TIDA — Input Document for the First Meeting (Paris, 30 November – 1 December 2026)**

| Field | Value |
|---|---|
| Document type | Contribution (Input Document) |
| Proposed handling | for action |
| Agenda item | To be allocated by the FG |
| Document ID | To be assigned by TSB |
| Source | Xinghua Zhao, independent expert (China) |
| Contact | zhaoxinghua07@126.com |
| Date | 2026-11-10 (revision v0.1.1) |
| Related FG work | Terms of Reference §3.4 (Security assessment criteria and benchmarks), §4.2 (Architectures for identity, trust, agent discovery and interoperability), §4.4 (Technical-policy and machine-readable trust metadata) |
| Pages | 4–5 (estimated; typeset length to be confirmed) |
| IPR | The author asserts no IPR claim over this contribution; it is offered for the Focus Group's use under the ITU-T A.7 / ITU common patent policy. |

---

## 0. Summary

This contribution addresses one question that sits between the group's identity work and its enforcement work: **when an agent's action reaches a boundary, what must the gate be able to show so that the action can be attributed to an accountable party afterwards?**

It proposes a **three-field binding record** — *who acted*, *on whose authority*, *what changed* — with a falsifiable completeness condition for each field, and it argues that a gate which cannot produce this record after the fact is not an enforcement point but a filter. It proposes no new work item, no new mandate, and no preferred technology.

## 1. Problem statement

Identity work answers who an actor is. Enforcement work answers what a boundary will allow. Between them sits a question that neither answers alone: **when a decision at the boundary is later questioned, can the enforcing party reconstruct who acted and on whose authority?**

In current practice the two halves are often recorded in different places, at different levels of detail, by different owners. The identity layer holds a credential; the enforcement layer holds an allow/deny log; the authority relationship — the mandate conferred by a principal on an agent — is frequently held nowhere machine-readable at all. The result is an asymmetry: an action can be blocked in real time but cannot be explained afterwards, or it can be explained afterwards only by asking the deployer, which is exactly the party whose account is least independent.

## 2. Proposal: three fields a gate must carry

| Field | What it must hold | Falsifiable condition (minimal) |
|---|---|---|
| **Actor** | An identifier that resolves to a registered agent instance, with its owner and version. | A decision record whose actor identifier does not resolve to a registry entry fails. |
| **Authority** | The grant that permitted the action: grantor, grantee, scope, and the regime under which it was conferred. | A decision record with no grantor, or whose scope does not cover the action taken, fails. |
| **Effect** | What changed at the boundary: the resource, the operation, and whether the change is reversible. | A decision record naming no resource or no operation fails; an irreversible change recorded as reversible fails. |

Three properties follow, and are the reason to standardise this rather than leave it to each deployer:

1. **Reconstructability** — the three fields together are sufficient to answer "who, on whose authority, did what" without contacting the deployer.
2. **Independence from the identity mechanism** — the binding record refers to an identity, but does not prescribe how that identity is established. Any identity architecture meeting §4.2 can populate it.
3. **Machine-readability** — the record is a data structure, not a narrative log line, so that a third party's gate can consume it. This is the link to §4.4.

### 2.1 Three failure modes the record is designed to expose

- **Attribution by convention.** The deployer's log says "agent-01" and everyone agrees what that means until the day two parties disagree. Failure exposed: an identifier that resolves to nothing outside its own tenant.
- **Authority by assertion.** The agent carries a token that says it may act, and the gate accepts the token as the authority. Failure exposed: a token that shows permission but not who conferred it.
- **Effect by omission.** A gate blocks or allows without recording what the call would have changed, so a later review cannot tell a refused read from a refused write. Failure exposed: decisions that cannot be compared because their effects were never described.

## 3. Mapping to the Terms of Reference

The mapping below uses the public Terms of Reference (https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx), and refers to clause numbers rather than to Annex A item identifiers.

| ToR clause | Kind of work | What this contribution supplies |
|---|---|---|
| **§3.4** Security assessment criteria and benchmarks | Objective: criteria and benchmarks for assessing interoperability, trustworthiness and security | The three-field record as an assessment criterion: a deployment that cannot produce it after the fact scores zero on reconstructability, regardless of its real-time block rate. |
| **§4.2** Architectures for identity, trust, agent discovery and interoperability | Deliverable: architectural approaches covering identity stacks | The point at which identity architecture and enforcement architecture must join: the decision record carried by the gate. |
| **§4.4** Technical-policy and machine-readable trust metadata | Deliverable: comparative analysis of trust frameworks and machine-readable metadata | A concrete candidate for what such metadata must contain, at the field level, with a completeness condition for each field. |

Out of scope: cryptographic profile selection, PKI operational practice, and the legal characterisation of mandates. This contribution states what the record must hold, not how each field is proven.

## 4. Request to the Focus Group

| # | Request | If accepted, the FG gets | If declined or deferred |
|---|---|---|---|
| W1 | Adopt the three fields — actor, authority, effect — as the **minimum content of a gate decision record**, with the falsifiable conditions in §2. | A single content requirement that both the identity and the enforcement tracks can build against. | The fields remain a proposal in this document; the gap between identity and enforcement stays implicit. |
| W2 | State that a gate which cannot produce the record **after the fact** does not satisfy the enforcement function, however well it performs in real time. | A test that a benchmark can apply without inspecting any vendor's implementation. | Enforcement remains measured by block rate alone. |
| W3 | Indicate the **intended host** — §4.2 architecture text, §4.4 metadata analysis, or a working-group draft. | Text prepared in the right form for the second meeting (Geneva, 26–27 January 2027). | Content remains available; form is adapted once the host is known. |

## 5. Relationship to the companion contribution on Registry–Evidence–Gates

A separate input document from the same source proposes three coordination terms — Registry, Evidence, Gates — with record-completeness conditions. This contribution is the narrower, enforcement-side reading of the same idea: it does not restate the terms, and it can be read alone. Where the two overlap, the companion document governs the terminology; this document governs what a gate must emit.


**Non-duplication (ToR §2, Rec. ITU-T A.7).** This contribution does not reopen
work already under way in ITU-T SG17 or in the Focus Group. It supplies a
record-level vocabulary and check on top of the threads already published in the
FG's GitHub space; where a thread already covers a point, this document defers to
it. The Focus Group and the SG17 Chair remain the judges of whether any overlap
exists, under ToR §2.

## 6. References and attribution

- ITU-T FG-TIDA, Terms of Reference — public text at https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx (clauses §3.4, §4.2, §4.4 cited above).
- ITU-T FG-TIDA, Circular T25-TSB-CIR-0179, Geneva, 8 October 2026 — public text at https://www.itu.int/md/T25-TSB-CIR-0179/en. Its paragraph on contributions states the submission route and the 23 November 2026 deadline.
- No public repository location is asserted; no run result is claimed.

*No trademark, no DOI, no canonical identifier is asserted in this document. Views are those of the named individual expert and do not represent any organisation.*

## 7. Handling note

Submitted **for action**, no later than **23 November 2026**, in accordance with the contribution paragraph of Circular T25-TSB-CIR-0179. **Pre-registration closes on 20 November 2026** and is required for both on-site and remote participation.

---

## Annex — Decision record, as a field list

```json
{"decision":{"gate":"gw-3","at":"2026-11-09T10:12:00Z","outcome":"allow"},
 "actor":{"id":"agent-01","owner":"org-a","version":"1.2"},
 "authority":{"grantor":"principal-p","grantee":"agent-01","scope":["read:record-42"],
              "regime":"delegation-under-policy-x"},
 "effect":{"resource":"record-42","operation":"read","reversible":true}}
```

**Scope grammar.** `authority.scope` is a list of entries, each either `operation` or `operation:resource`. An entry covers the action when the operation matches exactly and, where the entry names a resource, that resource matches `effect.resource`. A scope with no matching entry fails the authority condition. The grammar is stated here in natural language; a formal grammar (ABNF or equivalent) is proposed as a next step. Resolution of `actor.id` against a registry is **assumed to exist** rather than specified here — the interface by which a gate asks a registry is a question for ToR §4.2, not a content requirement of this record.

Completeness condition, stated so a third party can apply it: a record fails if any of the three field groups is absent; if `actor.id` does not resolve to a registry entry; if no entry in `authority.scope` covers `effect.operation` under the scope grammar above, or if it names a resource other than `effect.resource`; or if `effect.reversible` is marked true for an operation declared irreversible elsewhere.

Boundary sentence: *a record satisfying this condition is complete, not correct; completeness is not a certification, an endorsement, or a regulatory acceptance.*

## Annex C — act-content binding: the record must identify the act

The three-field record answers *who acted, on whose authority, and what
changed*. One property is missing from that picture: the record can name the
operation type and the resource class without identifying **the act it
decided**, so a record can be replayed onto a different act of the same type
and no check fails.

## Definition

A decision record satisfies **act-content binding** if and only if:

1. it contains the act-describing fields of the act it decided — at minimum
   `action`, `resource`, `parameters`, `principal`, `audience` — with
   instance-level values (not class-level placeholders such as `*` or `any`);
2. it carries a digest computed over the normalized form of those fields under
   the byte rule below;
3. a verifier recomputes the digest from the fields the record presents and the
   values match;
4. an assignable label alone (for example a random UUID) is not accepted as a
   binding.

**Preconditions.** The binding is fixed at decision time, and the record is
protected (signed, or held in an append-only store). Without that anchor, a
party that can rewrite both the act and the digest will pass the check. The
property detects substitution against a pinned binding; it does not establish
record authenticity.

**Byte rule.** UTF-8 JSON object, keys in Unicode code-point order, no
insignificant whitespace; strings, integers, booleans, null, arrays and objects
are admitted; floating-point numbers are rejected, because their rendering
differs between languages.

## Check

A single-file, standard-library-only checker (`act_content_check.py`) is
provided in the contribution repository
(https://github.com/zhaoxinghua09-cell/fgtida-paris-input-2026). It ships with seven self-test vectors and
uses stable exit codes: 0 satisfied; 1 no binding object or an assignable UUID
only; 2 substitution detected (missing field, class-level placeholder, digest
mismatch); 3 value not canonicalizable (floating-point); 4 invalid JSON.

## Non-goals

The property does not cover the decision value itself (`outcome`,
`consulted`), execution identity, TOCTOU, authorization validity or evidence
quality. If the group wishes the decision value to be bound as well, that is a
separate property.
