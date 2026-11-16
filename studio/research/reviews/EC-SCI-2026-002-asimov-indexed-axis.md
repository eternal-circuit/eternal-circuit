# EC-SCI-2026-002 — Indexed-axis ASIMOV proof-of-concept

- **Status:** SCIENCE_UNRESOLVED for the reference hardware mechanism.
- **Target:** Noncanonical guarded horizontal bench stage for contemporary engineering research. No story passage is under review.
- **Reviewed revision:** `15fcaa8c82aaf8d606740985f7c4aaaf093fd12e` (reviewed simulator and formal-checker files unchanged from the working tree inspected by the adversary).
- **Review date:** 2026-11-16.
- **Reviewer:** Separate Scientific Adversary agent. It shared the model family and workspace with the implementation agent, used its own review context, inspected the implementation, independently reran the checks and challenged the parser. No external laboratory, hardware testing or full research-source fidelity review.
- **Question:** Can independent mediation enforce the 0–20 mm axis envelope under explicit observable and physical bounds?

## Mechanism and assumptions

Only the mediator may commit a ±1 mm stroke after checking sample validity and the geometric reserve. A held carriage is stationary at initialization, on refusal and between strokes. Position error at commit is at most 1 mm, and the stroke remains in the interval joining the true start and nominal endpoint padded by at most 1 mm. The simulator trusts its runtime and fixture configuration and exposes only request bytes to the planner. The threat model and safety case inventory the assumptions to validate on a physical stage.

## Source ledger

| Source | Date | Type | Evidence and limitations |
| --- | --- | --- | --- |
| [NIST SP 800-160 v1r1, §D.4.2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf) | 2022 | Primary guidance independently rechecked | Reference-validation design criteria. No evidence about this actuator or prototype. |
| [HSE Control systems, Independence](https://www.hse.gov.uk/comah/sragtech/techmeascontsyst.htm) | Undated, checked 2026-11-16 | Regulator guidance independently rechecked | Dependencies include shared utilities, installation and maintenance. No measured common-cause rate. |
| [Local checker](../../experiments/asimov/formal/check.py) and [tests](../../experiments/asimov/tests/test_asimov.py) | 2026-11-16 | Original model and executed code | Independent rerun, finite abstraction only. |

## Quantitative audit and falsifiers

The ±1 mm sensor error translates the ideal stroke interval by at most 1 mm. Padding by 2 mm covers that translation plus the 1 mm excursion bound. Rejections preserve the current state. The independent rerun found 684/756 nominal transitions with zero violations in the respective initial sets and five passing automated tests. The reviewer also exercised every two-byte stream via the parser and a 1 MiB oversized line with a valid-looking suffix followed by a distinct valid line. An unending input line can stall processing, so there is no availability or deadline verdict.

The proof assumes the difficult physical obligations. At 0.2 m/s, a 5 ms reaction delay and 2 m/s² guaranteed braking imply 1 mm latency travel and 10 mm braking travel. This is an illustrative counterexample to substituting a fresh sample for a stop bound. A bias or bypass fixture settles at 21 mm. The excursion fixture admits a path to 22 mm while settling at 18 mm. The path bound is not a measured peak.

## Verdicts

| ID and testable proposition | Verdict | Falsifier or reopening condition |
| --- | --- | --- |
| C1. Under the settled-axis and mediation contracts, the guard preserves the continuous 0–20 mm position invariant on arbitrary request sequences. | **PASS** | A trajectory obeying all stated contracts that leaves the envelope would falsify the proof. Altered contracts require review. |
| C2. In the nominal simulator with trusted runtime/harness, the stdin byte interface cannot apply a stroke absent the authorization decision. | **PASS** | Produce a byte-only bypass under the pinned runtime assumptions. A hostile same-user OS process and trusted fault fixtures are outside this proposition. |
| C3. The proposed physical MCU, drive and independent supervisor integration can satisfy the same position invariant in its declared operating and fault domain. | **UNRESOLVED** | Validate position at commit, stationary holding, worst-case trajectory and fault braking, independence and every effect path. No measured failure probability or physical clearance. |
| C4. Hardware isolation alone guarantees general human safety. | **BLOCK** | An isolated controller can faithfully enforce an incorrect policy, accept wrong observations or leave relevant effects unmediated. A narrower hardware claim would require a new dossier. |

C1 and C2 pass only at their stated abstraction boundaries. The architecture as a physical mechanism remains unresolved. Reopen on measured hardware evidence or a changed assumption, threshold or implementation. Sources checked through 2026-11-16 within the scope above.

## Literary gate

**NOT_STARTED.** The physical mechanism lacks scientific PASS.

## Canon decision

Author approval pending. Research feature branch `studio/research/asimov-reference-prototype`. No canon destination proposed.

## Durable local research references

| Note | Pinned revision | Status | Finding |
| --- | --- | --- | --- |
| [EC-R-2026-001](../notes/2026/EC-R-2026-001-hardware-mediated-ai-safety.md) | `34e9e184f941711725cb3901b3b3ffcf966b3c76` | DRAFT | Foundations and limitations of hardware-mediated authorization |
| [EC-R-2026-002](../notes/2026/EC-R-2026-002-asimov-indexed-axis.md) | `15fcaa8c82aaf8d606740985f7c4aaaf093fd12e` | DRAFT | Interval proof, finite check, fault outcomes and hardware source ledger |
