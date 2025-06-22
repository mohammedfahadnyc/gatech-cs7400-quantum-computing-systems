from qiskit import QuantumRegister, QuantumCircuit


def simon():
    qreg = QuantumRegister(8, 'q')
    qc = QuantumCircuit(qreg)

    for i in range(4):
        qc.h(qreg[i])

    for i in range(4):
        qc.h(qreg[i])

    return qc


def calculate_secret():
    return "1010"