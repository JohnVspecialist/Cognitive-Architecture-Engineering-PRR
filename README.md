# Cognitive Architecture Engineering + Polyrhythmic Reasoning (PRR)

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

This repository unifies **Cognitive Architecture Engineering (CAE)** with **Polyrhythmic Reasoning (PRR)**.  

- **CAE** provides the shell: invariants, observability, boundaries, safety, and accountability.  
- **PRR** provides the core: multi-threaded reasoning loops in polyrhythmic cadence (4/4 vs 5/4).  

🚀 How to Use This / What It’s For

This project is a Cognitive Architecture + Polyrhythmic Reasoning (PRR) Engine.
It’s designed to demonstrate how reasoning “invariants” (rules that must always hold true) can be applied to model outputs, ensuring that the system stays logically consistent and interpretable.

🔹 What It’s For

Provides a unified engine that combines two layers:

CAE (Cognitive Architecture Engine): Handles invariants, checks consistency, and wraps outputs.

PRR (Polyrhythmic Reasoning): Applies reasoning loops in parallel patterns (like musical polyrhythms) for richer logic chains.

Serves as a playground for testing AI reasoning.

A starting point for secure, testable model pipelines where reasoning can be verified with automated checks.

---

## ✨ Features
- Deterministic invariants over probabilistic reasoning.  
- Production-focused observability hooks.  
- Extensible reasoning loops embedded in architectural guarantees.  

---

## 🚀 Quick Start

🔹 How to Use

Clone the repo & set up environment

git clone <your-repo-url>
cd Cognitive-Architecture-Engineering-PRR
python3 -m venv .venv
source .venv/bin/activate
pip install -e .


Run the demo

python examples/demo.py


Example output:

[CAE] Checking invariants...
[PRR] Running reasoning loop...
{'cae_wrapped': 'Processed: Hello Cognitive Architecture + PRR'}


Run the tests

PYTHONPATH=src pytest -v


Example output (green = success):

tests/test_engine.py::test_engine_runs PASSED
tests/test_unified_engine.py::TestUnifiedEngine::test_invariants_hold PASSED


Extend it

Add new invariants to check different properties of outputs.

Build new PRR loops in src/prr/loops.py.

Plug in different reasoning strategies.

-----------------------------------------------------

another option:

Clone the repo:
```bash
git clone https://github.com/JohnVspecialist/Cognitive-Architecture-Engineering-PRR.git
cd Cognitive-Architecture-Engineering-PRR
# Cognitive Architecture Engineering + Polyrhythmic Reasoning (PRR)

This repository unifies **Cognitive Architecture Engineering (CAE)** with **Polyrhythmic Reasoning (PRR)**.

- **CAE** provides the shell: invariants, observability, boundaries, safety, and accountability.
- **PRR** provides the core: multi-threaded reasoning loops in polyrhythmic cadence (4/4 vs 5/4).

## Features
- Deterministic invariants over probabilistic reasoning.
- Production-focused observability hooks.
- Extensible reasoning loops embedded in architectural guarantees.

## Usage
```bash
python examples/demo_unified.py
