class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def strStr(self, A, B):
        if not B:
            return 0
        
        if not A:
            return -1
        
        for i in range(len(A)):
            if A[i:i+len(B)] == B:
                return i
        
        return -1
