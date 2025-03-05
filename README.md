# Simulation-of-OR-gate-using-qiskit

Quantum OR Gate using Qiskit
This repository contains an implementation of a Quantum OR Gate using Qiskit. Since quantum gates must be unitary, there is no direct OR gate in quantum computing. However, we can simulate the behavior of a classical OR gate using CNOT and Toffoli (CCX) gates with an ancilla qubit.

🛠 Features:
✅ Simulates an OR gate using quantum circuits
✅ Uses an ancilla qubit to store the OR operation result
✅ Implements measurement to get classical output
✅ Provides a truth table verification

📜 Code Overview:
The circuit consists of three qubits (two inputs + one ancilla).
CNOT gates propagate input values to the ancilla.
A Toffoli gate corrects the ancilla value to match an OR operation.
The circuit is simulated using the QASM Simulator.
