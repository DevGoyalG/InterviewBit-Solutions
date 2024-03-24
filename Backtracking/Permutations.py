class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):
        result = []
        self.permute_recursive(A, 0, result)
        return result
    
    def permute_recursive(self, A, start, result):
        if start == len(A):
            result.append(A[:])  
            return
        
        for i in range(start, len(A)):
            A[start], A[i] = A[i], A[start]
            self.permute_recursive(A, start + 1, result)
            A[start], A[i] = A[i], A[start]
