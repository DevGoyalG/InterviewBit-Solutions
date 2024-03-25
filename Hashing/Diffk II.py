class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
		if len(A) < 2:
            return 0
            
        num_map = {}
        for num in A:
            if num - B in num_map or num + B in num_map:
                return 1
            num_map[num] = True
        
        return 0
