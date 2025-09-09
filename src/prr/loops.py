import itertools

def polyrhythmic_reasoning(query: str, steps: int = 4) -> list[dict]:
    """
    Generate reasoning steps in overlapping rhythmic cadences (4/4 vs 5/4).

    Args:
        query (str): The input prompt or question to reason about.
        steps (int): Number of steps to generate per rhythm.

    Returns:
        list[dict]: Structured reasoning outputs with 'analysis' and 'conclusion'.
    """
    rhythms = [
        [f"Step{i}" for i in range(steps)],       # 4/4 loop
        [f"Alt{i}" for i in range(steps + 1)]     # 5/4 loop
    ]

    combined = []
    for pair in itertools.zip_longest(*rhythms):
        combined.append([p for p in pair if p])

    results = []
    for i, layer in enumerate(combined):
        results.append({
            "analysis": f"{query} via {layer}",
            "conclusion": f"Result-{i}"
        })

    return results

