# question3.py
import numpy as np
import numpy.typing as npt
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator

class QuantumAgent(object):
    def __init__(self):
        self.backend = BasicSimulator()

    def generate_basis(self, n):
        self.basis = np.random.randint(0, 2, n)


    def encode_message(self, message):

        n = len(message)
        self.qubits = []
        self.generate_basis(n=n)

        for i in range(n):
            qc = QuantumCircuit(1)
            s = message[i]
            b = self.basis[i]


            if b == 0:
                # Computational basis
                if s == 1:
                    qc.x(0)
            else:
                # Hadamard basis
                if s == 1:
                    qc.x(0)
                qc.h(0)


            self.qubits.append(qc)

    def decode_qubits(self, qubits):

        n = len(qubits)
        self.recovered_message = np.zeros(n, dtype=np.int8)
        self.generate_basis(n=n)

        for i in range(n):

            qc = QuantumCircuit(1, 1)
            qc = qc.compose(qubits[i])

            b_prime = self.basis[i]


            if b_prime == 1:
                qc.h(0)


            qc.measure(0, 0)
            result = self.backend.run(run_input=qc, shots=1).result()
            bit_str = list(result.get_counts().keys())[0]
            self.recovered_message[i] = int(bit_str)

def bb84(message: npt.ArrayLike, alice: QuantumAgent, bob: QuantumAgent, eve: QuantumAgent = None):

    n = len(message)
    alice.encode_message(message=message)

    if eve is None:

        bob.decode_qubits(alice.qubits)
    else:

        eve.decode_qubits(alice.qubits)
        eve.encode_message(eve.recovered_message)
        bob.decode_qubits(eve.qubits)


    I_mask = (alice.basis == bob.basis)
    num_matching = np.sum(I_mask)


    if num_matching < np.floor(n / 2):
        return False


    original_bits = np.array(message)[I_mask]
    recovered_bits = bob.recovered_message[I_mask]
    num_agree = np.sum(original_bits == recovered_bits)


    return (num_agree >= np.floor(num_matching / 2))
