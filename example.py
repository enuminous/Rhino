from rhino import RhinoEvaluator, Shock

baseline = {
    "service":1.0,
    "consistency":1.0,
    "reserve":1.0
}

def shock_fn(state,m):
    state["service"] = max(0,1-0.5*m)
    state["consistency"] = max(0,1-0.3*m*m)
    state["reserve"] = max(0,1-0.9*m)
    return state

invariants = [
    lambda s: s["consistency"] >= 0.8,
    lambda s: s["service"] >= 0.5
]

evaluator = RhinoEvaluator(
    baseline,
    critical_weights={"service":2.0,"consistency":2.0,"reserve":0.5}
)

print(evaluator.evaluate(
    Shock("novel_compound_event",0.75,0.95),
    shock_fn,
    invariants
))
