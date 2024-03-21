class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        n = len(A)
        low, high = 0, n - 1
        
        if A[low] <= A[high]:
            return A[low]
        
        while low <= high:
            mid = (low + high) // 2
            
            if A[mid] > A[mid + 1]:
                return A[mid + 1]
            elif A[mid] < A[mid - 1]:
                return A[mid]
            
            if A[mid] > A[low]:
                low = mid + 1
            else:
                high = mid - 1
