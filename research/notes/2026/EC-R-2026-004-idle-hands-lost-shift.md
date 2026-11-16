# EC-R-2026-004 — Can one learned conveyor fault cost a shift?

- **ID:** EC-R-2026-004
- **Status:** DRAFT research deposit. No story premise is promoted.
- **Topics:** remote intervention, robot learning, process sensing, exception queues, staffing
- **Prepared by:** Codex with distinct Frontier Scout, Evidence Verifier, and Quantitative Modeler contexts
- **Created / sources inspected (UTC):** 2026-11-16
- **Applicable claims:** EC-SCI-2026-004, *Idle Hands* apprentice and remote conveyor queue
- **Source snapshot:** Versions and access date below
- **Preservation:** Original analysis and executable model. No third-party text or data reproduced.

## Executive finding

In the *Idle Hands* outline, an apprentice learns to diagnose a flexing conveyor sensor bracket. His remote sessions later become training inputs, and eventually the system resolves a familiar ticket locally. Existing experiments and products support parts of this sequence. Identical robot arms have learned a shared, tightly constrained policy from remote corrections across two labs. Commercial parcel cells use logged operator selections to guide low-confidence picks. A process photoeye can expose received-light quality, which can vary when its mount moves. The evidence does not establish unattended mechanical repair across sites or how much operator work this particular fault would remove.

The strongest bracket-preserving design restricts automation to a bounded diagnosis on commissioned equipment. The system identifies a familiar pattern under guarded observation, packages it for review and opens a separate local maintenance ticket. A staffed coverage reduction is a further decision. In a synthetic dispatch trace, replacing eight sixteen-minute diagnostics with four-minute reviews reduced work by 96 operator-minutes. That made a four-hour paid overlap removable under a ten-minute queue-start rule. Keeping the same work and moving arrivals into bursts still required the overlap. The model demonstrates a scheduling mechanism and its failure case. Neither the trace nor present robotics results supplies the prevalence, site-transfer performance, or roster evidence needed to predict that this shift would disappear.

## Technical account

### Problem and mechanism

**Original candidate.** A common family of conveyor stations across a remote-support fleet has a load-sensitive offset of a bracket carrying a non-safety process photoeye. The early in-person repair is an isolated physical job. A later remote session can capture synchronized guarded load-test observations, process state and camera/measurement evidence, plus operator decisions and an inspected outcome. Capture all dispositions, including inconclusive tests and reopens. A recording of a successful session alone omits how to reject lookalikes.

**Bracket-preserving variant.** Commission each station for a supported sensor, mount and observable load regime. Use a fixed camera or displacement channel against a fixed reference, received-light quality, and load/time registration. Repeated load-synchronous bracket displacement plus a light-margin drop is evidence for the candidate fault. Contamination, ordinary beam occlusion, camera movement, electrical intermittency, reflector angle and shared vibration can produce misleading traces. Compare with unloaded reference and hold out whole units, days and fault families. The diagnostics system can select a preapproved guarded test or observe an already permitted cycle. It stays outside the local interlock logic and may not authorize guard bypass, human entry or a novel repair. Any actual work inside the hazard zone uses a separate local work order and site isolation process. A remote diagnostic ticket closure is distinct from confirming the conveyor repaired. The proposed deployment has a retained remote reviewer and site technicians.

**Learning and failure attribution.** Version the selected demonstrations, benchmark the learned selector against a scripted comparison of telemetry and observed displacement, validate held-out units, and deploy only the commissioned envelope. A learned scorer can propose a test or rank a hypothesis alongside a fixed fallback. Interlocks stay local. If a simpler programmed test finds the same fault as reliably, the company can still extract the apprentice's procedure from the recordings, but the story cannot claim that a learning algorithm was indispensable. The release records or fleet lead can corroborate that his sessions contributed. One familiar motion, by itself, cannot prove provenance. A lasting fleet recurrence requires an installed population of comparable units and a reason replacement or redesign has not already eliminated the problem. Count original incidents and reopens separately.

**Alternate fault, if needed.** An overlapping parcel or low-confidence pick in a standardized guarded induction cell has a closer commercial precedent for remote guidance and subsequent local resolution. It preserves the early bracket repair and the conveyor setting while changing the later reveal. Service and arrival inputs must be re-estimated for parcel exceptions. The bracket-oriented staffing inputs cannot be imported as evidence for that alternative.

