# Error Correction and QAOA

This project combines simple quantum error correction circuits with a QAOA-based MaxCut solver.

## Approach

The QEC modules construct three-qubit repetition-style encoders and decoders for bit-flip and phase-flip recovery. The QAOA module builds a parameterized depth-one circuit for MaxCut, executes it on a simulator, and extracts the best cut value observed from sampled bitstrings.

## Key Files

- `bit_flip_qec.py` - bit-flip encoder and one-error/two-error decoder variants.
- `phase_flip_qec.py` - phase-flip encoder and decoder variants using Hadamard basis changes.
- `qaoa_maxcut.py` - `QAOASolver` class for simulated MaxCut experiments.

## Running Locally

Install dependencies from the repository root, then run a small MaxCut example:

```bash
python - <<'PY'
from importlib.machinery import SourceFileLoader
import networkx as nx

qaoa = SourceFileLoader("qaoa", "04-error-correction-and-qaoa/qaoa_maxcut.py").load_module()
solver = qaoa.QAOASolver(nx.cycle_graph(4), num_shots=256)
print(solver.solve())
PY
```
