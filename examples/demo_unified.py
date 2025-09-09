import os, sys

# Add repo root to Python path so imports like "from src..." work
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.unified_engine import UnifiedEngine

if __name__ == "__main__":
    invariants = {
        "analysis": lambda x: isinstance(x, str) and len(x) > 0,
        "conclusion": lambda x: x.startswith("Result")
    }

    engine = UnifiedEngine(invariants)
    output = engine.run("Test prompt about system resilience")
    print("Unified Engine Output:")
    for item in output:
        print(item)
