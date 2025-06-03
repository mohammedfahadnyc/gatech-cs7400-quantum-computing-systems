# CS 7400 Quantum Computing

This repository collects quantum computing projects completed as part of Georgia Tech's CS 7400 Quantum Computing course. The work spans foundational circuit construction, quantum communication, algorithm analysis, NISQ-era compilation, error correction, and QAOA-based optimization.

The implementations use Qiskit to build, simulate, and transpile quantum circuits while exploring both algorithmic behavior and hardware-aware execution constraints.

## Repository Structure

```text
.
├── 01-quantum-circuits-and-communication/
├── 02-quantum-algorithms/
├── 03-qubit-mapping-and-routing/
├── 04-error-correction-and-qaoa/
├── 05-research-review/
├── requirements.txt
└── README.md
```

## Projects

| Project | Summary |
| --- | --- |
| Quantum Circuits and Communication | Builds basic circuits, measurement simulations, BB84 key distribution, and reversible arithmetic components. |
| Quantum Algorithms | Implements and analyzes Deutsch, Deutsch-Jozsa, Bernstein-Vazirani, Simon, Grover, superdense coding, and state preparation circuits. |
| Qubit Mapping and Routing | Evaluates transpilation bases, routing overhead, coupling maps, SWAP insertion, and noise-aware qubit mappings for benchmark circuits. |
| Error Correction and QAOA | Implements bit-flip and phase-flip quantum error correction decoders plus a QAOA MaxCut solver. |
| Research Review | Contains a concise review of a quantum computing research paper and the source paper used for analysis. |

## Technologies

- Python
- Qiskit
- NumPy
- NetworkX
- OpenQASM benchmark circuits

## Running Locally

Create a Python environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Most modules expose functions that return `QuantumCircuit` objects or simulation results. Example:

```bash
python - <<'PY'
from importlib.machinery import SourceFileLoader

circuits = SourceFileLoader(
    "circuits",
    "01-quantum-circuits-and-communication/circuits.py",
).load_module()

print(circuits.q1b())
PY
```

The original course instruction bundles and submission metadata are intentionally excluded from version control.
