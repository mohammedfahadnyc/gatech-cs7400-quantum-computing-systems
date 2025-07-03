from qiskit import QuantumCircuit
from qiskit.circuit.library import CUGate
import math
import numpy as np


def cx_ideal():
    qc = QuantumCircuit(2)
    qc.append(CUGate(np.pi, 0, np.pi, 0), [0, 1])
    studentGate = qc.to_gate(label="cx_ideal")
    return studentGate


def cx_p_gate(p, label):
    theta = 2 * np.arcsin(np.sqrt(p))
    qc = QuantumCircuit(2)
    qc.cry(theta, 0, 1)
    return qc.to_gate(label=label)


def cx_p95():
    studentGate = cx_p_gate(0.95, "cx_p95")
    return studentGate


def cx_p70():
    studentGate = cx_p_gate(0.70, "cx_p70")
    return studentGate


def q3c_edge_gates():
    edge_gates = {
        "01": cx_p_gate(0.99, "cx_p99"),
        "12": cx_p_gate(0.90, "cx_p90"),
        "23": cx_p_gate(0.80, "cx_p80"),
        "03": cx_p_gate(0.75, "cx_p75"),
    }
    return edge_gates


def q3c_device_qubit_route_mapping():
    qubit_mapping = {0: 1, 1: 0, 2: 2, 3: 3}
    return qubit_mapping


def q3c_device_compatible_physical_circuit():
    qc = QuantumCircuit(4)
    gates = q3c_edge_gates()
    logical_to_physical = q3c_device_qubit_route_mapping()

    qc.append(gates["01"], [logical_to_physical[0], logical_to_physical[1]])
    qc.append(gates["12"], [logical_to_physical[0], logical_to_physical[2]])
    qc.append(gates["23"], [logical_to_physical[2], logical_to_physical[3]])
    qc.append(gates["12"], [logical_to_physical[0], logical_to_physical[2]])
    qc.append(gates["23"], [logical_to_physical[2], logical_to_physical[3]])

    return qc


def q3c_device_qubit_read_mapping():
    qubit_mapping = {0: 1, 1: 0, 2: 2, 3: 3}
    return qubit_mapping


def q3d_edge_gates():
    edge_gates = {
        "01": cx_p_gate(0.850, "cx_p850"),
        "12": cx_p_gate(0.825, "cx_p825"),
        "13": cx_p_gate(0.975, "cx_p975"),
        "34": cx_p_gate(0.990, "cx_p990"),
    }
    return edge_gates


def q3d_device_qubit_route_mapping():
    qubit_mapping = {0: 1, 1: 3, 2: 0, 3: 2}
    return qubit_mapping


def q3d_device_compatible_physical_circuit():
    qc = QuantumCircuit(5)
    gates = q3d_edge_gates()
    logical_to_physical = q3d_device_qubit_route_mapping()

    qc.append(gates["13"], [logical_to_physical[0], logical_to_physical[1]])
    qc.append(gates["01"], [logical_to_physical[0], logical_to_physical[2]])
    qc.append(gates["12"], [logical_to_physical[0], logical_to_physical[3]])

    return qc


def q3d_device_qubit_read_mapping():
    qubit_mapping = {0: 2, 1: 0, 2: 3, 3: 1, 4: None}
    return qubit_mapping
