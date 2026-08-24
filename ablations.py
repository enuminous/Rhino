from benchmark import baseline, compound_shock, invariants
from rhino import RhinoEvaluator, Shock

if __name__ == "__main__":
    full = RhinoEvaluator(
        baseline,
        critical_weights={"critical_service":2.0,"consistency":1.5}
    ).evaluate(Shock("compound",0.8,0.9),compound_shock,invariants)

    unweighted = RhinoEvaluator(
        baseline
    ).evaluate(Shock("compound",0.8,0.9),compound_shock,invariants)

    print("full performance retention:", full["performance_retention"])
    print("unweighted performance retention:", unweighted["performance_retention"])
