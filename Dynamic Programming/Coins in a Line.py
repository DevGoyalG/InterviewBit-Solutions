class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        n = len(A)
        memo = {}

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            take_i = A[i] + min(dp(i+1, j-1), dp(i+2, j))
            take_j = A[j] + min(dp(i+1, j-1), dp(i, j-2))
            memo[(i, j)] = max(take_i, take_j)
            return memo[(i, j)]

        return dp(0, n-1)
