class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        def search_left(A, target):
            left = 0
            right = len(A) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if A[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def search_right(A, target):
            left = 0
            right = len(A) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if A[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left_index = search_left(A, B)
        right_index = search_right(A, B)
        
        if left_index <= right_index:
            return [left_index, right_index]
        else:
            return [-1, -1]
