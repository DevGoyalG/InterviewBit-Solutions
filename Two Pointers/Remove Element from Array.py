class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        if not A:
            return 0
        
        left = 0  
        right = 0  
        
        while left < len(A):
            if A[left] != B:
                A[right] = A[left]
                right += 1
            left += 1
        
        return right
