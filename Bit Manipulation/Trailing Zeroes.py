class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count = 0
        
        binary_repr = bin(A)[2:]
        for digit in reversed(binary_repr):
            if digit == '0':
                count += 1
            else:
                break  
        
        return count
