from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile


def deutsch_f1_oracle():
    '''
    f(0) = 0, f(1) = 0
    '''
    qcirc = QuantumCircuit(2)
    return qcirc


def deutsch_f2_oracle():
    '''
    f(0) = 1, f(1) = 0
    '''
    qcirc = QuantumCircuit(2)
    qcirc.x(0)
    qcirc.cx(0, 1)
    qcirc.x(0)
    return qcirc


def deutsch_f3_oracle():
    '''
    f(0) = 0, f(1) = 1
    '''
    qcirc = QuantumCircuit(2)
    qcirc.cx(0, 1)
    return qcirc


def deutsch_f4_oracle():
    '''
    f(0) = 1, f(1) = 1
    '''
    qcirc = QuantumCircuit(2)
    qcirc.x(1)
    return qcirc


def deutsch_jozsa_oracle():
    '''
    g(x) = 0 if x is even
    g(x) = 1 if x is odd
    '''
    qcirc = QuantumCircuit(5)  

    
    
    
    qcirc.cx(0, 4)

    return qcirc