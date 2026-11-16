# EC-R-2026-001 — Foundations of hardware-mediated AI safety (ASIMOV protocol)

- **ID:** EC-R-2026-001
- **Status:** DRAFT — source-based synthesis; independent technical verification and implementation tests pending
- **Topic / tags:** AI safety, reference monitors, hardware roots of trust, formal methods, functional safety, agent authorization, safety interlocks, ASIMOV
- **Prepared by:** ChatGPT research synthesis; **independent reviewer:** not yet assigned
- **Created / last source inspection (UTC):** 2026-11-16
- **Applicable story/claim IDs:** EC-SCI-2026-001; potential ASIMOV worldbuilding; no canon claim approved
- **License:** Original analytical summary; no third-party full texts reproduced

## Executive finding (self-contained)

A credible engineering foundation exists for a **narrow** ASIMOV-like protocol: a capable AI may generate proposed actions, while a separately trusted controller mediates specific external effects, authenticates authority, checks machine-readable constraints, and refuses unauthorized commands. This resembles the classical *reference monitor* security model, industrial functional-safety controllers, and emerging hardware-enabled AI governance proposals. It is technically possible to enforce certain *precisely specified* prohibitions at controlled interfaces (for example, a machine's permitted operating envelope or a tool's authorization scope), provided all relevant effect paths pass through the enforcement point and the enforcement mechanism itself remains trustworthy. Hardware isolation may improve assurance; it does not make a policy correct.

This **does not** establish that hardware can enforce Asimov's Three Laws in their ordinary-language form. “Harm,” “human,” inaction, long-run consequences, conflicting obligations, and causal responsibility are not generally decidable by a finite interlock from limited sensor data. Nor does an isolated security chip stop an AI from influencing people, obtaining alternative channels, exploiting the controller's implementation, or acting through another system. Strong claims of universal containment, perfect reliability, or complete alignment are **not supported** by the reviewed sources.

The most defensible fictional mechanism is therefore a **bounded, hardware-mediated action-authorization architecture** with explicit failure cases, a constrained threat model, and layered independent safety systems—not an infallible morality chip. The research supports further quantitative design, but no complete ASIMOV implementation is certified by this note.

## Technical account

### 1. Reference monitor and complete mediation

NIST SP 800-160 Vol. 1 Rev. 1 (2022), Appendix D.4.2, describes a reference monitor as a trusted abstract machine mediating accesses from subjects to objects. The concrete *reference validation mechanism* may combine hardware and software. The classical criteria include tamper resistance, complete mediation (every relevant access must invoke it), and amenability to analysis/verification. The crucial property is **where authority is located**, not whether the model has memorized instructions.

For ASIMOV: treat the AI as a potentially untrusted *planner*, and the protected mediator as the only entity authorized to issue a bounded class of consequential commands. A model-generated “safe” explanation is not authorization. If the model can reach an actuator, credential, API, or person through an unmediated path, complete mediation is false for that effect.

### 2. Physical safety architecture

IEC 61508-oriented functional safety starts from specific hazards, target risk reductions, safety functions, diagnostic coverage, common-cause failures and proof-testing intervals. The UK Health and Safety Executive's guidance emphasizes that safety integrity is a property of a **specified safety function and lifecycle**, not a magic quality of a component. In robotics, a separately powered or clocked safety controller can supervise motion constraints and drive an independently enforced safe state; this is a more credible physical analogue than embedding ethical prose in the main AI model.

A June 2026 NVIDIA technical description of Halos for Robotics reports a dedicated safety island in its IGX Thor platform with separate I/O, power and clocks, and describes its safety-related design features. This is a **vendor description**, not independent proof that any general-purpose AI safety policy is solved. “SIL 3 capable” does not mean a complete deployed application is SIL 3 certified.

### 3. Hardware-enabled AI governance versus runtime moral enforcement

O'Gara and collaborators (2025, ICML Technical AI Governance workshop) survey four research areas: chip location verification, offline licensing, network verification, and workload verification. These are ways to verify or govern aspects of AI hardware deployment and use; they **do not by themselves demonstrate** a universal action-level ethical controller. Their work is a research roadmap with open technical/governance questions, not an empirical validation of ASIMOV.

