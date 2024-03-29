class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        low = 0  
        high = len(A) - 1  
        mid = 0  

        while mid <= high:
            if A[mid] == 0:  
                A[low], A[mid] = A[mid], A[low]  
                low += 1  
                mid += 1  
            elif A[mid] == 1:  
                mid += 1 
            else:  
                A[mid], A[high] = A[high], A[mid]  
                high -= 1  

        return A
