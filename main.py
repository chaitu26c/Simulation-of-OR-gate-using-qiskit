from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit, transpile, assemble
import matplotlib.pyplot as plt
from qiskit.result import marginal_counts

# Create a quantum circuit with 3 qubits (2 inputs + 1 ancilla) and 1 classical bit
qc = QuantumCircuit(3, 1)

# Input qubits: A (qubit 0) and B (qubit 1)
qc.x(0)  # Set A = 1 (comment this line for different inputs)
qc.x(1)  # Set B = 1 (comment this line for different inputs)

# OR operation using an ancilla (qubit 2)
qc.cx(0, 2)  # Copy A to Ancilla
qc.cx(1, 2)  # Copy B to Ancilla
qc.ccx(0, 1, 2)  # Remove A·B from Ancilla

# Measure the OR result stored in the ancilla (qubit 2)
qc.measure(2, 0)




# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit)
result = job.result()
counts = result.get_counts(qc)
print(counts)



# Draw the circuit
qc.draw(output='mpl')
plot_histogram(counts)
plt.show()
