from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import math

"""
In this question, you need to design quantum circuits to generate the given quantum states in Dirac's notations.
For each part, return a QuantumCircuit object that corresponds to the given state $\ket{\psi}$.
The Dirac's notations should be understood in Qiskit little-endian ordering.
You may not use the `initialize` instruction.
You can only use the following gates: `h, x, y, z, s, t, u, cu, rx, ry, rz, cx, crx, cry, crz, ccx`
"""


def q6a():
    '''
    Construct the quantum circuit to generate
        $$\ket{\psi}= \frac{1}{2}\ket{00} + \frac{1}{2}\ket{01} + \frac{1}{2}\ket{10} + \frac{1}{2}\ket{11}$$
    Args:
        None
    Return:
        qcirc: your QuantumCircuit object
    '''
    qcirc = QuantumCircuit(2)
    qcirc.h(0)
    qcirc.h(1)
    return qcirc


def q6b():
    '''
    Construct the quantum circuit to generate
        $$\ket{\psi}= \frac{1}{2}\ket{010} + \frac{\sqrt{3}}{2}\ket{101}$$
    Args:
        None
    Return:
        qcirc: your QuantumCircuit object
    '''
    qcirc = QuantumCircuit(3)

    theta = 2 * math.pi / 3

    qcirc.ry(theta, 2)

    qcirc.cx(2, 0)
    qcirc.x(1)
    qcirc.cx(2, 1)

    return qcirc


def q6c():
    '''
    Construct the quantum circuit to generate
        $$\ket{\psi}= \frac{1}{\sqrt{2}}\ket{01} - \frac{1}{\sqrt{2}}\ket{10}$$
    Args:
        None
    Return:
        qcirc: your QuantumCircuit object
    '''
    qcirc = QuantumCircuit(2)
    qcirc.x(1)
    qcirc.h(0)
    qcirc.cx(0, 1)
    qcirc.z(0)

    return qcirc


from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import math


def q6d():
    '''
    Construct the quantum circuit to generate
        $\ket{\psi}= \frac{1}{2}\ket{0001} + \frac{i}{2}\ket{0010} - \frac{1}{2}\ket{0100} - \frac{i}{2}\ket{1000}$
    Args:
        None
    Return:
        qcirc: your QuantumCircuit object
    '''
    qcirc = QuantumCircuit(4)

    
    

    
    qcirc.h(2)
    qcirc.h(3)

    
    qcirc.s(3)  
    qcirc.z(2)  

    
    
    qcirc.x(2)
    qcirc.x(3)
    qcirc.ccx(2, 3, 0)
    qcirc.x(2)
    qcirc.x(3)

    
    qcirc.x(2)
    qcirc.ccx(2, 3, 1)
    qcirc.x(2)

    
    

    return qcirc


def q6e():
    qcirc = QuantumCircuit(3)

    theta_2 = 2 * math.asin(1 / math.sqrt(3))
    qcirc.ry(theta_2, 2)

    qcirc.x(2)
    qcirc.cry(math.pi / 2, 2, 1)
    qcirc.x(2)

    qcirc.x(1)
    qcirc.x(2)
    qcirc.ccx(1, 2, 0)
    qcirc.x(1)
    qcirc.x(2)

    return qcirc