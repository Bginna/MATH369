from math import gcd as bltin_gcd
import sys


#This checks if GCD is 1, if its not, returns false
def coprime(a, b):
    return bltin_gcd(a, b) == 1


primeFactors = []
#iterates through all integers less than N and checks if they are prime factors
for i in range (1, int(sys.argv[1])):

    if coprime(i, int(sys.argv[1])):
        primeFactors.append(i)

print("Prime factors: " + str(primeFactors))
print("Euler Phi: " + str(len(primeFactors)))
