class Solution:
	# @param A : integer
	# @return a strings
	def convertToTitle(self, A):
		column_title = ""
        while A > 0:
            remainder = A % 26
            if remainder == 0:
                column_title += 'Z'
                A -= 1
            else:
                column_title += chr(ord('A') + remainder - 1)
            A //= 26
        return column_title[::-1]
