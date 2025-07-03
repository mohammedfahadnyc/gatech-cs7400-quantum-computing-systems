from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, transpiler
from utils import get_benchmark_dict

workload_list = get_benchmark_dict("benchmarks/swap_benchmarks")

def q1a():
    '''
    Decompose the benchmark circuits using qiskit transpile function with basis gates set [cx,u],
    and return a dictionary of benchmark circuits' names as keys and transpiled circuits as values.
    '''
    output_dict = {}
    ############################################################################
    # Student code begin
    ############################################################################
    for name, circuit in workload_list.items():
        transpiled_circuit = transpile(circuit, basis_gates=['cx', 'u'])
        output_dict[name] = transpiled_circuit
    ############################################################################
    # Student code end
    ############################################################################
    return output_dict


def q1b():
    '''
    Decompose the benchmark circuits using qiskit transpile function with basis gates set [cx,rx,ry,rz],
    and return a dictionary of benchmark circuits' names as keys and transpiled circuits as values.
    '''
    output_dict = {}
    ############################################################################
    # Student code begin
    ############################################################################
    for name, circuit in workload_list.items():
        transpiled_circuit = transpile(circuit, basis_gates=['cx', 'rx', 'ry', 'rz'])
        output_dict[name] = transpiled_circuit
    ############################################################################
    # Student code end
    ############################################################################
    return output_dict
