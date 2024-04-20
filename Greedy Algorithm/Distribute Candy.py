class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)
        candies = [1] * n  
        
        for i in range(1, n):
            if A[i] > A[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        
        return sum(candies)
