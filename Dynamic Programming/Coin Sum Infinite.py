class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, A, B):
        MOD = 1000007
        dp = [0] * (B + 1)
        dp[0] = 1

        for coin in A:
            for i in range(coin, B + 1):
                dp[i] += dp[i - coin]
                dp[i] %= MOD

        return dp[B] % MOD
