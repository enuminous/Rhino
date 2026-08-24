# RHINO — EFMW Zoo #43

**Robustness under High-Impact Novel Operations**

RHINO is an experimental EFMW-inspired framework for testing whether a system retains essential coherence when subjected to severe, unfamiliar, and structurally different perturbations.

## Core question

> What remains intact when the system is hit by something large, unusual, and outside its comfortable operating envelope?

RHINO focuses on retained invariants, graceful degradation, recovery potential, and structural robustness under novel high-impact shocks.

## Primary outputs

- retained-coherence score
- invariant survival
- performance retention
- shock amplification
- graceful-failure score
- structural damage
- recovery potential
- robustness margin

## Repository contents

- `theory.md`
- `architecture.md`
- `shock_model.md`
- `limitations.md`
- `rhino.py`
- `benchmark.py`
- `ablations.py`
- `test_rhino.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_rhino.py
```

## Zoo position

FALCON #42 tests fast reaction under tight latency constraints.

**RHINO #43 asks what happens when the disturbance itself is large, novel, and potentially system-breaking.**
