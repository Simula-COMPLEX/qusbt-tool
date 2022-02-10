import math

def run(qc):
    qc.h(2)
    qc.p(math.pi/4, 2)

    qc.x(10)
    qc.h(11)
    qc.p(math.pi/2,11)

    for i in range(9):
        control = []
        control.append(10)
        for j in range(9-i):
            control.append(j)
        qc.mct(control, 9-i)
    qc.cnot(10,0)

    qc.barrier()

    qc.ccx(5, 6, 0)  # M1

    for i in range(8):
        control = []
        control.append(10)
        control.append(11)
        for j in range(1,9-i):
            control.append(j)
        qc.mct(control,9-i)
    qc.ccx(10,11,1)

    qc.barrier()

    for i in range(8):
        control = []
        control.append(10)
        control.append(11)
        for j in range(1,9-i):
            control.append(j)
        qc.mct(control,9-i)
    qc.ccx(10, 11, 1)

    qc.barrier()

    for i in range(7):
        control = []
        control.append(11)
        for j in range(2,9-i):
            control.append(j)
        qc.mct(control,9-i)
    qc.cnot(11,2)

    qc.barrier()

    qc.measure([0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8,9])