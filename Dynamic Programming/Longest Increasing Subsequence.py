class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        n = len(A)
        dp = [1] * n  

        for i in range(1, n):
            for j in range(i):
                if A[i] > A[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
