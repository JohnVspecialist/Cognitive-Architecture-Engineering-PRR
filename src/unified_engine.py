from src.cae.invariants import check_invariants
from src.cae.observability import log_event
from src.cae.boundaries import enforce_boundaries
from src.cae.safety import safety_filter
from src.prr.loops import polyrhythmic_reasoning

class UnifiedEngine:
    """
    The unified engine that embeds Polyrhythmic Reasoning (PRR)
    inside Cognitive Architecture Engineering (CAE).
    """

    def __init__(self, invariants: dict):
        self.invariants = invariants

    def run(self, query: str):
        log_event("START_QUERY", {"query": query})

        # Step 1: Generate reasoning using PRR
        results = polyrhythmic_reasoning(query)

        # Step 2: Apply CAE layers (boundaries, safety, invariants)
        safe_results = [safety_filter(enforce_boundaries(r)) for r in results]
        valid = [r for r in safe_results if check_invariants(r, self.invariants)]

        log_event("END_QUERY", {"valid_results": len(valid)})
        return valid
