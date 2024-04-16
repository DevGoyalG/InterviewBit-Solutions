class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        MOD = 10**9 + 7
        result = 0
        n = len(A)
        
        for i in range(32): 
            count_ones = 0
            for j in range(n):
                if (A[j] >> i) & 1: 
                    count_ones += 1
            result += (count_ones * (n - count_ones)) % MOD
        
        return (2 * result) % MOD
