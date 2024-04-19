class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        if not A:
            return 0
        
        max_prod = min_prod = result = A[0]
        
        for i in range(1, len(A)):
            if A[i] > 0:
                max_prod = max(A[i], max_prod * A[i])
                min_prod = min(A[i], min_prod * A[i])
            elif A[i] < 0:
                temp = max_prod
                max_prod = max(A[i], min_prod * A[i])
                min_prod = min(A[i], temp * A[i])
            else:
                max_prod = min_prod = 0
            
            result = max(result, max_prod)
        
        return result
