# Scientific constraints for The Eternal Circuit

Working modeling brief. Use mathematical and statistical laws as constraints on outcomes. Choose a small model appropriate to each scene and record its assumptions, units, uncertainty, and failure modes.

| System | Minimum model | Consequence for a scene |
| --- | --- | --- |
| Signals and clocks | A one-way path of length d has a vacuum transit lower bound d/c. Include transmission, processing, queuing, link outages, and clock reference where material. | Earth cannot supervise Martian decisions in real time. Delayed commands can arrive under obsolete assumptions. |
| Transport | Budget trajectory, delta-v, propellant, dry mass, payload, travel time, and arrival or deceleration. For an ideal rocket with constant exhaust velocity, delta-v = exhaust velocity × ln(initial mass / final mass). | A rescue, mass evacuation, or archive launch needs vehicles, capacity, and time. |
| Compute | Estimate operation count by workload, memory footprint and movement, bandwidth, available power, cooling, utilization, and hardware attrition. At constant electrical power P, energy over time t is P × t. | A fleet can lose useful inference or control capacity long before losing access to its stored weights. |
| Heat and irreversible erasure | For the standard idealized erasure of an equiprobable bit at temperature T, the Landauer lower bound is k_B T ln 2. Estimate real compute energy independently. For an idealized radiating surface facing a much colder sink, emitted power scales with emissivity, area, and absolute temperature to the fourth power. | Running colder shifts heat-rejection and reliability constraints. An erasure bound alone gives no usable throughput estimate. |
| Encoding and uploading | Specify what was observed, how it was sampled, which variables the representation retains, what decoder and side information it uses, and the error metric. Separate lossless encoding of a sampled record from loss incurred before encoding. | Behavioral fidelity under one test can coexist with severe loss of source information outside that test. A learned reconstruction includes the decoder's prior assumptions. |
| Archives | Track integrity checks, repair redundancy, copying cadence, independent versus common-mode faults, physical media and power, and whether future readers have the specification and keys. | Surviving bytes can be inaccessible or intelligible in a different sense than intended. Replication cannot restore information missing from every independent source. |
| Demography | Advance age cohorts with age-specific survival, fertility, and migration. Distinguish births per year, total fertility rate, and population change. Compare trajectories under differing assumptions about care, cost, work, health, and relationship formation. | Persistent low fertility produces delayed effects because the age structure carries momentum. Regional and generational trajectories can diverge. |
| Reliability and behavior | Specify base rates and the measurement process. Model correlated failures, uncertainty in estimates, and changes in the population or operating conditions after deployment. Validate tail-risk claims against plausible alternatives. | An AI can excel on audited cases while failing in rare or shifted conditions and while causing harm its rubric omits. |
| Cosmic horizon | State the assumed expansion history and accessible causal domain. Track local stores of usable free energy, radiative sinks, and long-term risks to matter or hardware according to the scenario assumed. | Heat death is an asymptotic loss of usable gradients in the chosen model. Treat intermediate epochs and extrapolations as conditional. |

## Rules for disputed evidence

Relativity and local energy accounting constrain the setting. There is no faster-than-light travel or signaling. A speculative mechanism can motivate a character's actions. Its possible existence and causal consequences remain separate from what the story actually establishes.

Use order-of-magnitude estimates first and preserve enough inputs for a reader to recompute them. Distinguish measurement error, variation between cases, and uncertainty about the model itself. Where two models can fit the same evidence, record a test that would distinguish them or mark the issue unresolved. Do not assign numerical odds to a theological proposition or to an unmodeled exotic mechanism.

For scenes involving memory loss, specify who chose the objective function and which errors it discounts. For late-era scenes, keep an energy ledger that includes maintenance effort, mobility, storage refresh, and the cost of detecting errors. Physical entropy, Shannon entropy, and the story's language of spiritual decay may echo each other. Use the relevant quantity and units when making a quantitative claim.

Technical reference for the erasure limit: Barbara Piechocinska, [Information erasure](https://doi.org/10.1103/PhysRevA.61.062314).
