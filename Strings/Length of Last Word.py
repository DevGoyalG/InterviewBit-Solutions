class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLastWord(self, A):
		length = 0
        found_last_word = False
        
        for i in range(len(A) - 1, -1, -1):
            if A[i] == ' ':
                if found_last_word:
                    return length
            else:
                length += 1
                found_last_word = True
        
        return length
