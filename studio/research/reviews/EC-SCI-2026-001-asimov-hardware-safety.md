# EC-SCI-2026-001 — Hardware-mediated ASIMOV safety

- **Status:** SCIENCE_UNRESOLVED for a universal Asimov-law controller; bounded authorization mechanism is an engineering hypothesis
- **Target:** potential Eternal Circuit ASIMOV protocol worldbuilding; no manuscript changes
- **Reviewer:** initial synthesis; independent science adversary and quantitative reviewer not yet executed
- **Review date:** 2026-11-16
- **Local evidence:** [EC-R-2026-001](../notes/2026/EC-R-2026-001-hardware-mediated-ai-safety.md), status DRAFT; pin to this PR's merge commit after merge

## Claim decomposition

1. **Bounded claim:** A separately protected controller can deny specific unauthorized actions at fully mediated interfaces under stated hardware/software assumptions. **Plausible in principle**, supported by reference-monitor and functional-safety engineering; **not yet PASS** for any particular ASIMOV design without architecture, threat model, tests and independent review.
2. **Universal claim:** Hardware can guarantee an autonomous AI never harms humans, including indirectly or through inaction. **UNRESOLVED / not supportable on available evidence**: no generally executable harm oracle, full coverage proof or probability/assurance case.
3. **Emerging hardware AI governance:** location/workload/network verification proposals are relevant analogues but **not** demonstrations of universal action-level safety.

## Quantitative audit

See the local note's illustrative hazardous-demand calculation and correlated-failure caveat. No actual measured ASIMOV failure rate, latency, bypass rate, sensor coverage, or policy-correctness result is available; inventing one would be invalid.

## Primary adversarial objections

Incomplete mediation, impossible-to-generalize ethical predicates, out-of-band influence, compromised or misconfigured enforcement, sensor uncertainty, common-cause failures, vendor evidence limitations, and lack of independently tested deployment.

## Verdict

**SCIENCE_UNRESOLVED.** No scientific PASS; no literary gate or canon promotion. Next: choose a narrow effect boundary, measurable safety invariant, platform, threat model, formal state machine, proof/test obligations and independent verification. An author's desire for absolute safety does not override this verdict.

## Research references

| Local note ID | Version | Status | Finding |
| --- | --- | --- | --- |
| EC-R-2026-001 | Initial research PR; pin commit after merge | DRAFT | Hardware mediation is plausible for bounded actions, not universal moral guarantees |

- **Literary:** NOT_STARTED
- **Author approval:** PENDING
- **Canon:** NOT PROMOTED
