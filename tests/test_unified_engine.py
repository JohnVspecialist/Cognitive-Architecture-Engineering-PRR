import unittest
from cae_prr.unified_engine import UnifiedEngine

class TestUnifiedEngine(unittest.TestCase):
    def test_invariants_hold(self):
        # create engine with minimal config
        engine = UnifiedEngine(config={"cae": {}, "prr": {}})

        # run once
        output = engine.run("Hello World")

        # your engine returns {"cae_wrapped": "<string>"}
        text = output["cae_wrapped"]

        # invariants on the returned text
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 0)
        self.assertTrue(text.startswith("Processed"))

if __name__ == "__main__":
    unittest.main()

