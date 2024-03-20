class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):
		if A <= 2:
            return A

        first, second = 1, 2

        for _ in range(3, A + 1):
            current = first + second
            first, second = second, current

        return second
