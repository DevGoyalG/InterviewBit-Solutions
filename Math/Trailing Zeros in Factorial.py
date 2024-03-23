class Solution:
	# @param A : integer
	# @return an integer
	def trailingZeroes(self, A):
        count = 0
        divisor = 5
        while A >= divisor:
            count += A // divisor
            divisor *= 5
        return count
