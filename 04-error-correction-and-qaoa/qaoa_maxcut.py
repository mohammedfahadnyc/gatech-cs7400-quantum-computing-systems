# question3.py
import numpy as np
import networkx as nx
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.providers.basic_provider import BasicSimulator


class QAOASolver(object):
    def __init__(self, input_graph: nx.Graph, num_shots=1000):
        self.G = input_graph
        self.E = list(input_graph.edges())
        self.V = list(input_graph.nodes())
        self.gamma = np.random.uniform()
        self.beta = np.random.uniform()
        self.simulator = BasicSimulator()
        self.num_shots = num_shots
        self.qaoa_solution = 0

    def create_qaoa_circuit(self, p: int=1):
        self.qaoa_circuit = QuantumCircuit(len(self.V), len(self.V))
        self.qaoa_circuit.h(range(len(self.V)))
        for _ in range(p):
            for edge in self.E:
                node1, node2 = edge
                self.qaoa_circuit.cx(node1, node2)
                self.qaoa_circuit.rz(2 * self.gamma, node2)
                self.qaoa_circuit.cx(node1, node2)
            self.qaoa_circuit.rx(2 * self.beta, range(len(self.V)))

    def execute_qaoa_circuit(self):
        self.qaoa_circuit.measure(range(len(self.V)),range(len(self.V)))
        compiled_circuit = transpile(self.qaoa_circuit, self.simulator)
        job = self.simulator.run(compiled_circuit, shots=self.num_shots)
        result = job.result()
        self.qaoa_counts = result.get_counts(compiled_circuit)

    def find_maxcut(self):
        for s in self.qaoa_counts:
            self.qaoa_solution = max(self.qaoa_solution, self._compute_cut(s))

    def _compute_cut(self, s: str):
        cut_value = 0
        s = s[::-1]
        for edge in self.E:
            node1, node2 = edge
            if s[node1] != s[node2]:
                cut_value += 1
        return cut_value

    def optimize_parameters(self):
        pass

    def solve(self):
        self.create_qaoa_circuit()
        self.execute_qaoa_circuit()
        self.find_maxcut()
        return self.qaoa_solution