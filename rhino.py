from dataclasses import dataclass
from typing import Dict, List, Callable, Optional
import math
import copy

@dataclass
class Shock:
    name: str
    magnitude: float
    novelty: float = 1.0

class RhinoEvaluator:
    def __init__(self, baseline: Dict[str,float], critical_weights: Optional[Dict[str,float]] = None):
        self.baseline = copy.deepcopy(baseline)
        self.critical_weights = critical_weights or {}

    @staticmethod
    def clip01(x):
        return max(0.0, min(1.0, float(x)))

    def apply_shock(self, state: Dict[str,float], shock_fn: Callable[[Dict[str,float], float], Dict[str,float]], magnitude: float):
        return shock_fn(copy.deepcopy(state), magnitude)

    def invariant_survival(self, state, invariants: List[Callable[[Dict[str,float]], bool]]):
        if not invariants:
            return 1.0
        return sum(1 for f in invariants if f(state))/len(invariants)

    def performance_retention(self, after: Dict[str,float]):
        keys = [k for k in self.baseline if k in after]
        if not keys:
            return 0.0
        weights = {k:max(0.0,self.critical_weights.get(k,1.0)) for k in keys}
        total = sum(weights.values()) or 1.0
        vals = []
        for k in keys:
            b = self.baseline[k]
            a = after[k]
            if b == 0:
                retain = 1.0 if a == 0 else 0.0
            else:
                retain = self.clip01(a/b)
            vals.append(weights[k]*retain)
        return sum(vals)/total

    def structural_retention(self, after: Dict[str,float]):
        keys = [k for k in self.baseline if k in after]
        if not keys:
            return 0.0
        mse = sum((after[k]-self.baseline[k])**2 for k in keys)/len(keys)
        d = math.sqrt(mse)
        return max(0.0,1.0-d)

    def evaluate(self, shock: Shock, shock_fn, invariants=None):
        invariants = invariants or []
        before = copy.deepcopy(self.baseline)
        after = self.apply_shock(before, shock_fn, shock.magnitude)

        inv = self.invariant_survival(after,invariants)
        perf = self.performance_retention(after)
        structural = self.structural_retention(after)
        loss = 1.0 - (0.5*perf + 0.5*structural)
        amplification = loss/(max(1e-9,shock.magnitude))
        recovery_potential = self.clip01(0.5*inv + 0.5*structural)
        graceful = self.clip01(0.6*inv + 0.4*perf)

        return {
            "shock": shock.name,
            "magnitude": shock.magnitude,
            "novelty": shock.novelty,
            "invariant_survival": inv,
            "performance_retention": perf,
            "structural_retention": structural,
            "shock_amplification": amplification,
            "graceful_failure": graceful,
            "recovery_potential": recovery_potential,
            "after": after
        }
