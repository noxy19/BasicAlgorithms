import math
def eral(n):
    lA = map(lambda x: x+2, range(n-1))
    lB = []
    while lA[0] < math.sqrt(n):
        lB.append(lA[0])
        for i in lA:
            if i%lB[-1] == 0:
                lA.remove(i)
    return lB+lA

print eral(100)
