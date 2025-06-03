from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import numpy as np

def q1a():
    qc = QuantumCircuit(4)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.id(0)  # Corrected identity gate
    qc.x(1)
    qc.y(2)
    qc.z(3)
    return qc

def q1b():
    qc = QuantumCircuit(3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    return qc

def q1c():
    qc = QuantumCircuit(6)
    qc.x(5)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.h(4)
    qc.h(5)
    qc.cx(0, 5)
    qc.cx(1, 5)
    qc.cx(2, 5)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.h(4)
    qc.h(5)
    return qc

def q1d():
    qc = QuantumCircuit(2)
    qc.h(1)
    qc.cp(np.pi/2, 1, 0)
    qc.h(0)
    qc.swap(0, 1)
    return qc

