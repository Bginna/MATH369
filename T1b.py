import math
import sys


def primeFactors(n):
    primeFactorList0 = []
    while n % 2 == 0:
        primeFactorList0.append(2)
        n = n / 2

    for i in range (3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            primeFactorList0.append(i)
            n = n / i

    if n > 2:
        primeFactorList0.append(n)
    return primeFactorList0


primeFactorList = primeFactors(int(sys.argv[1]))
distinctFactors = []

for i in primeFactorList:
    if i not in distinctFactors:
        distinctFactors.append(i)

finalVal = int(sys.argv[1])

for i in distinctFactors:
    finalVal = finalVal * (1 - (1 / i))

print("Euler Phi: " + str(finalVal))