### Method, source results and limits

| Evidence inspected | Reconstructable result | Inference boundary |
| --- | --- | --- |
| Hoque et al., Fleet-DAgger §6.3 | Four identical ABB YuMi arms at two labs, two remote operators, and four discrete pushing actions. Physical batches had 250 action slots per arm, three random seeds per method, and 375 original image/action training examples augmented tenfold. Physical resets still needed human work. | Supports bounded sharing of corrections across matching hardware. The larger 100-robot evaluation used simulation with algorithmic supervisors. No physical staffing multiplier or maintenance skill transfer follows. |
| Physical Intelligence, RECAP v2 §VI-C2 and Appendix E | Box assembly evaluated iterative training over two rounds. Main text reports 600 autonomous and 360 expert-intervention trials each round. Appendix E calls the 600 demonstrations, so the type label remains ambiguous. The paper reports about 2× throughput after round two and about 90% success for the folding and labeling stages within a 600 s budget. Final stacking still failed in some trials. | Scoped developer result with other training inputs and physical trials. No staffing logs or evidence for learning the bracket procedure. |
| Li et al., Robin §VI Table II | In the authors' production comparison, Reported failures were 4,444 of 89,162 baseline and 3,427 of 90,127 experimental picks. The published experimental success count disagrees with its totals. See the audit immediately below. | A pick-ranking comparison in parcel induction with collision-checked candidates. A failed pick is not a staffed ticket. |
| Physical Intelligence, π0.7 §IX-C | Reported 80% shirt-folding success on a bimanual UR5e with no folding training data from that embodiment, versus 80.6% across tests with ten experienced teleoperators new to that task and setup. | Positive bounded transfer. About one in five policy trials still failed on that task. No fault diagnosis or unattended service claim. |
| Plus One Robotics, PickOne/Yonder operating description | Low-confidence frames can go to a remote operator who selects an item. The vendor describes saving the response for machine learning and using local placement feedback. | Direct analogous workflow. The public product description supplies no audited causal staffing or recurrence series. |
| SICK RAY26 KA-09735 v1.0 | Run quality is received light divided by light at the teach reference, expressed in percent. Mount vibration, alignment, angle, damage and contamination are named factors. | Supports the optical channel and confounds for a process sensor. It does not validate load-linked bracket diagnosis or the proposed sensor combination. |
| Papallas and Dogar, §VI-C | In the virtual 20-robot comparison, one method elicited human input for 307 of 1,000 problems versus 175 for its baseline while improving task metrics. The timing gain diminished at 30 robots. | Counterexample to using higher success as a proxy for less human work. The intervention is high-level and the pooled fleet result is simulated. |

Robin Table II lists 90,127 experimental picks, 87,700 successes, 3,427 failures and 96.20% success. The success and failure counts sum to 91,127, so at least one entry is wrong. The experimental total and count of failures imply 3.80% failure, matching the printed 96.20% success rate and the authors’ roughly 24% relative failure reduction against baseline. The raw data were unavailable. Treat the magnitude as the authors’ internally qualified estimate, not as an input to the staffing model.

### Quantitative results and reproducibility

The original dispatch model is in [research/models/idle-hands](../../models/idle-hands/). It uses one synthetic 480-minute day, one core dispatcher, an optional 240-minute paid overlap, an illustrative maximum ten-minute wait to **start remote work**, eight eligible tasks, and eight unrelated ones. Each eligible task consumes 16 minutes with manual diagnosis or 4 minutes for validation after a successful classifier shortcut. Each unrelated task consumes 12 minutes. With the assumptions fixed, labor demand drops from 224 to 128 operator-minutes, since 8 × (16 − 4) = 96. Maximum wait on the baseline trace with one dispatcher is 59 minutes. The overlap reduces it to 2 minutes. On that trace, the shortened work meets the rule with one dispatcher at 9 minutes. The same post-update workload on a clustered trace yields 14 minutes with one dispatcher and 3 with the overlay. The clustered manual baseline already passed with the overlay at 10 minutes, so this directly shows that equal workload savings can leave the overlay necessary.

