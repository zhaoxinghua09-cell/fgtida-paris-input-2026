# FG-TIDA Use Case Proposals (3) — Delegated Authority, Gated Update, Mid-Session Revocation

**ITU-T FG-TIDA — Input Document for the First Meeting (Paris, 30 November – 1 December 2026)**

| Field | Value |
|---|---|
| Document type | Contribution (Input Document) — use-case proposals |
| Proposed handling | for action |
| Agenda item | To be allocated by the FG |
| Document ID | To be assigned by TSB |
| Source | Xinghua Zhao, independent expert (China) |
| Contact | zhaoxinghua07@126.com |
| Date | 2026-11-10 (revision v0.1.1) |
| Related FG work | Terms of Reference §3.3 (Use cases), §4.1 (Use cases and requirements analysis) |
| Pages | 6–7 (estimated; typeset length to be confirmed) |
| IPR | To be completed per the ITU-T FG contribution template |

> Each proposal below follows the field structure of the FG's `FG-TIDA Use Case Proposal` template, so that it can be entered in the use-case register without restructuring. Fields the template requires are all completed; where a field does not apply, the reason is stated rather than left blank.

## What is asked of the FG

1. **Enter these three proposals in the use-case register**, one entry per proposal, attributed to this contribution.
2. **Use them for requirements analysis under ToR §4.1**, since each yields five requirements already phrased as requirements rather than as narrative.
3. **Indicate which theme each case should be mapped to**, where the group's theme taxonomy is settled; the primary theme is marked per proposal, and the others are marked as exercised.

**On form:** every requirement below is stated as content, not as syntax. Each is expected to be satisfied by instantiating mechanisms that already exist — credentials, tokens, signed logs, status lists — rather than by defining a new data structure. Where a requirement needs a machine-readable form, that form is a candidate for the group's metadata work (ToR §4.4), not a proposal here.

---

# Proposal 1 — A delegated agent reads a patient record to prepare an external lab referral

## 1. Identification

- **Title:** Delegated record read for an external lab referral
- **Submitting organization:** Independent expert (China) — individual submission, no organisation represented
- **Contact name:** Xinghua Zhao
- **Contact email:** zhaoxinghua07@126.com
- **Sector:** Health *(primary)*; Other: cross-organisational clinical data exchange

## 2. The situation

**Plain language description (≤3 sentences):** A hospital clinician authorises an agent to read one patient's record so that a referral to an external laboratory can be prepared. The laboratory must decide whether to accept the referral prepared by an agent it has never dealt with. Today it accepts on the strength of the hospital's letterhead, not on anything the agent can show.

- **Actor:** the clinician (principal), the hospital's agent (acting), the external laboratory (relying party), the laboratory's own intake system.
- **Action:** read one identified record; compose a referral package; transmit it.
- **Decision required:** *"May this hospital's agent be relied upon to have read the record it cites, on this clinician's authority, for this patient?"*
- **Problem encountered:** the referral carries a clinician signature on paper and an agent identifier in a header; nothing binds the two.
- **Current mitigation:** bilateral contracts plus manual call-back verification, which fails outside business hours.
- **Residual gap:** the relying party cannot distinguish an agent acting under a valid delegation from one repeating a stale or exceeded delegation.

## 3. Actors and context

**Taxonomy roles involved:** Principal ✔ / Relying party ✔ / Deployer–Owner ✔ / Agent instance ✔ / User ✔ / Attestor ✔

**Mandates in this case**

| Grantor | Grantee | What is conferred | Governing regime |
|---|---|---|---|
| Clinician | Hospital agent | Read one identified patient record; compose a referral | Clinical delegation under hospital policy |
| Hospital | Laboratory | Accept referrals prepared with delegated agent assistance | Bilateral service agreement |
| Laboratory | Intake system | Admit the referral into the queue | Internal operating procedure |

