class Solution:
	# @param A : string
	# @return an integer
	def findRank(self, A):
		n = len(A)
        MOD = 1000003
        rank = 1
        fact = [1] * (n + 1)

        for i in range(2, n + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        for i in range(n):
            smaller = 0
            for j in range(i + 1, n):
                if A[j] < A[i]:
                    smaller += 1
            rank = (rank + smaller * fact[n - i - 1]) % MOD

        return rank
