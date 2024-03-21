class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A == 0:
            return []

        result = [[1]]

        for i in range(1, A):
            row = [1]
            for j in range(1, len(result[-1])):
                row.append(result[-1][j - 1] + result[-1][j])
            row.append(1)
            result.append(row)

        return result
