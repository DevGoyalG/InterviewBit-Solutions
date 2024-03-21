class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        if n == 0:
            return []

        leaders = []
        max_right = A[n - 1]
        leaders.append(max_right)

        for i in range(n - 2, -1, -1):
            if A[i] > max_right:
                leaders.append(A[i])
                max_right = A[i]

        return leaders[::-1] 
