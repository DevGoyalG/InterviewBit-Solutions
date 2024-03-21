class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        N = len(A)
        
        result = []
        
        for j in range(N):
            anti_diagonal = []
            i, k = 0, j
            while i < N and k >= 0:
                anti_diagonal.append(A[i][k])
                i += 1
                k -= 1
            result.append(anti_diagonal)
        
        for i in range(1, N):
            anti_diagonal = []
            j, k = N - 1, i
            while j >= 0 and k < N:
                anti_diagonal.append(A[k][j])
                j -= 1
                k += 1
            result.append(anti_diagonal)
        
        return result
