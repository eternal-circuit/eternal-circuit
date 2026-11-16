# EC-SCI-2026-004 — Idle Hands diagnostic overlap pilot

- **Status:** SCIENCE_PASS for the narrow, reversible roster-trial proposal. Standing removal remains CONDITIONAL PASS.
- **Target:** *Idle Hands* development, [The apprentice and The remote shift](../../brainstorming/the-divine-register/idle-hands.md). No approved manuscript edit.
- **Date / era:** Reviewed 2026-11-16. Fictional matched warehouse fleet in the working late-2030s to mid-2040s range. No exact year selected.
- **Reviewer:** Separate Scientific Adversary context. Shared model family and workspace. The reviewer independently reran the queue model and rechecked selected primary materials. The Evidence Verifier independently audited the source deposit. No external organization, live operation or physical experiment was involved.
- **Question:** Can a bounded learned bracket diagnosis contribute to management omitting one prospective paid overlap block, given a reversible trial and retained response?

## Mechanism and assumptions

A process photoeye can lose optical margin when a mount shifts. Record known load, bracket displacement against a stationary reference, and sensor quality during an authorized guarded observation. A versioned diagnostic derived partly from earlier operator examples packages a suspected fault for a qualified review. Ambiguous cases go to manual triage. The retained desk can order a separate isolated repair. ASIMOV permission and protective circuits remain at the site. The bracket observation cannot approve maintenance or certify the equipment as fixed.

The employer has a paid four-hour support overlap distinct from ordinary dispatch and local maintenance. It can schedule one future occurrence without the extra operator after shadow roster testing. Keep a funded overflow route or restore the overlap when demand exceeds the accepted operating conditions. The trial concerns future scheduling and makes no claim about cancelling previously committed wages. Keep the apprentice eligible for other blocks.

## Evidence and quantitative audit

| Evidence | Review finding |
| --- | --- |
| [SICK KA-09735 v1.0](https://support.sick.com/sick-knowledgebase/article/?code=KA-09735) and [OSHA 1910.147](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147) | Run quality is nonspecific and requires independent displacement evidence and known conditions. Guarded observation and hazardous-energy servicing are separate operations, with current U.S. guidance used as engineering context. |
| [Fleet-DAgger](https://proceedings.mlr.press/v205/hoque23a.html) and [PickOne/Yonder](https://www.plusonerobotics.com/automated-parcel-induction) | Feasibility analogues for bounded remote corrections and logged training inputs. Neither shows a fleet-wide diagnostic qualification, estimated service time or staffing change. |
| [Queue model](../models/idle-hands/README.md) | With one desk, the regular trace moves from 59 to 9 minutes maximum start wait while demand falls from 224 to 128 operator-minutes. The clustered trace has identical post-change work but waits 14 minutes with one desk against a 10-minute example rule. Moving one regular-family release from minute 209 to 207 yields 11 minutes, showing the small decision margin. The model checks queue entry and end-of-day completion only. |

All 256 success subsets are represented on the regular trace. Among them, 2 of 28 six-success subsets and 3 of 8 seven-success subsets meet the rule, as does the eight-success subset. Under an additional illustrative assumption that all eight conversions are independent with equal probability p on this fixed trace, rule attainment is `2p^6(1−p)^2 + 3p^7(1−p) + p^8`. It is about 0.315 at p=0.8 and 0.585 at p=0.9. The independence and equal-probability assumptions are unsupported for a real fleet. Common load, weather, maintenance or rollout can affect multiple sites together.

A diagnostic with 90% sensitivity and a 10% false-positive rate has just 50% positive predictive value when target prevalence is 10% among screened tickets. These are chosen inputs. They illustrate why accuracy alone cannot justify a four-minute review time. Repeated openings of one defective asset may inflate apparent prevalence and the data available for training. Permanent bracket redesign, a fixed diagnostic rule, false positives, delayed escalation, and the cost of standby or fallback can overturn the case for removal.

## Verdicts

| ID | Precise claim | Verdict and falsifier |
| --- | --- | --- |
| C1 | In a matched, instrumented and commissioned cell, software can flag likely load-linked flex from guarded observations and prepare evidence for qualified review, while local staff retain responsibility for the isolated repair. | **PASS** for bounded decision support. Reopen if the scene implies automatic confirmation of all lookalikes, unguarded inspection, novel manipulation, or permission to return machinery to service. |
| C2 | On the pinned regular synthetic trace, the stated service-time substitutions cross the modeled queue threshold. | **PASS** for the exact model. An independent queue replay with different outcomes would falsify the calculation. |
| C3 | This learning update justifies standing removal of overlap coverage or reliably meets a real fleet SLA. | **CONDITIONAL PASS.** Require held-out peak traces, qualified asset and fault denominators, reopen rates, full process and repair costs, service-time tails, coverage constraints and operator availability. The clustered scenario defeats any assertion based only on the mean. |
| C3a | Management can plausibly omit one upcoming four-hour paid overlap on the ordinary shift class as a reversible scheduling trial after its own shadow roster testing, while retaining core dispatch, local repair and authorized funded fallback. | **PASS** for the fictional trial decision. Do not assert actual SLA attainment, ongoing removal or a product-wide performance rate. The condition fails if no practical overflow or reinstatement route exists. |
| C4 | The present evidence supports unattended structural repair on a heterogeneous conveyor fleet. | **BLOCK** on the current record. The evidence measures unrelated bounded motions or guidance. Qualify the maintenance task, tooling, access and site safety separately before reconsidering. |

The literary referral uses C1 and C3a only. C2 informs credibility and does not appear as data in the scene. C3 and C4 stay outside scope. The parcel singulation alternative needs a fresh staffing model and is outside this referral.

## Literary gate and author decision

**READY_FOR_AUTHOR.** The separate Literary Adversary initially returned **REVISE** on `0be8637318c5c0c8ee9d114a90599cc0c01013dd`. The first draft moved too quickly from recognition to the roster and had the apprentice repeat evidence already in the ticket. In the [revised scene proposal](../../brainstorming/the-divine-register/proposals/idle-hands-the-lost-shift.md), he takes satisfaction in the useful diagnosis before opening the roster, then chooses to flag the existing unloaded comparison for the local technician and asks for an export of the posted hours. The reviewer cleared `89d9a7c418f323e31ab81c7ab2db001d55af4b89` with the scientific premises intact.

The Canon Keeper compared the proposal with the confirmed story-two placement, the existing workplace outline and the intended chronology. The early supervised repair and dock worker's acknowledgment remain the anchors. Diagnosis, local repair and lost roster hours are separate events. The exact year, workplace, disclosure and ultimate staffing decision remain author choices. The Archivist independently reproduced the 12 matrix rows and 256-subset sweep and checked the evidence pins.

Canon status **PROPOSED**. Author approval pending. The existing outline and other manuscripts were left intact.

## Durable local research references

| Note and artifact | Pinned revision | Status |
| --- | --- | --- |
| [EC-R-2026-004](../notes/2026/EC-R-2026-004-idle-hands-lost-shift.md), [executable](../models/idle-hands/queue_model.py) | Scientific review packet `d8c5837a01aeb620692c319e3a3bd800dbe89996` | DRAFT research with independent reproduction. CPython 3.13.3, `python3 studio/research/models/idle-hands/queue_model.py`. |
| EC-R-2026-004 source-fidelity clarification | `a84b722dfa75e78dd71ebe69a27f1adad3f55156` | Primary-source links and supervisor scope clarified. Model unchanged. |