**Cross-border?** No — single jurisdiction in this instance; a cross-border variant is noted under §7.
**Embodied?** No.
**Agent action type:** Read-only ✔ (the consequential act, transmission, is performed by the hospital system, not the agent).
**Crosses organisational boundary?** Yes — hospital to external laboratory.
**Risk level:** High.

## 4. Theme relevance

| Theme | Yes | Primary | Justification |
|---|---|---|---|
| Dynamic Identity | ✔ | | The agent's eligibility changes with each patient authorisation. |
| Continuous Trust and Attestation | ✔ | | The laboratory needs ongoing evidence, not a one-time credential. |
| Delegation | ✔ | ✔ | The entire case is about a mandate conferred, bounded, and relied upon. |
| Discovery and Cross-Border Trust | ✔ | | The laboratory has no prior relationship with the agent. |
| Runtime Enforcement (Control Plane) | ✔ | | The boundary decision is made at the laboratory's intake. |
| Embodied AI Identity and Trust | | | Not applicable — no physical actuation. |

**Related theme proposals:** none linked at submission time.

## 5. Requirements

| # | Type | Requirement description | Criticality |
|---|---|---|---|
| 1 | Technical | The referral must carry a machine-readable statement of who conferred the read authority, on whom, and for which record. | Must |
| 2 | Technical | The relying party must be able to check that the cited record identifier matches the record actually read. | Must |
| 3 | Technical | Expiry and scope of the delegation must be checkable without contacting the clinician. | Must |
| 4 | Business | A refused referral must be explainable to the patient in plain language. | Should |
| 5 | Legal | The delegation record must be retained for the period the clinical record is retained. | Must |

## 6. Assessment criteria

- **Success criteria:** the laboratory can answer §2's decision question from the referral package alone, with no call-back.
- **Measurable metric:** proportion of referrals admitted without human verification, and proportion of later disputes resolved from the package alone.

## 7. Duplication check

- **Existing standards or SDOs:** W3C Verifiable Credentials (credential presentation); ISO/IEC 24760 (identity framework); ITU-T SG17 identity management work; HL7 FHIR for the clinical payload.
- **Overlap notes:** these define how a credential is issued and how clinical data is structured. None of them define what a gate must record about the *delegation* at the moment it admits a referral, which is the gap this case targets.

## 8. Maturity

- **Pilot status:** Hypothetical.
- **Reference implementation:** n/a.

## 9. IP and confidentiality

- **Confidentiality level:** Public. No patient data is described; the case is structural.
- **IP notes:** none.

## 10. Assets

- **Link to assets:** none. Dataset ✗ / Code ✗ / Protocol ✗.
- **IP notes:** none asserted.

---

# Proposal 2 — A model update is held until an assessment and a human authorisation are recorded

## 1. Identification

- **Title:** Gated model update in a regulated device workflow
- **Submitting organization:** Independent expert (China) — individual submission, no organisation represented
- **Contact name:** Xinghua Zhao
- **Contact email:** zhaoxinghua07@126.com
- **Sector:** Health *(primary)*; Other: regulated software lifecycle

## 2. The situation

**Plain language description (≤3 sentences):** A vendor proposes a new model version for a device already in clinical use. The change may not take effect until the assessment is recorded and a named person authorises it. Today that control lives in a change-management system that the device itself never sees.

- **Actor:** the vendor's engineering team, the vendor's release agent, the quality reviewer (principal for the authorisation), the deploying hospital.
- **Action:** replace the deployed model version with a new one.
- **Decision required:** *"Was this change assessed and authorised by an accountable person before it reached patients?"*
- **Problem encountered:** the device can report which model it runs, but not who decided that this model may run.
- **Current mitigation:** change tickets and periodic audit, which reconstruct the decision days later.
- **Residual gap:** a model swapped outside the ticket system leaves no trace the device can show.

## 3. Actors and context

