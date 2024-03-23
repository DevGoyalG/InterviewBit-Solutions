class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
        if not A:
            return ""
        
        lcp = A[0]
        
        for i in range(1, len(A)):
            j = 0
            while j < len(lcp) and j < len(A[i]) and lcp[j] == A[i][j]:
                j += 1
            lcp = lcp[:j]
            if not lcp:
                break
        
        return lcp
