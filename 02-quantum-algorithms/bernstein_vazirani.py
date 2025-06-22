from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from math import pi


def bv_ideal():
    '''
    Implement the Bernstein Vazirani (BV) algorithm circuit with an oracle function with a secrete key of "0101010"
    Args:
        None
    Return:
        qcirc: A QuantumCircuit object of your implementation of BV algorithm
    '''
    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################

    secret_key = "0101010"
    n = len(secret_key)

    qcirc = QuantumCircuit(n + 1)

    for i in range(n):
        qcirc.h(i)

    qcirc.x(n)
    qcirc.h(n)

    for i in range(n):
        if secret_key[i] == '1':
            qcirc.cx(i, n)

    for i in range(n):
        qcirc.h(i)

    ############################################################################
    # Student code end
    ############################################################################

    return qcirc


def bv_noisy():
    '''
    Recreate your BV circuit with all H gates replaced with U(pi/2, pi/16, pi)

    Args:
        None
    Return:
        qcirc: A QuantumCircuit object of your implementation of BV algorithm with simulated noise
    '''
    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################

    secret_key = "0101010"
    n = len(secret_key)

    qcirc = QuantumCircuit(n + 1)

    for i in range(n):
        qcirc.u(pi / 2, pi / 16, pi, i)

    qcirc.x(n)
    qcirc.u(pi / 2, pi / 16, pi, n)

    for i in range(n):
        if secret_key[i] == '1':
            qcirc.cx(i, n)

    for i in range(n):
        qcirc.u(pi / 2, pi / 16, pi, i)

    ############################################################################
    # Student code end
    ############################################################################

    return qcirc