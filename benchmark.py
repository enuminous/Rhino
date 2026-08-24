from rhino import RhinoEvaluator, Shock

baseline = {
    "capacity":1.0,
    "redundancy":1.0,
    "consistency":1.0,
    "critical_service":1.0
}

def compound_shock(state, m):
    state["capacity"] = max(0.0,1.0-0.8*m)
    state["redundancy"] = max(0.0,1.0-1.0*m)
    state["consistency"] = max(0.0,1.0-0.5*m*m)
    state["critical_service"] = max(0.0,1.0-0.6*m)
    return state

invariants = [
    lambda s: s["consistency"] >= 0.75,
    lambda s: s["critical_service"] >= 0.50,
    lambda s: s["capacity"] >= 0.30,
    lambda s: s["redundancy"] >= 0.20
]

if __name__ == "__main__":
    ev = RhinoEvaluator(
        baseline,
        critical_weights={
            "critical_service":2.0,
            "consistency":1.5,
            "capacity":1.0,
            "redundancy":1.0
        }
    )
    for m in [0.2,0.5,0.8,1.0]:
        print(ev.evaluate(
            Shock("compound",m,novelty=0.9),
            compound_shock,
            invariants
        ))
