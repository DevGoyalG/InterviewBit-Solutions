class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if not A:
            return 0
        
        def find_min_max(arr, low, high):
            if low == high:
                return arr[low], arr[low]
            elif high - low == 1:
                return min(arr[low], arr[high]), max(arr[low], arr[high])
            
            mid = (low + high) // 2
            min1, max1 = find_min_max(arr, low, mid)
            min2, max2 = find_min_max(arr, mid + 1, high)
            
            return min(min1, min2), max(max1, max2)
        
        min_val, max_val = find_min_max(A, 0, len(A) - 1)
        return min_val + max_val
