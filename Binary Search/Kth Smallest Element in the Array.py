class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
        def countSmallerOrEqual(mid):
            count = 0
            for num in A:
                if num <= mid:
                    count += 1
            return count
        
        low = min(A)
        high = max(A)
        
        while low < high:
            mid = (low + high) // 2
            count = countSmallerOrEqual(mid)
            if count < B:
                low = mid + 1
            else:
                high = mid
        
        return low
