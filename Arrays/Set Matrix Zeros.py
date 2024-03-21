class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        if not A:
            return A

        rows_to_zero = set()
        cols_to_zero = set()

        m, n = len(A), len(A[0])

        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        for row in rows_to_zero:
            for j in range(n):
                A[row][j] = 0

        for col in cols_to_zero:
            for i in range(m):
                A[i][col] = 0

        return A
