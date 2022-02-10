import math

def run(qc):
    qc.x(0)
    qc.h(2)

    qc.barrier()

    qc.h(4)
    qc.p(math.pi/4, 4)
    qc.barrier()

    qc.x(1)
    qc.cx(1,2)
    qc.x(0)
    qc.cx(0,1)
    qc.mct([0,1],2)
    qc.barrier()

    for i in range(11):
        control = []
        control.append(2)
        if i < 10:
            for j in range(10-i):
                control.append(j + 3)
        qc.mct(control,10-i+3)
    qc.barrier()

    qc.mct([0,1],2)
    qc.cx(0,1)
    qc.x(0)
    qc.cx(1,2)
    qc.x(1)
    qc.barrier()

    qc.measure([3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10])

