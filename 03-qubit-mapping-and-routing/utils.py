import glob
import os
from qiskit import QuantumCircuit

def get_benchmark_dict(path):
    """
    Finds and reads benchmark quantum circuits from *.qasm files in the given
    path and store them in a dict using *.qasm filenames as keys and
    the QuantumCircuit objects as values.
    Args:
        path: str
    Return:
        out_dict: dict
    """
    list_qasm = glob.glob(os.path.join(path,'*.qasm'))
    out_dict = {}
    for qasm_file in list_qasm:
        circuit_name = os.path.splitext(os.path.basename(qasm_file))[0]
        circuit = QuantumCircuit.from_qasm_file(qasm_file)
        circuit.name = circuit_name
        out_dict.update({circuit_name:circuit})
    
    return out_dict

def map_target(physical_state: str, logical_size: int, readout_mapping: dict):
    """
    Maps physical qubit reading from simulator run to logical qubit results
    of size logical_size in qiskit default little endian ordering
    Args:
        physical_state: str
        logical_size: int
        readout_mapping: dict
    Return:
        logical_state: str
    """
    logical_state = ["0"]*logical_size
    for key, value in readout_mapping.items():
        if value is not None:
            assert value in range(logical_size)
            logical_state[value] = physical_state[len(physical_state)-1-key]
    return "".join(logical_state[::-1])