**Taxonomy roles involved:** Principal ✔ / Relying party ✔ / Builder ✔ / Deployer–Owner ✔ / Agent instance ✔ / Attestor ✔

**Mandates in this case**

| Grantor | Grantee | What is conferred | Governing regime |
|---|---|---|---|
| Quality reviewer | Release agent | Execute the model replacement after assessment | Internal quality procedure under device regulation |
| Vendor | Deploying hospital | Supply the updated model with its assessment record | Supply agreement |
| Hospital | Clinical system | Accept the new version into use | Local clinical governance |

**Cross-border?** Yes — vendor and hospital in different jurisdictions in the common case.
**Embodied?** No.
**Agent action type:** Irreversible in effect (a superseded model version cannot be un-run on decisions already made).
**Crosses organisational boundary?** Yes.
**Risk level:** High.

## 4. Theme relevance

| Theme | Yes | Primary | Justification |
|---|---|---|---|
| Dynamic Identity | ✔ | | The release agent's authority is scoped to one change. |
| Continuous Trust and Attestation | ✔ | | The assessment is evidence that must survive the change. |
| Delegation | ✔ | | A named reviewer confers the right to act. |
| Discovery and Cross-Border Trust | ✔ | | Vendor and hospital do not share an authority chain. |
| Runtime Enforcement (Control Plane) | ✔ | ✔ | The gate is the point where the change is held until conditions are met. |
| Embodied AI Identity and Trust | | | Not applicable. |

**Related theme proposals:** none linked at submission time.

## 5. Requirements

| # | Type | Requirement description | Criticality |
|---|---|---|---|
| 1 | Technical | The device must be able to show, after the fact, the assessment and the authorising person for its current model. | Must |
| 2 | Technical | A version change with no recorded authorisation must be detectable by the device, not only by the vendor. | Must |
| 3 | Technical | Authorisation records must be immutable once written. | Must |
| 4 | Business | Rollback must be possible without erasing the record of the change that is being rolled back. | Should |
| 5 | Legal | Records must satisfy the retention rules of both jurisdictions involved. | Must |

## 6. Assessment criteria

- **Success criteria:** the decision question in §2 is answerable from the device, offline, with no vendor access.
- **Measurable metric:** count of version changes for which the authorisation record is missing or non-immutable.

## 7. Duplication check

- **Existing standards or SDOs:** IEC 62304 (software lifecycle); ISO 13485 (quality management); FDA premarket change protocols; ITU-T SG17 security assessment work.
- **Overlap notes:** these govern the process of change control. None specifies what the *device itself* must be able to show about the authorisation, which is the gap here.

## 8. Maturity

- **Pilot status:** Hypothetical.
- **Reference implementation:** n/a.

## 9. IP and confidentiality

- **Confidentiality level:** Public.
- **IP notes:** none.

## 10. Assets

- **Link to assets:** none.
- **IP notes:** none asserted.

---

# Proposal 3 — An agent's authority is revoked mid-session at a visited network

## 1. Identification

- **Title:** Mid-session revocation of a roaming agent's authority
- **Submitting organization:** Independent expert (China) — individual submission, no organisation represented
- **Contact name:** Xinghua Zhao
- **Contact email:** zhaoxinghua07@126.com
- **Sector:** Telecom *(primary)*

## 2. The situation

**Plain language description (≤3 sentences):** A user's agent is serving a session on a visited network abroad when the user withdraws its authority. The visited network must stop honouring the agent immediately, but it has no relationship with the authority that granted it. Today revocation propagates as a signed instruction that the visited network may receive late or not at all.

- **Actor:** the user (principal), the agent, the home operator (grantor), the visited network (relying party).
- **Action:** continue an in-progress session, and any resource operations within it.
- **Decision required:** *"Is this agent still entitled to act for this user, at this moment, on this network?"*
- **Problem encountered:** entitlement was checked at session start; the session outlives the entitlement.
- **Current mitigation:** session timeouts and periodic re-authentication, which are not the same as revocation.
- **Residual gap:** a revoked agent can keep acting until the next re-authentication boundary.

