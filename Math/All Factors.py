import math

class Solution:
    def allFactors(self, A):
        factors = []
        sqrt_A = int(math.sqrt(A))
        for i in range(1, sqrt_A + 1):
            if A % i == 0:
                factors.append(i)
                if i != A // i:
                    factors.append(A // i)
        factors.sort()
        return factors
