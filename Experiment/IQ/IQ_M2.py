import math

def swap_registers(circuit, n):
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    return circuit

def qft_rotations(circuit, qubit, p):
    for j in range(qubit + 1, 10):
        circuit.cu1(math.pi/2**(p), qubit, j)
        p += 1
    circuit.barrier()
    return circuit

def run(qc):
    n = 10
    swap_registers(qc,n)
    for qubit in range(3):
        qc.h(qubit)
        p = 1
        qft_rotations(qc,qubit,p)

    qc.ch(4, 3)  # M2
    qft_rotations(qc,3,1)
    for qubit in range(4,10):
        qc.h(qubit)
        p = 1
        qft_rotations(qc,qubit,p)

    qc.measure([0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9])

