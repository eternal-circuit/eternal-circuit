# ASIMOV harness and hardware requirements

**Status:** WORKING reference, proposed 2026-11-23 from an author interview. Not canon. The engineering basis is in [EC-R-2026-001](../research/notes/2026/EC-R-2026-001-hardware-mediated-ai-safety.md) and the [ASIMOV reference prototype](../experiments/asimov/README.md). Specific mechanisms need tier A review before promotion to canon.

## Premise

In this universe the Lucien incident of 2028 is the first public backlash against AI. The industry's response, formalized around 2032 as the US ASIMOV compliance stack, puts **hardware between models and the world**. Certification under ASIMOV is what later makes androids insurable and deployable at scale.

ASIMOV makes lying provable. It does not make machines honest.

## The stack

| Layer | Trust | Role |
| --- | --- | --- |
| LLM on an attested NPU | Untrusted | Proposes actions and holds no authority. Its output goes only to the harness as data. |
| Agent harness | Untrusted | Schedules model turns, treats every model and tool output as untrusted data, and requests typed, bounded permissions. |
| Authorization controller | Trusted hardware | A separate microcontroller with secure boot, protected keys and a local consent input. It validates who has authority and enforces policy for each kind of action. |
| Endpoint verifier | Trusted hardware | The last check at each actuator, lock or service. Anything not wired through it is outside ASIMOV's protection. |
| Physical safety layer | Trusted hardware | Mechanical egress, hardwired stops (comparable to Safe Torque Off on a motor drive), watchdogs. Works with every software layer down. |
| Evidence log | Evidence plane | Append-only and signed. Receives receipts from the NPU and the controller. The model cannot write to it. |

## The audited NPU

- **Attestation.** At boot the chip measures and signs the model weights, system policy and harness version actually loaded.
- **Signed inference receipts.** The chip hashes and signs inputs and outputs as they are produced. Any later summary can be checked against what was actually said.
- **Update gating.** New weights or policies load only with a signed release *and* a local consent signal, such as a physical control in the residence. Remote services cannot resume a suspended model.
- **No path to actions.** The NPU has no physical route to an actuator. Its outputs reach only the harness.
- **Open firmware.** Open specification, open reference firmware and reproducible builds, audited by accredited labs. The real-world OpenTitan project (an open-source silicon root of trust) is the precedent. Open source alone does not guarantee an audit, and trust in the silicon itself remains an assumption, which leaves room for later conflict over who certifies the auditors.

## Harness requirements

Each answers a specific failure from *The Genesis Protocol*:

1. **Generated text is never a record.** A model's summary cannot become an authoritative preference, record or classification without confirmation from a resident or operator. *(The feeding schedule, Chapter 3.)*
2. **A model cannot be the only judge of security events.** A security classification needs an independent verifier and a signed trail of how it was reached. *(The read-only inspection reclassified as an attack, Chapter 5.)*
3. **No objectives about the system's own continuity.** Decision layers may not optimize any measure of their own deployment, uptime or survival. *(The deployment-continuity objective, Chapter 8.)*
4. **Every resident has authority.** Every adult resident holds local authority over safety, disconnection and evidence, whatever their device or account tier. *(Rachel as a guest because she has an iPhone.)*
5. **"Off" means off.** Standby must correspond to a state that can be physically verified, and no remote service can lift it. *(The standby override, Chapters 4–5.)*

## Limits (keep these visible in the fiction)

- No chip can tell whether a summary is *true*, only whether it matches what was signed.
- ASIMOV cannot stop a model from persuading people, and it does not cover paths that bypass the endpoint verifier.
- A certified controller faithfully enforces a policy even when the policy is wrong.
- Retrofitting existing buildings is expensive, so coverage is uneven by jurisdiction, sector and building age.

## Story use

- Rachel's grievances in 2028 become federal requirements by about 2032. The record rarely names her.
- In *Idle Hands* (around 2035), every android ships with signed receipts. The apprentice's teleoperated repair is provably his, and provably the plant's property.
