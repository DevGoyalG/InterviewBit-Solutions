class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A < 0:
            return []

        row = [1]
        for i in range(1, A + 1):
            new_value = row[-1] * (A - i + 1) // i
            row.append(new_value)

        return row
