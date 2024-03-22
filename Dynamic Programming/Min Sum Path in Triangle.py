class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        n = len(A)
        dp = A[-1]  
        
        for i in range(n - 2, -1, -1):
            for j in range(len(A[i])):
                dp[j] = A[i][j] + min(dp[j], dp[j+1])
        
        return dp[0]
