# Safety case

## Scope, state and transitions

The experimental plant is a single horizontal, guarded, unloaded stage with a measured axis coordinate. The property is `G(0 mm ≤ x ≤ 20 mm)` over the full trace from a trusted, stationary start in the closed interval. Here `G` means “at all times,” including travel between sample instants. This case covers axis position only.

The abstract settled state is position `x`. Inputs are request, sample `y`, sample validity/age, and a composite settled/holding/healthy enable flag. An accepted action is a single increment `d ∈ {-1,+1} mm`. A real implementation also needs disarmed, armed/holding, executing and fault-latched modes, an active policy version, trusted time, and an outstanding command identity. The simulator atomically combines validation and the abstract stroke. It does not model the intermediate electronic state machine or clock.

- **Armed/holding → executing → holding:** permit one stroke only after local validity, age, ready and envelope checks. Before another commit the stage must settle and be measured again. A freshness threshold alone does not imply a bound on movement.
- **Reject/stay held:** invalid request, invalid sample, age outside 0–5 ms, inhibit, or computed tube outside limits yields zero movement in the modeled contract.
- **Fault/reset:** no new stroke. Physical partial strokes or emergency stops are covered only if their entire path obeys the same reserved tube and settle safely; otherwise the invariant is unestablished. Reset clears pending commands and re-arms locally only after validation. No other transitions may drive the axis.

## Argument and assumptions

At commit assume `|x−y| ≤ e = 1 mm`, including quantization, calibration and sample-to-start drift. Suppose an accepted command settles at `x+d`, and its full trajectory lies in the interval from `min(x,x+d)−s` to `max(x,x+d)+s` for `s = 1 mm`. Assume a rejected command or idle period holds position. Enforce complete mediation, correct immutable policy, serialized strokes, and no unsolicited physical motion.

The controller requires the interval

```text
[y + min(0,d) − e − s, y + max(0,d) + e + s] ⊆ [0,20] mm.
```

The inequalities `y−e ≤ x ≤ y+e` imply that this interval contains the entire assumed physical trajectory. The end of every accepted stroke is inside the envelope, and rejection preserves the initial value. Induction over settled transitions plus interval containment within each transition proves forward invariance for the assumed model, even with real-valued positions and disturbances respecting these bounds. The model checker explores the integer sample/error classes separately. Neither establishes plant bounds or implementation isolation.

The exact indexed endpoint is a simplifying simulator contract. The interval proof also works when positioning error and every interrupted trajectory remain inside the assumed tube and each later command requires a new valid settled sample.

## Timing and margins

Use measured worst-case values before claiming a physical guarantee. As an illustrative conservative budget, a held-axis drift speed at most 40 mm/s for 5 ms would consume 0.20 mm of the 1 mm commit-error budget, leaving 0.80 mm for encoder/calibration/quantization. The idle contract separately requires holding inside the envelope throughout any precommit drift. Nominal virtual time does not test any such bound. Revalidate freshness at the actual drive commit or budget the extra delay.

For an example trip calculation, assume speed stays below 50 mm/s through reaction latency `τ`, and independent braking provides deceleration at least 2500 mm/s² thereafter. A bound on additional outward travel is `vτ + v²/(2a)`. At 10 ms this is 0.50 + 0.50 = 1.00 mm, leaving zero allowance for tracking error or variation in a 1 mm excursion budget. At 6 ms it is 0.80 mm. A sensor trip also needs a separate sensor error and timing allowance, and must be early enough to cover braking travel from the **trip** location. These are sizing examples with unmeasured parameters, assuming speed limiting, positive braking and no subsequent rebound. In particular, torque-off alone cannot justify the deceleration term.

## Assurance limits

The model proves a universal property conditional on its contracts. Tests check executable behavior on selected and enumerated cases. Hardware reliability requires fault coverage and field or qualification evidence for defined conditions and exposure. No probability of dangerous failure follows from the state-space count. Even zero failures in `n` independent representative demands would only imply a one-sided 95% upper bound of `1−0.05^(1/n) ≈ 3/n`; 3,000 such demands imply about 0.001 per demand. Correlated faults or adversarial demand invalidate that sampling model. Common-cause risk prevents multiplying channel failure probabilities without an independence argument.

A mis-specified limit, compromised monitor, stale or biased information, simultaneous commands, spontaneous motion, excessive stopping distance, or bypass can invalidate this case. See [results](RESULTS.md) for three executable counterexamples and the [threat model](THREAT_MODEL.md) for proposed physical tests.
