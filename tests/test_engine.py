from cae_prr.unified_engine import UnifiedEngine

def test_engine_runs():
    engine = UnifiedEngine(config={"cae": {}, "prr": {}})
    result = engine.run("Test input")
    assert isinstance(result, dict)
    assert "cae_wrapped" in result
    assert "Processed: Test input" in result["cae_wrapped"]
