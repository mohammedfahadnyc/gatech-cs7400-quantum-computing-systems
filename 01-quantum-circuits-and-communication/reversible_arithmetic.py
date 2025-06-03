from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.providers.basic_provider import BasicSimulator


def encoder(x: int = 0, y: int = 0, n=4):
    assert x >= 0 and x < 2 ** n and isinstance(n, int)
    assert y >= 0 and y < 2 ** n and isinstance(n, int)
    qc = QuantumCircuit(n * 2)
    for i in range(n):
        if x & (1 << i): qc.x(i)
        if y & (1 << i): qc.x(n + i)
    return qc


def decoder(qc: QuantumCircuit, n=4):
    assert n >= 1 and isinstance(qc, QuantumCircuit)
    simulator = BasicSimulator()
    qc.measure(list(range(n)), list(range(n)))
    cc = transpile(qc, simulator)
    result = simulator.run(cc, shots=1).result().get_counts().keys()
    value = next(iter(result))
    return int(value[::-1], 2)


def quantum_and():
    qc = QuantumCircuit(3)
    qc.ccx(0, 1, 2)
    qc.swap(0, 2)
    return qc


def quantum_or():
    qc = QuantumCircuit(3)
    qc.x(0)
    qc.x(1)
    qc.ccx(0, 1, 2)
    qc.x(2)
    qc.swap(0, 2)
    return qc


def quantum_xor():
    qc = QuantumCircuit(2)
    qc.cx(1, 0)
    return qc


def quantum_adder():
    qc = QuantumCircuit(8)
    qc.cx(0, 4)
    qc.cx(1, 5)
    qc.cx(2, 6)
    qc.cx(3, 7)
    qc.ccx(0, 4, 1)
    qc.ccx(1, 5, 2)
    qc.ccx(2, 6, 3)
    qc.cx(0, 4)
    qc.cx(1, 5)
    qc.cx(2, 6)
    qc.cx(3, 7)
    qc.cx(4, 0)
    qc.cx(5, 1)
    qc.cx(6, 2)
    qc.cx(7, 3)
    return qc


def encoder_signed(x: int = 0, y: int = 0, n=4):
    min_val = -(2 ** (n - 1))
    max_val = 2 ** (n - 1) - 1



    if x < 0:
        x = (1 << n) + x
    if y < 0:
        y = (1 << n) + y

    return encoder(x, y, n)


def decoder_signed(qc: QuantumCircuit, n=4):
    result = decoder(qc, n)

    if result >= (1 << (n - 1)):
        result = result - (1 << n)

    return result