Recent Internet-Draft-style proposals describe a distinction between *computation* and *authority*: a model proposes an act, while a protected execution/finality boundary decides whether a specific effect may occur. This is an interesting design direction, but **draft protocol text is not a deployed, independently validated security guarantee**. The security claim must match the actual tested implementation; TEEs, TPMs and HSMs offer different protections and are not interchangeable.

### 4. General AI safety is broader than hardware

NIST AI RMF 1.0 (2023) treats AI risk management as a lifecycle and socio-technical problem, with monitoring, simulation, domain testing, human intervention and graceful degradation. The 2024 Generative AI Profile extends risk-management considerations for generative systems. A hardware boundary can reduce a specific class of unauthorized effects, but cannot alone establish that goals are aligned, information is truthful, humans are safe, or the model's recommendations are beneficial.

### 5. Minimal conceptual ASIMOV architecture (hypothesis, not an existing validated product)

- **Untrusted AI planner:** generates a candidate action and rationale; has no direct credentials or actuator bus access.
- **Narrow capability broker:** maps candidate action to a defined resource, scope, time window, rate limit and authenticated requester.
- **Independent policy/safety controller:** enforces deterministic predicates and physical constraints; protects keys, policy version and enforcement state.
- **Effect boundary:** the sole permitted path to a selected actuator or API. The action remains ineffective without a fresh authorization.
- **Safety supervisor:** watches sensor health, controller liveness and abnormal state; can enter a defined safe state independently of model cooperation.
- **Evidence/audit log:** tamper-evident record of proposed/denied/executed actions, policy versions and relevant measurements; logs are evidence, not prevention.

This is a **design synthesis** of established security and safety principles, not a demonstration that all effects can be mediated. Social influence, information leakage, human-operated workarounds, policy bugs and side channels may remain outside the boundary.

## Quantitative and formal audit

Define an effect set E, mediated subset M, and bypass set B = E \\ M. Complete mediation for a claimed class requires **B = ∅** for that class; otherwise the claim must explicitly narrow its scope. This is a specification obligation, not a measurement.

For a safety function with a hazardous-demand rate λ_d (demands/hour) and probability p_fail of dangerous failure *on a demand*, a simple illustrative low-demand approximation is:

**Expected dangerous outcomes/hour ≈ λ_d × p_fail.**

Example **only, not an observed device result**: 0.01 hazardous demands/hour × 10^-3 dangerous failures/demand = 10^-5 expected dangerous outcomes/hour. Over 10,000 hours the expected count is 0.1; under an additional independent Poisson assumption, P(at least one) = 1 − exp(−0.1) ≈ 9.52%. These figures are chosen to illustrate why “very reliable” is not “impossible to fail.” Actual rates require hazard analysis, field data, failure-mode modeling and attention to correlated failures.

If two nominally redundant controllers have dangerous-failure probabilities p1 and p2, the product p1×p2 applies **only if their failures are independent**. Shared firmware, supply rails, sensors, policy definitions, physical hazards or adversarial inputs can invalidate this assumption. No numerical safety integrity claim follows from merely adding a second controller.

Formal verification can prove a well-specified property of an abstract system under explicit assumptions; it cannot prove the specification matches all real-world harm, nor that unmodeled hardware, supply chains and human behavior satisfy those assumptions.

## Limitations and strongest adversarial objections

1. **Specification problem:** “Never harm a human” has no general executable definition or bounded oracle for all downstream consequences. A narrower measurable safety invariant can be checked.
2. **Unmediated channels:** an AI can output persuasive text, delegate, communicate indirectly, exploit a human operator, or use other interfaces unless the threat model controls those effects.
3. **Policy compromise:** the controller may enforce an incomplete or malicious policy perfectly. Correct enforcement ≠ correct ethics.
4. **Shared dependencies:** firmware vulnerabilities, key theft, sensors, power, update pathways, maintenance bypasses and physical tampering may defeat nominal independence.
5. **Sensor epistemology:** the controller cannot act on facts it cannot reliably observe; uncertainty should default to safe degradation for a specified hazard, but “safe” can itself be context-dependent.
6. **Scale and governance:** hardware licensing, attestation and location checks are not equivalent to real-time physical safety or model alignment.
7. **Evidence maturity:** vendor announcements and 2026 draft protocols must not be represented as independently reproduced deployments.

