class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        n = len(A)
        
        i = n - 2
        while i >= 0 and A[i] >= A[i + 1]:
            i -= 1
        
        if i == -1:
            A.reverse()
            return A
        
        j = n - 1
        while A[j] <= A[i]:
            j -= 1
        
        A[i], A[j] = A[j], A[i]
        
        A[i + 1:] = reversed(A[i + 1:])
        
        return A
