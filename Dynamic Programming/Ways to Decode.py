class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        MOD = 10**9 + 7
        n = len(A)
        
        dp = [0] * (n + 1)
        dp[0] = 1 
        dp[1] = 1 if A[0] != '0' else 0  
        
        for i in range(2, n + 1):
            if A[i - 1] != '0':
                dp[i] += dp[i - 1]
            if '10' <= A[i - 2:i] <= '26':
                dp[i] += dp[i - 2]
            dp[i] %= MOD
        
        return dp[n]
