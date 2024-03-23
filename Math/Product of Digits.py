class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        str_A=str(A)
        product=1
        for digit in str_A:
            product*=int(digit)
        return product
