# EC-R-2026-002 — Bounded authorization for an indexed axis

- **ID:** EC-R-2026-002
- **Status:** DRAFT. Separate adversarial model/software review completed. Independent research-source fidelity review and physical validation remain open.
- **Topics:** ASIMOV, complete mediation, forward invariance, safe motion, hardware trust roots
- **Prepared by:** Codex. Scientific adversary scope and findings are in the companion dossier.
- **Created / sources checked (UTC):** 2026-11-16
- **Applicable claims:** EC-SCI-2026-002 C1–C4
- **Source snapshot:** Versions in ledger below. Software and note revision pinned by the dossier.
- **Preservation:** Original analysis and code only. Third-party sources are summarized.

## Executive finding

A single guarded horizontal carriage provides a bounded test of the ASIMOV hypothesis. The planner can request either direction but cannot choose position, speed, credentials or power. A separate decision rule reserves space for both sensor error at commit and physical excursion during the stroke. If all motion passes through the gate, position is held between strokes, and a validated plant respects the reserved bounds, the position invariant follows by interval containment and induction for arbitrary sequences of requests. This is a result about the complete physical trace in an assumed mathematical model.

A separate finite transition enumerator visited 19 reachable integer states from the demonstration start and checked 684 input-labelled transitions. From every safe integer start it checked 756 transitions. No nominal transition exceeded the envelope. The executable simulator agreed on all 756 cases and rejected missing/stale measurements and an inhibit. Deliberate sensor bias and a bypass produced out-of-bounds endpoints. Excess excursion admitted an out-of-bounds path despite a safe endpoint. The strongest limitation is that the proof presumes bounds on sensing, holding and travel that must be justified by physical integration and fault tests. Available MCU and safety-drive functions make a bench experiment plausible. This experiment acquired no hardware measurements and establishes no dangerous-failure rate.

## Technical account

### Problem and mechanism

Let true settled position be x in [0,20] mm, measured position be y, and the requested increment d be ±1 mm. Require sensor error |x−y| ≤ 1 mm at commit, including drift and calibration. Let the full physical stroke lie inside the interval joining x and x+d, enlarged by 1 mm at either end. Compute the authorization interval [y+min(0,d)−2, y+max(0,d)+2] mm and authorize only if it fits inside [0,20] mm. Translation by x−y shifts the nominal measured segment to the true segment. Adding the sensor and excursion allowances covers both translations and physical overshoot. Denied transitions hold position, so induction covers every authorized/denied sequence. Fault-time paths are included only if they obey the same tube. Arbitrary repeated requests and safe refusal are within scope, as is the possibility that the carriage cannot make progress near a guarded boundary.

A physical reference monitor must control every relevant way to issue a drive command. Integrity requires secure firmware and wiring, plus an independently engineered inhibit. Boot verification detects unauthorized images within its trust chain. It supplies no assurance that a properly signed policy matches the hazard. Calibration, true position, braking and shared infrastructure remain physical dependencies.

### Method and experimental conditions

A standard-library Python simulator runs a request-only pipe into a controller that owns the plant through a trusted harness. The plant returns a continuous path interval for each step, with an exact integer settled endpoint. Nominal requests contain only a signed direction marker and newline. The fixed policy checks ready status, trusted sample presence and age (0–5 ms), and the geometric interval. Explicit fixture inputs vary bias, staleness, inhibit, excursion and bypass. Bias and bypass use safely initialized but non-nominal boundary states. No physical time or electronics were modeled.

An independent executable model uses states x and a nondeterministic product of three action classes, three integer errors, two overshoot allowances and two health classes. There are 36 input combinations per state. Breadth-first reachability and exhaustive simulator/model comparison are complemented by the real-valued interval argument. Conditions and commands are in [results](../../../experiments/asimov/RESULTS.md).

### Quantitative results and reproducibility

From 10 mm, nominal unbiased positive requests advance eight times to 18 mm, then fail the interval check. Under admissible integer error the reachable interval is 1–19 mm. Bias −10 mm at 20 mm creates a false reading of 10 mm and a true endpoint of 21 mm. Overriding drive mediation at 20 mm also reaches 21 mm even though the policy refuses. A 4 mm excursion at 17 mm after a +1 mm command admits travel to 22 mm before settling at 18 mm. The path model reports bounds, not time traces.

For a measured maximum outward speed v through latency τ and a verified minimum deceleration a, an illustrative stop distance is vτ+v²/(2a). At 50 mm/s, 10 ms and 2500 mm/s² this is 1.00 mm before additional error allowances. If a bench needs more than 1 mm, increase the guard band, reduce speed, or drop the physical invariant and evaluate command authorization alone. The 5 ms cutoff addresses sample age, and sufficient braking requires its own latency and actuation analysis.

### Limitations, counterevidence and alternatives

The 756 combinations are exhaustive cases of a finite abstraction, not random independent demands. No statistical confidence interval or component reliability applies to that count. A physically independent sensor or controller can still share calibration, brakes, power, environment or maintenance errors. Sensor authentication cannot establish physical truth. Drive torque removal may allow coast. A stationary stage is also a physical assumption in the reject and idle states. Bench falsifiers include precommit drift beyond the measurement allocation, any unmediated drive path, and any ordinary or fault-time trajectory leaving its reserved interval. A disconnected controller can be evaluated for command admission without assuming a mechanical stopping bound.

