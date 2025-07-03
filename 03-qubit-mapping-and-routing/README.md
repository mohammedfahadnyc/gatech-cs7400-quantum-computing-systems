# Qubit Mapping and Routing

This project explores NISQ compilation concerns: basis decomposition, device coupling constraints, routing overhead, and noise-aware qubit placement.

## Approach

The code loads OpenQASM benchmark circuits, transpiles them under different basis-gate and coupling-map assumptions, and measures depth or SWAP overhead introduced by routing. It also includes custom device mappings that account for edge-level gate reliability.

## Key Files

- `transpilation_baselines.py` - basis-gate decomposition experiments for benchmark circuits.
- `routing_overhead_analysis.py` - grid and ring coupling maps with average depth and SWAP overhead analysis.
- `noise_aware_mapping.py` - custom probabilistic CNOT-like gates and physical qubit mappings.
- `utils.py` - benchmark loading and readout mapping helpers.
- `benchmarks/swap_benchmarks/` - OpenQASM benchmark circuits.

## Running Locally

Install dependencies from the repository root, then run from this project directory so the benchmark path resolves:

```bash
cd 03-qubit-mapping-and-routing
python - <<'PY'
import routing_overhead_analysis as routing
print(routing.average_nswap_change())
PY
```
