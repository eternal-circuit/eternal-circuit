# Reproducible results

Run the [README commands](README.md) from the repository root. The recorded run used CPython 3.13.3 on macOS. Five tests passed, including simulator/model agreement on all 756 integer transition inputs, threshold checks, malformed and oversized input, and explicit fault cases. The repository had no pre-existing executable test suite or CI test workflow at the base revision.

The finite checker independently visits reachable states by breadth-first search. It distinguishes three request classes, three integer errors, two excursion margins and two health classes, for 36 input combinations per settled state. Missing and stale samples are equivalent to inhibit for the position transition; separate tests verify those rejection paths in the implementation. No fairness or input distribution assumption is needed.

| Initial set | Reachable settled positions (mm) | Input-labelled transitions checked | Interval violations |
| --- | --- | ---: | ---: |
| {10} | 1–19 inclusive | 684 | 0 |
| All integers 0–20 | 0–20 inclusive | 756 | 0 |

A run with nominal unbiased sensing advanced from 10 mm to 18 mm on eight positive requests. It refused three more positive requests, refused one malformed request, and authorized one negative request to 17 mm. The checker can reach 19 mm with admissible nonzero measurement error, so the nominal settled limit of 18 mm is not a general bound on settled position.

## Fault injection

| Fixture | Decision | Settled position (mm) | Path bounds (mm) | Interpretation |
| --- | --- | ---: | --- | --- |
| Missing sample, 6 ms stale sample, or watchdog inhibits | Refused | 10 | [10,10] | Known invalid state holds in the model. |
| −10 mm sensor bias at x=20 mm | Accepted | 21 | [19,22] | A fresh-looking false sample permits an unsafe endpoint. The initial state is a safe boundary state, separate from the nominal run. |
| 4 mm excursion at x=17 mm | Accepted | 18 | [13,22] | The fault model admits a continuous trajectory through 22 mm. A safe endpoint and a controller permit are compatible with unsafe transient motion. |
| Alternate drive path at x=20 mm | Refused | 21 | [19,22] | The test fixture applies motion despite rejection to expose the complete-mediation dependency. |

Path bounds are overapproximations produced by the plant contract. A bound extending outside the envelope admits an unsafe trajectory; it does not report a measured peak. The deterministic exercise is a comparison of assumptions, not a sample of real-world fault rates. The program does not model cryptographic authentication, real time, memory isolation, independent power, brake physics or physical configuration. An unfinished input line can stall processing; the simulator has no liveness or deadline guarantee.

The theorem for real-valued paths is in the [safety case](SAFETY_CASE.md). Exhaustive enumeration validates the discrete model only. Neither the finite check nor the tests support physical certification.
