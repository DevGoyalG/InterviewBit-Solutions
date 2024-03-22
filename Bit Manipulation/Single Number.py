class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
        result = 0
        for num in A:
            result ^= num
        return result
