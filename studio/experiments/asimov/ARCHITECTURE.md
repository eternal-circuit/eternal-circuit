# Reference architecture

## Authority and knowledge

| Question | Design answer |
| --- | --- |
| Who generates decisions? | The untrusted planner can propose any sequence, at any rate, including invalid inputs. |
| Who has authority? | An immutable ingress binding grants the planner the capability to **request** one signed-direction increment of one axis. Only the separate controller may commit a stroke. The safety supervisor may remove permission. |
| What keeps enforcement intact? | Protected boot and firmware, physical separation of effect wiring, minimal interfaces, independent inhibit, and verified configuration. Each is an assurance obligation. |
| Who defines safety? | Engineering and independent hazard review specify the limits, operating domain and fault assumptions. A correctly functioning monitor can enforce a bad specification. |
| What can be known? | Timestamped encoder readings, settled/holding state, and diagnostic signals within established uncertainty. The controller has no general observation of people, obstacles, downstream effects or harm. |

```text
planner → bounded request ingress → authorization MCU → drive → carriage
                                     ↑                    ↑
                               encoder A            wired inhibit
                                                          ↑
                     encoder B, stops, E-stop → independent supervisor
```

Use a dedicated MCU with its own protected flash, clock, supervisory power and sensor link. Keep the host physically disconnected from motion, enable, debug and maintenance interfaces. The drive starts disarmed. A local reset/re-arm procedure validates position/holding and clears any pending commands. Both authorization and independent enable must be present for motion. The supervisor independently checks position, drive state, its watchdog/heartbeat, guards and emergency stop and removes motion permission on fault. Set its trip threshold from its **own** delay and braking budget. A safety PLC and drive's safety inputs can implement the veto. Diagnostics may detect departures from assumptions; an already unsafe stroke cannot be undone.

## Interfaces and lifecycle

| Boundary | Contract |
| --- | --- |
| Planner → MCU | Fixed-size operation enumeration, no absolute position, gain, duration, update or actuator credentials. Finite queue, bounded per-cycle parsing budget and rate limits; excess requests dropped. Link identity authenticates the request source where multiple principals share ingress. A hostile authenticated planner remains untrusted. |
| Sensors → checks | Independent position channels where practicable; trusted local timestamp and freshness check, plausibility and disagreement diagnostics, calibrated scale, range and worst-case error. Confirm carriage settled and holding locally before latching sample. An authenticated sample can still be wrong. |
| MCU → drive | Prefer dedicated drive I/O with exclusive wiring and one-shot, single-flight commit. For a digital link, authenticate device/axis, step, policy version, session epoch, monotonic sequence and expiry as a single canonical record. Verify at the drive before effect, atomically consume sequence, reject duplicates, expire after deadline, purge on reset and rekey per boot. Engineer clock/skew and reset behavior explicitly. MACs authenticate fields and origin; the receiving endpoint must enforce timing and consumption. |
| Supervisor → drive | Separate fail-deenergize loop, safety drive input and monitored brake where the hazard demands it. Measure achieved stop behavior. STO removes torque and can allow coasting; a safe stop may require monitored braking and retention. |
| Maintenance and updates | Independently authorized signing key and review, install only disarmed, reject older or wrong-device policy, verify complete candidate before atomic activation, retain a verified recovery image under the same safety floor, self-test and require local re-arm. Commission with actuator disconnected before enabling. Bind policy to machine configuration, units and firmware compatibility. |
| Audit | Monotonic events for sample/time/health, request and result, active policy hash, commit ID, drive acknowledgement and supervisor fault. Hash-chain and sign checkpoints under a separate audit identity, export to an independent collector to detect missing/truncated history. Report gaps, rate-limit logging and keep it off the commit deadline. Simulator JSONL is plain diagnostic output. |

The static prototype policy can be compiled into firmware with protected outer limits. A signed update is still a code/policy change requiring regression and hazard review. An independent trip path must retain its own configuration and veto during a failed or compromised update.

## Hardware choices and evidence boundaries

| Technology | Appropriate role | Assurance limit |
| --- | --- | --- |
| Dedicated secure-boot MCU | Deterministic parsing and geometric checks, local encoder validation, exclusive drive command, watchdog/protected debug. ST's STM32H5 STiRoT documents immutable boot on supported parts. | Platform security capabilities require correct configuration. General-purpose MCU and firmware require safety evidence. |
| Safety PLC and safety drive | Independent monitoring/inhibit and validated stop functions where supported. Siemens documents an S7-1500TF/S210 integration. | Device function and wiring evidence alone cannot establish this stage's stopping envelope or independence. |
| TPM 2.0 | Platform measurements, attestation and key sealing. Optional for host/commissioning evidence. | Quotes represent measured state and policy, with trust in the measurement chain. The TPM does not own actuator I/O or bound travel. |
| Secure element | Protect a local device identity or message-authentication keys; an SE050-class device illustrates the role. | Does not supply trusted mechanical sensing or deterministic stop control. |
| HSM | Offline firmware/policy signing and authorization under controlled key custody. FIPS 140-3 applies to cryptographic modules. | Module validation does not establish correct policy or key-holder decisions. Keep signing out of the live motion loop. |
| TEE | Optional isolation for provisioning, sensitive host data or telemetry. | Shared SoC, debug, power, DMA/peripherals, availability and trusted I/O require platform-specific arguments. A host enclave is insufficient as the sole motion authority. |

The component classes exist today. The full controller-to-physical-envelope argument, security/safety co-assurance, quantified independence and reliable evolution of the safety specification remain development and validation work. Original documents and versions are recorded in the [research deposit](../../research/notes/2026/EC-R-2026-002-asimov-indexed-axis.md).

## Next bench build

Use an unloaded, guarded, low-energy horizontal stage with an encoder, independent calibrated external position measurement, suitable brakes/holding, end stops outside the experimental envelope, independent emergency-stop and motor inhibit. Bench the dedicated MCU, safety PLC/safety relay and monitored drive first against a hardware-in-the-loop plant. Measure maximum true sample error, start/stop latency, excursion in both directions and residual travel during watchdog, power-loss and brake faults across the declared load, temperature, supply and wear range. Use an independent timebase and account for instrument uncertainty. Inspect every wiring and debug/maintenance path with the drive disconnected before field motion.

If the 1 mm excursion contract cannot be validated, expand the reservation margin or lower speed and permitted stroke energy. A narrower fallback is authorization of command values at a guarded, disconnected interface, with no position-invariance claim.
