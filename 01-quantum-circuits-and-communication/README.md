# Quantum Circuits and Communication

This project focuses on basic quantum circuit construction, measurement behavior, quantum key distribution, and reversible arithmetic.

## Approach

The modules use Qiskit circuits and the basic simulator to construct small single-qubit and multi-qubit circuits, measure outcomes, model BB84 communication, and build reversible logic blocks.

## Key Files

- `circuits.py` - single-qubit gates, entanglement, oracle-style circuits, and a small QFT-style circuit.
- `measurement_simulation.py` - simulator-based measurements for selected circuits.
- `bb84_key_distribution.py` - BB84-style message encoding, basis selection, decoding, and optional intercept-resend behavior.
- `reversible_arithmetic.py` - reversible AND, OR, XOR, unsigned addition, and signed encode/decode helpers.

## Running Locally

Install dependencies from the repository root, then import the functions you want to inspect:

```bash
python - <<'PY'
from importlib.machinery import SourceFileLoader

mod = SourceFileLoader("bb84", "01-quantum-circuits-and-communication/bb84_key_distribution.py").load_module()
print(mod.QuantumAgent)
PY
```
