def check_invariants(output: dict, invariants: dict) -> bool:
    """
    Ensure outputs meet deterministic invariants.
    
    Example:
    invariants = {
        "analysis": lambda x: isinstance(x, str),
        "conclusion": lambda x: x.startswith("Result")
    }
    """
    for key, condition in invariants.items():
        if key not in output:
            return False
        if not condition(output[key]):
            return False
    return True
