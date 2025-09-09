def enforce_boundaries(output: dict) -> dict:
    """
    Clamp outputs into a deterministic schema so they can be validated downstream.

    Example:
    Ensures 'analysis' and 'conclusion' keys always exist, even if PRR forgot them.
    """
    normalized = dict(output)  # copy to avoid side-effects
    if "analysis" not in normalized:
        normalized["analysis"] = "N/A"
    if "conclusion" not in normalized:
        normalized["conclusion"] = "N/A"
    return normalized
