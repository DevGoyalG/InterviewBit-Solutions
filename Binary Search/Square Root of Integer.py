class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A
        
        low, high = 1, A
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == A:
                return mid
            elif mid * mid < A:
                low = mid + 1
            else:
                high = mid - 1
        
        return high
