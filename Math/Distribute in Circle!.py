class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        position = (C + (A - 1)) % B
        if position == 0:
            return B
        else:
            return position
