class Solution:
	# @param A : list of integers
	# @param B : list of integers
	def merge(self, A, B):
		m = len(A)
        n = len(B)
        
        i = m - 1
        j = n - 1
        
        A += [0] * n
        
        k = m + n - 1
        
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1
        
        while j >= 0:
            A[k] = B[j]
            j -= 1
            k -= 1
