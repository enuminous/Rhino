# RHINO Architecture

## Pipeline

1. Healthy-State Snapshotter
2. Shock Generator
3. Novelty Gate
4. Perturbation Executor
5. Invariant Validator
6. Capability Retention Analyzer
7. Structural Damage Estimator
8. Amplification Analyzer
9. Recovery Potential Estimator
10. Robustness Reporter

## Inputs

- healthy baseline state
- perturbation family
- shock magnitude
- novelty metadata
- invariants
- critical capability weights

## Outputs

```json
{
  "invariant_survival": 0.80,
  "performance_retention": 0.71,
  "structural_retention": 0.66,
  "shock_amplification": 1.42,
  "graceful_failure": 0.74,
  "recovery_potential": 0.81
}
```

## Design principle

RHINO does not reward a system for staying online at any cost.

Critical boundaries and recoverability matter more than raw continuity.

## Integration

BISON can characterize overload-specific stress behavior.

JELLYFISH can model downstream cascades.

PHOENIX can evaluate actual post-shock recovery.

BEAVER can evaluate repair interventions after the shock.
