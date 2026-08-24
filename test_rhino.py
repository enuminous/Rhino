import unittest
from rhino import RhinoEvaluator, Shock

class TestRhino(unittest.TestCase):
    def test_zero_shock_retains_system(self):
        base = {"a":1.0,"b":1.0}
        def f(s,m): return s
        out = RhinoEvaluator(base).evaluate(Shock("none",0.0),f,[])
        self.assertAlmostEqual(out["performance_retention"],1.0)

    def test_large_shock_reduces_retention(self):
        base = {"a":1.0}
        def f(s,m):
            s["a"] = max(0.0,1.0-m)
            return s
        ev = RhinoEvaluator(base)
        low = ev.evaluate(Shock("x",0.2),f,[])
        high = ev.evaluate(Shock("x",0.8),f,[])
        self.assertGreater(low["performance_retention"],high["performance_retention"])

    def test_invariant_failure_detected(self):
        base = {"a":1.0}
        def f(s,m):
            s["a"] = 0.1
            return s
        inv = [lambda s:s["a"]>=0.5]
        out = RhinoEvaluator(base).evaluate(Shock("x",1.0),f,inv)
        self.assertEqual(out["invariant_survival"],0.0)

if __name__ == "__main__":
    unittest.main()
