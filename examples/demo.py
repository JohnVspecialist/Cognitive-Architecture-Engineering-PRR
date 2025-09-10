from cae_prr.unified_engine import UnifiedEngine

engine = UnifiedEngine(config={"cae": {}, "prr": {}})
result = engine.run("Hello Cognitive Architecture + PRR")
print(result)