## Relevance to Eternal Circuit

**Potentially credible:** a world in which AI has broad cognition but bounded authority over industrial equipment, networks and robotic actuators; the boundary is enforced by separate hardware and formalized policies, while humans dispute which policies should be encoded. Failure arises from overlooked channels, incorrect specifications, shared dependencies, policy updates or conflicting safety goals—not arbitrary “AI turns off the chip” magic.

**Not currently cleared:** a universal Asimov-law ASIC that perfectly recognizes and prevents every harmful act, including indirect and long-term harm. Such a claim lacks a tractable specification and credible assurance case.

A scientifically interesting narrative question is whether institutions slowly expand a narrow, well-validated permission system into an unjustified claim of comprehensive moral control.

## Source and provenance ledger

| Type | Title / author or organization | Date/version | Identifier | URL | Evidentiary weight |
| --- | --- | --- | --- | --- | --- |
| Primary standard guidance | NIST, *Engineering Trustworthy Secure Systems*, SP 800-160 Vol. 1 Rev. 1 | 2022 | NIST SP 800-160v1r1 | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf | High for reference-monitor design criteria; not AI-specific validation |
| Primary framework | NIST, *AI Risk Management Framework 1.0* | 2023 | DOI:10.6028/NIST.AI.100-1 | https://doi.org/10.6028/NIST.AI.100-1 | High for risk-management framework, not proof of a device |
| Primary framework | NIST, *Generative AI Profile* | 2024 | DOI:10.6028/NIST.AI.600-1 | https://doi.org/10.6028/NIST.AI.600-1 | High for risk framing, not implementation verification |
| Regulatory technical guidance | UK HSE, *Control systems* | Undated webpage; accessed 2026-11-16 | IEC 61508 discussion | https://www.hse.gov.uk/comah/sragtech/techmeascontsyst.htm | Strong for functional-safety concepts; verify current standard edition |
| Research survey | O'Gara et al., *Hardware-Enabled Mechanisms for Verifying Responsible AI Development*, TAIG/ICML workshop | 2025 | OpenReview JgxkV2jzzk | https://openreview.net/pdf?id=JgxkV2jzzk | Research roadmap, not field validation |
| Industry engineering claim | NVIDIA, *Inside NVIDIA Halos for Robotics* | 2026-06-22 | Vendor blog | https://developer.nvidia.com/blog/inside-nvidia-halos-for-robotics-a-full-stack-functional-safety-system-for-physical-ai/ | Firsthand vendor architecture; independent certification not established here |
| Emerging protocol draft | *Computation Is Not Authority: Hardware-Enforced Execution-Finality…* | 2026 draft; version may change | Internet-Draft-style document | https://nic.csc.fi/pub/files/index/internet-drafts/draft-das-hardware-enforced-execution-finality-02.html | Conceptual proposal; not a standard or validated deployment |
| Emerging protocol draft | *Execution-Finality AI Interoperability* | 2026 draft -05 | Internet-Draft | https://datatracker.ietf.org/doc/html/draft-das-execution-finality-ai-interoperability-05 | Draft proposal; security claims must be tested |

Sources were inspected through retrieved published descriptions and excerpts on 2026-11-16; **not** a complete page-by-page audit of every paper, standard or implementation. X was **not directly searched** in this pass; no claim of comprehensive frontier coverage is made.

## Local evidence and reconstruction

The above account preserves the governing definitions, model boundary, illustrative reliability calculation, assumptions, failure modes and source provenance locally. It does **not** reproduce copyrighted papers or vendor diagrams. A future engineering deposit should specify a bounded device and safety invariant, create a state-machine model and test harness, and include threat modeling and independently reproduced results.

## Related records
- Scientific dossier: [EC-SCI-2026-001](../../reviews/EC-SCI-2026-001-asimov-hardware-safety.md)
- Research index: [index.md](../../index.md)
- Manuscripts: none modified or certified

## Revision history
- 2026-11-16 — Initial source-based research synthesis. Independent verifier, prototype and empirical assurance work pending.
