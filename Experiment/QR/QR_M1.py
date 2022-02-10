import math

def run(qc):
    qc.h(4)
    qc.p(math.pi/3, 4)
    qc.mcp(math.pi / 6, [5,6], 4)  # M1
    qc.h(4)


    qc.barrier()

    qc.cswap(4, 5, 9)
    qc.cswap(4, 6, 10)
    qc.cswap(4, 7, 11)
    qc.cswap(4, 8, 12)

    qc.barrier()

    qc.swap(0, 5)
    qc.swap(1, 6)
    qc.swap(2, 7)
    qc.swap(3, 8)

    qc.barrier()

    qc.mcx([0,1,2], 3)
    qc.mcx([0,1], 2)
    qc.cx(0, 1)
    qc.x(0)

    qc.barrier()

    qc.measure([0, 1, 2, 3], [0, 1, 2, 3])







