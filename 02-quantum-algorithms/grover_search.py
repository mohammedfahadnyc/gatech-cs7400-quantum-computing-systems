from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.quantum_info import Statevector
import numpy as np


def grover(n: int):
    '''
    This function output Grover's algorithm circuit for a specific target.
    Implement the circuit for applying Rotation phase + Inversion around the mean n times,
    where n is a positive integer.
    Args:
        n: int of the number of times to apply (rotation + inversion)
    Return:
        qcirc: QuantumCircuit of your implementation of Grover's algorithm
    '''
    qcirc = None

    
    
    

    
    qcirc = QuantumCircuit(3)

    
    for i in range(3):
        qcirc.h(i)

    
    for _ in range(n):
        
        
        
        
        qcirc.x(0)
        qcirc.h(2)
        qcirc.ccx(0, 1, 2)  
        qcirc.h(2)
        qcirc.x(0)

        
        
        for i in range(3):
            qcirc.h(i)

        
        for i in range(3):
            qcirc.x(i)

        
        qcirc.h(2)
        qcirc.ccx(0, 1, 2)
        qcirc.h(2)

        
        for i in range(3):
            qcirc.x(i)

        
        for i in range(3):
            qcirc.h(i)

    
    
    

    return qcirc


def target_state():
    """
    What is the target state found by the Grover's circuit?
    Args:
        None
    Return:
        s: str of the target state
    """

    s = ""
    
    
    

    
    
    
    
    
    
    
    
    
    
    

    s = "110"

    
    
    

    return s


def post_processing(grover_qcirc):
    '''
    Args:
        grover_qcirc: QuantumCircuit returned by your grover function with input n
    Return:
        prob: float of the probability of finding the target state by running grover's algorithm n times
    '''

    prob = None
    
    
    

    
    statevector = Statevector.from_instruction(grover_qcirc)

    
    target_string = target_state()
    target_index = int(target_string, 2)

    
    amplitudes = statevector.data
    prob = abs(amplitudes[target_index]) ** 2

    
    
    

    return prob