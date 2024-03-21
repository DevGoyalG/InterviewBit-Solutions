class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generateMatrix(self, A):
        result = [[0] * A for _ in range(A)]
        
        left, right, top, bottom = 0, A - 1, 0, A - 1
        num = 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result[top][i] = num
                num += 1
            top += 1

            for i in range(top, bottom + 1):
                result[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left - 1, -1):
                result[bottom][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                result[i][left] = num
                num += 1
            left += 1

        return result
