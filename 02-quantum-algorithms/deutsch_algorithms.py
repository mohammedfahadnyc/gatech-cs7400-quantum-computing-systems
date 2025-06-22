from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator
import math


def qubit_preparation(n):
    """
    Prepare enough qubits based on the length of the information to be sent.
    Args:
        n: int of length of classical_information
    Return:
        qcirc: QuantumCircuit of prepared qubits
    """
    num_pairs = math.ceil(n / 2)
    num_qubits = 2 * num_pairs

    qcirc = QuantumCircuit(num_qubits)

    for i in range(num_pairs):
        alice_qubit = 2 * i
        bob_qubit = 2 * i + 1

        qcirc.h(alice_qubit)
        qcirc.cx(alice_qubit, bob_qubit)

    return qcirc


def qubit_encoding(prepared_qubits, classical_information):
    """
    Encode classical bits into quantum qubits using superdense coding.
    Args:
        prepared_qubits: QuantumCircuit of prepared Bell pairs
        classical_information: str
    Return:
        qcirc: QuantumCircuit of encoded qubits
    """
    qcirc = prepared_qubits.copy()

    n = len(classical_information)
    num_pairs = math.ceil(n / 2)

    for i in range(num_pairs):
        alice_qubit = 2 * i

        bit_idx_1 = 2 * i
        bit_idx_2 = 2 * i + 1

        bit1 = classical_information[bit_idx_1] if bit_idx_1 < n else '0'
        bit2 = classical_information[bit_idx_2] if bit_idx_2 < n else '0'

        if bit1 == '0' and bit2 == '1':
            qcirc.x(alice_qubit)
        elif bit1 == '1' and bit2 == '0':
            qcirc.z(alice_qubit)
        elif bit1 == '1' and bit2 == '1':
            qcirc.z(alice_qubit)
            qcirc.x(alice_qubit)

    return qcirc


def qubit_decoding(encoded_qubits, n):
    """
    Decode the quantum state back into classical information.
    Args:
        encoded_qubits: QuantumCircuit of encoded qubits
        n: int of original classical information length
    Return:
        restored_information: str
    """
    qcirc = encoded_qubits.copy()
    num_qubits = qcirc.num_qubits
    num_pairs = num_qubits // 2

    creg = ClassicalRegister(num_qubits)
    qcirc.add_register(creg)

    for i in range(num_pairs):
        alice_qubit = 2 * i
        bob_qubit = 2 * i + 1

        qcirc.cx(alice_qubit, bob_qubit)
        qcirc.h(alice_qubit)

        qcirc.measure(alice_qubit, alice_qubit)
        qcirc.measure(bob_qubit, bob_qubit)

    simulator = BasicSimulator()
    job = simulator.run(qcirc, shots=1)
    result = job.result()
    counts = result.get_counts()
    measured_string = list(counts.keys())[0]

    
    measured_string = measured_string.zfill(num_qubits)

    
    measured_bits = {i: measured_string[::-1][i] for i in range(num_qubits)}

    restored_bits = []
    for i in range(num_pairs):
        alice_qubit = 2 * i
        bob_qubit = 2 * i + 1

        restored_bits.append(measured_bits[alice_qubit])
        restored_bits.append(measured_bits[bob_qubit])

    restored_information = ''.join(restored_bits[:n])
    return restored_information