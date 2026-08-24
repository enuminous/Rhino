# RHINO Theory

## 1. Problem

Many systems are robust to small perturbations and fragile to large, unfamiliar ones.

High-impact novel operations may include:
- abrupt demand spikes,
- correlated subsystem failures,
- unusual input distributions,
- simultaneous resource loss,
- topology changes,
- unexpected operating modes,
- compound disturbances.

RHINO evaluates whether critical structure survives these shocks.

## 2. Pre-shock state

Let the healthy system state be:

`x_0`

A shock `p` produces:

`x_1 = F(x_0, p)`

## 3. Invariant survival

Let critical invariants be:

`I = {I_1,...,I_k}`

Survival score:

`S_I = passed_invariants / total_invariants`

## 4. Performance retention

For critical capability score `Q`:

`R_Q = Q_after / (Q_before + eps)`

clipped to `[0,1]` where appropriate.

## 5. Structural damage

For state distance:

`D = dist(x_after, x_before)`

Structural retention:

`R_S = 1 - normalized(D)`

## 6. Shock amplification

If perturbation magnitude is `|p|` and system loss is `L`:

`A = L / (|p| + eps)`

High `A` indicates fragile amplification.

## 7. Graceful failure

A robust system may not remain fully functional.

Instead, it should:
- preserve critical invariants,
- shed lower-priority capabilities,
- avoid uncontrolled cascades,
- retain recoverability.

Candidate graceful-failure score:

`G = critical_retention - uncontrolled_failure_penalty`

## 8. Robustness margin

Let `m` be shock magnitude.

Define:

`M = max m such that critical invariants remain satisfied`

## 9. Novelty dimension

Novel shocks should differ structurally from calibration conditions.

Examples:
- held-out combinations,
- unseen topology changes,
- unseen direction of perturbation.

## 10. EFMW interpretation

The EFMW-inspired layer is recursive evaluation across:
- state,
- invariants,
- capability,
- dependencies,
- recovery.

The key question is not merely:
"Did the system fail?"

It is:
"What structure survived, what broke, and what remains recoverable?"

## 11. Falsifiable prediction

RHINO should add value where:
- shocks are compound,
- invariant survival matters,
- failure modes differ by perturbation type,
- recovery potential matters.

If ordinary stress testing and robustness metrics capture the same outcomes, RHINO adds no justified complexity.
