# Shock Model

## Shock schema

```json
{
  "name": "compound_resource_loss",
  "magnitude": 0.8,
  "novelty": 0.9,
  "affected_dimensions": ["capacity", "redundancy", "latency"]
}
```

## System state schema

```json
{
  "capacity": 1.0,
  "redundancy": 1.0,
  "consistency": 1.0,
  "critical_service": 1.0
}
```

## Robustness evaluation

For each shock:
1. snapshot pre-shock state
2. apply perturbation
3. evaluate critical invariants
4. measure capability retention
5. quantify structural damage
6. measure amplification
7. estimate recovery potential

## Robustness curve

Evaluate across increasing magnitudes:

`m_1 < m_2 < ... < m_n`

Plot retained coherence against shock magnitude.

## Failure classification

Suggested classes:
- NONE
- GRACEFUL
- DEGRADED
- BOUNDARY_BREACH
- CASCADE
- UNRECOVERABLE
