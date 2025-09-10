from cae.core import CAEController
from prr.loops import PRRReasoner

class UnifiedEngine:
    def __init__(self, config):
        self.cae = CAEController(config.get("cae", {}))
        self.prr = PRRReasoner(config.get("prr", {}))

    def run(self, input_text: str):
        self.cae.check_invariants(input_text)
        reasoning_output = self.prr.reason(input_text)
        return self.cae.wrap_output(reasoning_output)
