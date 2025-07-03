from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, transpiler
from qiskit.transpiler import CouplingMap
from utils import get_benchmark_dict

workload_list = get_benchmark_dict("benchmarks/swap_benchmarks")


def create_coupling_maps():
    coupling_maps = {}

    def grid_edges(rows, cols):
        edges = []
        for r in range(rows):
            for c in range(cols):
                i = r * cols + c
                if c < cols - 1:
                    edges.append((i, i + 1))
                    edges.append((i + 1, i))
                if r < rows - 1:
                    edges.append((i, i + cols))
                    edges.append((i + cols, i))
        return edges

    def ring_edges(n):
        edges = []
        for i in range(n):
            edges.append((i, (i + 1) % n))
            edges.append(((i + 1) % n, i))
        return edges

    coupling_maps['GRID 5X5'] = CouplingMap(grid_edges(5, 5))
    coupling_maps['GRID 5X4'] = CouplingMap(grid_edges(5, 4))
    coupling_maps['GRID 7X3'] = CouplingMap(grid_edges(7, 3))
    coupling_maps['RING 20'] = CouplingMap(ring_edges(20))

    return coupling_maps


def average_depth_change():
    output_dict = {}
    coupling_maps = create_coupling_maps()

    for name, circuit in workload_list.items():
        original_depth = circuit.depth()
        depth_sum = 0

        for cmap in coupling_maps.values():
            transpiled = transpile(
                circuit.copy(),
                coupling_map=cmap,
                routing_method='sabre',
                optimization_level=1
            )
            depth_sum += transpiled.depth()

        avg_depth = depth_sum / len(coupling_maps)
        output_dict[name] = float(avg_depth - original_depth)

    return output_dict


def average_nswap_change():
    output_dict = {}
    coupling_maps = create_coupling_maps()

    for name, circuit in workload_list.items():
        swap_sum = 0

        for cmap in coupling_maps.values():
            transpiled = transpile(
                circuit.copy(),
                coupling_map=cmap,
                routing_method='sabre',
                optimization_level=1
            )
            swap_sum += transpiled.count_ops().get('swap', 0)

        avg_swaps = swap_sum / len(coupling_maps)
        output_dict[name] = avg_swaps

    return output_dict