## 3. Actors and context

**Taxonomy roles involved:** Principal ✔ / Relying party ✔ / Deployer–Owner ✔ / Agent instance ✔ / Infra provider ✔ / Attestor ✔

**Mandates in this case**

| Grantor | Grantee | What is conferred | Governing regime |
|---|---|---|---|
| User | Agent | Act for the user within a declared scope | Consumer consent under national telecom rules |
| Home operator | Agent | Authenticate to the visited network | Roaming agreement |
| Visited network | Agent | Use of local resources for the session | Local licensing conditions |

**Cross-border?** Yes — home and visited jurisdictions differ.
**Embodied?** No.
**Agent action type:** Consequential (reversible) for resource use; irreversible for any disclosure already made.
**Crosses organisational boundary?** Yes.
**Risk level:** Medium.

## 4. Theme relevance

| Theme | Yes | Primary | Justification |
|---|---|---|---|
| Dynamic Identity | ✔ | ✔ | The question is whether an identity claim is still valid now, not whether it was valid at session start. |
| Continuous Trust and Attestation | ✔ | | Revocation is a continuous-state problem, not a one-time check. |
| Delegation | ✔ | | The user's mandate is the thing being withdrawn. |
| Discovery and Cross-Border Trust | ✔ | | The relying party has no direct relationship with the grantor. |
| Runtime Enforcement (Control Plane) | ✔ | | The visited network is the enforcement point. |
| Embodied AI Identity and Trust | | | Not applicable. |

**Related theme proposals:** none linked at submission time.

## 5. Requirements

| # | Type | Requirement description | Criticality |
|---|---|---|---|
| 1 | Technical | The relying party must be able to learn of a revocation within a bounded interval, stated as a number. | Must |
| 2 | Technical | A revoked agent's subsequent operations must fail closed, not open. | Must |
| 3 | Technical | The relying party must be able to show, after the fact, whether it knew of the revocation at the time it acted. | Must |
| 4 | Business | The user must be able to tell, in plain language, what the agent did before revocation took effect. | Should |
| 5 | Legal | Records of revocation and of actions taken after it must satisfy both jurisdictions' evidentiary rules. | Must |

## 6. Assessment criteria

- **Success criteria:** no operation by a revoked agent succeeds beyond the declared interval.
- **Measurable metric:** maximum observed delay between revocation and first refused operation, per roaming pair.

## 7. Duplication check

- **Existing standards or SDOs:** 3GPP authentication and key agreement; OAuth 2.0 token revocation; W3C Verifiable Credentials status lists; GSMA roaming agreements.
- **Overlap notes:** these define revocation mechanics within one domain. None defines what the *visited* network must record to show that it acted on a revocation it had received — the after-the-fact half of this case.

## 8. Maturity

- **Pilot status:** Hypothetical.
- **Reference implementation:** n/a.

## 9. IP and confidentiality

- **Confidentiality level:** Public.
- **IP notes:** none.

## 10. Assets

- **Link to assets:** none.
- **IP notes:** none asserted.

---

## Annex — Why these three, together

The three cases are chosen to be separable and complementary: one tests **delegation** at the moment of admission (Proposal 1), one tests **enforcement** at the moment of change (Proposal 2), and one tests **identity validity** after the moment of admission (Proposal 3). Each yields requirements that can be entered independently; entered together, they cover the admission, change and revocation ends of one lifecycle.

## Handling note

Submitted **for action**, no later than **23 November 2026**, in accordance with the contribution paragraph of Circular T25-TSB-CIR-0179. **Pre-registration closes on 20 November 2026** and is required for both on-site and remote participation.

*No trademark, no DOI, no canonical identifier is asserted. Views are those of the named individual expert; no organisation is represented.*
