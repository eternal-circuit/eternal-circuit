# Idle Hands remote-maintenance coverage experiment

This model asks when one paid four-hour overlay shift could be removed from an eight-hour fleet dispatch roster. It is a synthetic counterfactual for the fiction proposal. No fleet observations, wages, demonstration count, learning curve, fault-rate estimates or measured service times are inputs.

## Inputs

| Input | Assumption |
| --- | --- |
| Scope | One pooled remote-maintenance desk for a cluster of matched warehouse lanes, including one eligible recurring conveyor fault family. |
| Staffing | One qualified technician available at minute 0 through 480, with an optional second operator available from 120 through 360. Each eligible operator has the same modeled dispatch service time. Breaks and other tasks are absent; a real roster must provide coverage for them. |
| Jobs and releases | Eight family tickets, 16 minutes of operator time each in manual handling. Eight unrelated jobs, 12 minutes each. The exact open-loop releases are in the script in minutes from shift start. No carry-in and no ticket aging from preceding shifts. |
| Intervention | A chosen subset of family tickets has been provisionally diagnosed locally and needs a four-minute human review. All other family tickets take the original 16 minutes. The release is when the desk can start handling or validating the ticket. This model holds release times fixed across counterfactuals, so it omits autonomous attempt time and the added delay of failed attempts. |
| Queue rule | Non-preemptive arrival order. Dispatch to the operator who can start soonest and complete within the overlay window if that operator is used. Break ties by ticket ID and prefer the base operator when both can start together. |
| Acceptance | Every ticket on the evaluated trace must start within ten minutes of desk release and finish within the 480-minute day. This is an invented business rule for roster evaluation. It covers the desk queue, with no implication for safe machinery or total recovery time. |
| Employer decision | On achieving the stated business rule with one operator on the accepted demand conditions, the employer elects to remove one standby shift. Removing hours is a discretionary cost/coverage decision, not a direct consequence of the reduction in service minutes. |

The fleet, number of sites and times are story assumptions. Confirm them from logs if treated as empirical claims. Count the recurring condition by independent fault opportunities. Repeated interventions on a single defective machine can overstate both training evidence and fleet demand. A permanently repaired bracket does not keep supplying its old rate of tickets; define an eligible bounded family on distinct assets or treat recurring incidents as an evaluation stress trace. Repairs involving unknown damage, unsafe states or a nonmatching assembly require a separate response. The queue model assumes a qualified local diagnostic and does not determine whether a robot can learn or safely perform it. The diagnostic queue excludes the subsequent local physical repair.

## Reproduce

From the repository root, run `python3 research/models/idle-hands/queue_model.py`. Python standard library only. The script checks reference results with assertions and enumerates all 256 subsets of converted family tickets. These are combinatorial scenarios without assigned probabilities.

| Trace | Policy | Staffing | Worst start wait | Operator-min |
| --- | --- | --- | ---: | ---: |
| Regular | Manual | Base | 59 min | 224 |
| Regular | Manual | Base + overlay | 2 min | 224 |
| Regular | All family tickets shortened | Base | 9 min | 128 |
| Clustered | Manual | Base + overlay | 10 min | 224 |
| Clustered | All family tickets shortened | Base | 14 min | 128 |
| Clustered | All family tickets shortened | Base + overlay | 3 min | 128 |
| Synchronized burst | All family tickets shortened | Base | 28 min | 128 |
| Synchronized burst | All family tickets shortened | Base + overlay | 9 min | 128 |

The regular baseline uses 224/480 ≈ 47% of one operator's shift on average, but releases 188 operator-minutes of demand inside the 120-minute window [120,240). After converting all family tickets the day uses 128/480 ≈ 27% of one shift. It reduces work by 96 operator-minutes, or 43%, yet can remove 240 rostered minutes because that shift was scheduled partly as standby for peak load.

At six successes, 2 of 28 placements of the shortened tickets pass on the regular trace. At seven successes 3 of 8 pass. At eight successes this specific trace passes, and increasing validation from eight to nine minutes changes the worst wait from 9 to 13 minutes. The never-passing low counts and the sensitivity sweep are printed by the executable. The selectively constructed clustered trace has the same daily workload as the regular trace. Its manual overlay passes, but conversion still cannot remove the overlay. The burst also has identical demand counts and processing minutes but fails one-operator coverage after every eligible ticket is shortened. Its design places the same eight calls in eight consecutive release minutes. It is a density stress test, not a claim to know actual failure clustering. Its corresponding manual baseline already fails with the overlay, which also limits using it as a story depiction of an ordinary pre-deployment day.

## Falsification and next measurement

Use time-stamped release, onset, intervention, validation and completion observations over both ordinary and synchronized start-up days. Hold out whole sites, layouts or commissioning batches where appropriate. Measure service-time tails, incidents without usable demonstrations, autonomous recoveries that send delayed manual jobs into the same peak, and rerouting when an operator is unavailable. Apply the proposed staffing rule to those traces with the existing roster's priorities, breaks and minimum coverage. If peak demand, regulatory requirements or an on-call guarantee still require two operators, the supported result is fewer task minutes or callouts. The model does not infer employment rates, company decisions, physical safety, causal learning gains or the probability of a shift disappearing.