### Relevance to Eternal Circuit

Narrow delegated authority is plausible as a research direction. Even identical chassis can require different policies after a load, wear, or actuator change. This creates a testable dependency on how a particular installation is commissioned. No story premise follows from the present hardware evidence.

## Source and provenance ledger

The documents or relevant sections were inspected on 2026-11-16. No direct X coverage and no independent field replication of this integration were available. A vendor integration example supports implementability of its documented interfaces only.

| Type | Title / organization | Date / version | Persistent ID | Original URL | Accessed UTC | Evidence quality |
| --- | --- | --- | --- | --- | --- | --- |
| Primary systems engineering guidance | Engineering Trustworthy Secure Systems, NIST | 2022, Vol. 1 Rev. 1, §D.4.2 and §E.13 | 10.6028/NIST.SP.800-160v1r1 | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf | 2026-11-16 | Design criteria for complete, non-bypassable, evaluable and protected mediation |
| Primary firmware guidance | Platform Firmware Resiliency Guidelines, NIST | 2018 | 10.6028/NIST.SP.800-193 | https://csrc.nist.gov/pubs/sp/800/193/final | 2026-11-16 | Firmware protection, detection and recovery concepts |
| Regulator engineering guidance | Control systems, UK HSE | Undated web edition, Independence section | COMAH technical measures | https://www.hse.gov.uk/comah/sragtech/techmeascontsyst.htm | 2026-11-16 | Independence and common-cause design considerations |
| Primary control theory | Control Barrier Function Based Quadratic Programs for Safety Critical Systems, Ames et al. | 2017 journal issue | 10.1109/TAC.2016.2638961 | https://authors.library.caltech.edu/records/jnhr0-1ww05 | 2026-11-16 | Forward invariance framing. ASIMOV uses a stroke contract and interval proof. |
| Vendor documentation | Getting started with STiRoT for STM32H5 MCUs, STMicroelectronics | AN6007 Rev. 9, June 2026, §2.1 | AN6007 | https://www.st.com/resource/en/application_note/an6007-getting-started-with-stirot-st-immutable-root-of-trust-for-stm32h5-mcus-stmicroelectronics.pdf | 2026-11-16 | Immutable first boot and application verification, not stage validation |
| Vendor application example | Controlling SINAMICS S210 Safety Integrated Functions using SIMATIC S7-1500TF via PROFIsafe, Siemens | V1.11, October 2019, §2.1 | 109760341 | https://cache.industry.siemens.com/dl/files/341/109760341/att_1001483/v1/109760341_SafetyS210_TO_Axis_DOC_V11_en.pdf | 2026-11-16 | Distinguishes actuator torque-off and monitored stop functions |
| Primary specification | Trusted Platform Module Library, Trusted Computing Group | Family 2.0, level 00, rev. 01.59, 2019-11-08, Part 1 | TPM 2.0 rev. 01.59 | https://trustedcomputinggroup.org/wp-content/uploads/TCG_TPM2_r1p59_Part1_Architecture_pub.pdf | 2026-11-16 | TPM measurement, key and attestation architecture |
| Vendor documentation | EdgeLock SE050 Secure Element, NXP | Undated product page | SE050 | https://www.nxp.com/products/SE050 | 2026-11-16 | Device/key hardware capabilities |
| Primary standard | Security Requirements for Cryptographic Modules, NIST | 2019 | FIPS 140-3 | https://csrc.nist.gov/pubs/fips/140-3/final | 2026-11-16 | Cryptographic module assurance scope |
| Primary specification | TEE System Architecture, GlobalPlatform | v1.3, May 2022 | GPD_SPE_009 | https://globalplatform.org/specs-library/tee-system-architecture/ | 2026-11-16 | Logical isolation and trusted application interfaces |

## Local evidence and reconstruction

Start at 10 mm, use signed 1 mm strokes, a 20 mm envelope, 1 mm sample error, 1 mm transient allowance and holding on denial. Enumerate the three request classes, measurement errors −1, 0, +1 mm, overshoot 0 or 1 mm, and ready/not ready. Push any newly reached safe settled state into the work queue and check the entire path interval of every generated edge. Reproduce the unvalidated fault examples with `python3 -m asimov.simulation.run --demo`. No device qualification, latency measurement, certification or hardware attack test can be reproduced from these artifacts.

## Related records

- Prior deposit [EC-R-2026-001](EC-R-2026-001-hardware-mediated-ai-safety.md) and dossier [EC-SCI-2026-001](../../reviews/EC-SCI-2026-001-asimov-hardware-safety.md).
- Follow-on [EC-SCI-2026-002](../../reviews/EC-SCI-2026-002-asimov-indexed-axis.md).
- No manuscript target or revision.

## Revision history

- 2026-11-16 — Initial design, formal argument, finite checker, fault fixtures and source ledger.
