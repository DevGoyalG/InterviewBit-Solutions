class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        result = [[A] * (2*A - 1) for _ in range(2*A - 1)]
        
        for k in range(A):
            for i in range(k, 2*A - 1 - k):
                for j in range(k, 2*A - 1 - k):
                    result[i][j] = A - k
        
        return result
