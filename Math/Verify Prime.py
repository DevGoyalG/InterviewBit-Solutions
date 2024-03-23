class Solution:
	# @param A : integer
	# @return an integer
	def isPrime(self, A):
        if A <= 1:
            return 0  

        for i in range(2, int(A**0.5) + 1):
            if A % i == 0:
                return 0  

        return 1
