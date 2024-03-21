class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        if not A:
            return A
        
        n = len(A)
        
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            
            for i in range(first, last):
                top = A[first][i]
                
                A[first][i] = A[last - (i - first)][first]
                
                A[last - (i - first)][first] = A[last][last - (i - first)]
                
                A[last][last - (i - first)] = A[i][last]
                
                A[i][last] = top
                
        return A
