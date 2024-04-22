class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) < 2:
            return 0
        
        max_profit = 0
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                max_profit += A[i] - A[i - 1]
        
        return max_profit
