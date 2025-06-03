from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
import numpy as np

def _q1a_for_q2():
    qc = QuantumCircuit(4)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.id(0)
    qc.x(1)
    qc.y(2)
    qc.z(3)
    return qc

def _q1b_for_q2():
    qc = QuantumCircuit(3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    return qc

def _q1c_for_q2():
    qc = QuantumCircuit(6)
    qc.x(5)       # Flip ancilla (q5)
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

def _q1d_for_q2():

    qc = QuantumCircuit(2)
    qc.h(1)
    qc.cp(np.pi/2, 1, 0)
    qc.h(0)
    qc.swap(0, 1)
    return qc

def q2a():
    qc = _q1a_for_q2()
    qr = QuantumRegister(4, 'q')
    cr = ClassicalRegister(4, 'c')
    qc_measure = QuantumCircuit(qr, cr)
    qc_measure.compose(qc, inplace=True)
    qc_measure.measure(qr, cr)
    simulator = BasicSimulator()
    compiled_circuit = transpile(qc_measure, simulator)
    job = simulator.run(compiled_circuit, shots=10000)
    result = job.result()
    counts = result.get_counts(compiled_circuit)


    target_state = '1010'
    count_target = counts.get(target_state, 0)
    total_shots = sum(counts.values())
    return float(count_target) / float(total_shots) if total_shots > 0 else 0.0

def q2b():
    qc = _q1b_for_q2()
    qr = QuantumRegister(3, 'q')
    cr = ClassicalRegister(1, 'c')
    qc_measure = QuantumCircuit(qr, cr)
    qc_measure.compose(qc, inplace=True)
    qc_measure.measure(0, 0)  # Measure qubit 0 only
    simulator = BasicSimulator()
    compiled_circuit = transpile(qc_measure, simulator)
    job = simulator.run(compiled_circuit, shots=10000)
    result = job.result()
    counts = result.get_counts(compiled_circuit)
    target_state = '1'
    count_target = counts.get(target_state, 0)
    total_shots = sum(counts.values())
    return float(count_target) / float(total_shots) if total_shots > 0 else 0.0

def q2c():
    qc = _q1c_for_q2()
    qr = QuantumRegister(6, 'q')
    cr = ClassicalRegister(3, 'c')
    qc_measure = QuantumCircuit(qr, cr)
    qc_measure.compose(qc, inplace=True)
    qc_measure.measure([0, 1, 2], [0, 1, 2])
    simulator = BasicSimulator()
    compiled_circuit = transpile(qc_measure, simulator)
    job = simulator.run(compiled_circuit, shots=10000)
    result = job.result()
    counts = result.get_counts(compiled_circuit)
    target_state = '010'
    count_target = counts.get(target_state, 0)
    total_shots = sum(counts.values())
    return float(count_target) / float(total_shots) if total_shots > 0 else 0.0

def q2d():
    qc_initial = _q1d_for_q2()

    num_qubits = qc_initial.num_qubits
    qr = QuantumRegister(num_qubits, 'q')
    cr = ClassicalRegister(1, 'c')
    qc_measure = QuantumCircuit(qr, cr)
    qc_measure.compose(qc_initial, qubits=list(range(num_qubits)), inplace=True)


    qc_measure.h(qr[1])
    qc_measure.measure(qr[1], cr[0])

    simulator = BasicSimulator()
    compiled_circuit = transpile(qc_measure, simulator)
    job = simulator.run(compiled_circuit, shots=10000)
    result = job.result()
    counts = result.get_counts(compiled_circuit)

    target_state = '0'
    count_target = counts.get(target_state, 0)
    total_shots = sum(counts.values())
    return float(count_target) / float(total_shots) if total_shots > 0 else 0.0
