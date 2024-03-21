class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        count_A_greater_than_C = 0
        count_B_less_than_C = 0

        for num in A:
            if num > C:
                count_A_greater_than_C += 1

        for num in B:
            if num < C:
                count_B_less_than_C += 1

        return max(count_A_greater_than_C, count_B_less_than_C)
