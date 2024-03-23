class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        total_fine = 0
        rule = B % 2  

        for last_digit in A:
            if last_digit % 2 != rule:
                total_fine += C

        return total_fine
