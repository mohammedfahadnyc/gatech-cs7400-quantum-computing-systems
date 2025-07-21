from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator


def encoder():
    """
    Your implementation of bit-flip QEC encoder that works for both 1 bit-flip error and 2 bit-flip errors
    Args:
        None
    Return:
        QuantumCircuit
    """

    qc = QuantumCircuit(3)
    ############################################################################
    # Student code begin
    ############################################################################

    qc.cx(0, 1)
    qc.cx(0, 2)

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def decoder1():
    """
    Your implementation of bit-flip QEC decoder that works for 1 bit-flip error
    Args:
        None
    Return:
        QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qc = QuantumCircuit(3)

    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.ccx(1, 2, 0)
    qc.cx(1, 2)
    qc.cx(0, 1)

    qc.cx(0, 2)
    qc.cx(0, 1)

    ############################################################################
    # Student code end
    ############################################################################
    return qc


def decoder2():
    """
    Your implementation of bit-flip QEC decoder that works for 2 bit-flip errors
    Args:
        None
    Return:
        QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qc = QuantumCircuit(3)

    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.x(1)
    qc.ccx(1, 2, 0)
    qc.x(1)
    qc.cx(1, 2)
    qc.cx(0, 1)

    qc.cx(0, 2)
    qc.cx(0, 1)

    ############################################################################
    # Student code end
    ############################################################################

    return qc