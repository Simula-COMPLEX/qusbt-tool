import math

def run(qc):
    qc.h([10,11,12,13,14,15,16,17,18,19])
    for i in range(10):
        qc.cz(i,i+10)
    qc.barrier()
    qc.h([10,11,12,13,14,15,16,17,18,19])
    qc.measure([10,11,12,13,14,15,16,17,18,19],[0,1,2,3,4,5,6,7,8,9])

    from qiskit.tools.visualization import circuit_drawer
    circuit_drawer(qc, filename='./BV_circuit.txt')
