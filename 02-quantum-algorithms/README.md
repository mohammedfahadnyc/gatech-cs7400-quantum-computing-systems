# Quantum Algorithms

This project implements several canonical quantum algorithms and supporting circuit constructions in Qiskit.

## Approach

The modules construct algorithm-specific circuits, oracle components, and post-processing helpers. The focus is on understanding how each algorithm transforms quantum state and how the measured result encodes the target property.

## Key Files

- `deutsch_algorithms.py` - Deutsch and Deutsch-Jozsa oracle circuits.
- `superdense_coding.py` - Bell-pair preparation, two-bit encoding, and decoding.
- `bernstein_vazirani.py` - ideal and noisy Bernstein-Vazirani circuits.
- `simon_period_finding.py` - Simon-style circuit scaffold and secret-string helper.
- `grover_search.py` - Grover iteration circuit and target-state probability post-processing.
- `state_preparation.py` - state preparation circuits for selected Dirac-notation target states.

## Running Locally

Install dependencies from the repository root, then import a module directly:

```bash
python - <<'PY'
from importlib.machinery import SourceFileLoader

grover = SourceFileLoader("grover", "02-quantum-algorithms/grover_search.py").load_module()
qc = grover.grover(1)
print(qc)
print(grover.post_processing(qc))
PY
```