The subset sweep varies which eligible calls get shortened, then replays dispatch. On the baseline trace there are successful allocations at 6/8 shortened tickets (2 of 28 subsets) and at 7/8 (3 of 8). All eight shortened calls meet the target for the single 8/8 subset. These are scenario counts, and subsets are not equally likely in a fleet. Waiting time is neither total restoration time nor a safety limit. The work decrease supports a larger paid-hours change only under the explicit assumption that management purchases scheduled coverage in blocks and can remove the optional block. An error may create extra escalations, correlated failures can overload the desk, and fixed coverage or redundancy obligations can make the block nonremovable. Compare peak waits, fallback utilization, reopens and paid shifts during shadow and trial periods before reconsidering a cut.

### Limitations and relevance to Eternal Circuit

No access to historical ticket traces, deployment success rates, multi-site safety test logs or any employer's roster. There is no trained bracket-diagnosis system here. Review the mechanical failure recurrence, fleet mix, validation workload and who pays for local repair separately. A field evaluation needs timestamps, site and asset IDs, duplicate/reopen flags, hands-on operator and local maintenance durations, guard trips, classified failures, shift rules and shared shocks. Include bases and denominators by site and peak period. Replay the same held-out arrivals with and without the changed skill, and compare against queue, recovery, safety and business requirements. The original branch of the story remains open. If only task handling is demonstrated, the ticket can close faster and shifts can remain for bursts. If a roster cut is supported, it is the apprentice's paid remote overlap, with remaining core response and local technicians.

## Source and provenance ledger

| Type | Original source | Version or persistent identifier | Accessed UTC | Quality/limit |
| --- | --- | --- | --- | --- |
| Published original study | [Hoque et al., Fleet-DAgger](https://proceedings.mlr.press/v205/hoque23a.html) | CoRL 2022, PMLR 205:368–380 (2023) | 2026-11-16 | Separate physical and simulated experiments |
| Original preprint | [Physical Intelligence, π*0.6](https://arxiv.org/html/2511.14759v2) | arXiv:2511.14759v2, 2025-11 | 2026-11-16 | Developer task evaluation, site transfer unspecified |
| Original preprint | [Physical Intelligence, π0.7](https://arxiv.org/html/2604.15483v1) | arXiv:2604.15483v1, 2026-04 | 2026-11-16 | Developer cross-embodiment task test |
| Published original study | [Li et al., large-scale package manipulation](https://roboticsproceedings.org/rss19/p023.pdf) | RSS 2023, DOI 10.15607/RSS.2023.XIX.023 | 2026-11-16 | Operator-authored production pick comparison |
| First-party product description | [Plus One Robotics, Automated Parcel Induction](https://www.plusonerobotics.com/automated-parcel-induction) | Living page | 2026-11-16 | Interface description, no measured staffing result |
| First-party sensor manual note | [SICK, RAY26 Quality of Run](https://support.sick.com/sick-knowledgebase/article/?code=KA-09735) | KA-09735 v1.0 | 2026-11-16 | Process measurement and confounds |
| Published original study, accepted version | [Papallas and Dogar, To ask for help or not to ask](https://eprints.whiterose.ac.uk/id/eprint/189268/1/root.pdf) | IROS 2022, White Rose record 189268 | 2026-11-16 | Virtual fleet result, distinct assistance task |
| U.S. regulator source | [OSHA, control of hazardous energy](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147) | 29 CFR §1910.147 | 2026-11-16 | Engineering context for separating diagnostic observation from servicing. Future site and jurisdiction remain open. |

The scout and verifier independently inspected primary sources and reported convergent limits. No direct X scan, industry data access, or independent reproduction of the robotics studies. The numerical model is the original evidence that can be rerun locally.

## Local evidence and reconstruction

A single monitored process photoeye and an independently observable mounting reference can supply complementary signals. Use held-out known fault and lookalike cases to check whether their combination is specific enough and retain local maintenance on unsafe or unknown states. Then run the paired queue using identical arrivals and change only service times and staffing. A cluster at one minute is sufficient to show why a mean cannot determine a coverage decision. All example input parameters are synthetic.

## Related records

- [Idle Hands development outline](../../../brainstorming/the-divine-register/idle-hands.md)
- [ASIMOV indexed-axis deposit](EC-R-2026-002-asimov-indexed-axis.md)
- [EC-SCI-2026-004](../../reviews/EC-SCI-2026-004-idle-hands-lost-shift.md)

## Revision history

- 2026-11-16 — Initial primary-source synthesis and original staffing counterfactual.
