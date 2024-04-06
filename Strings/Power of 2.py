class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        num = int(A)
        
        if num == 1:
            return 0
        
        while num % 2 == 0:
            num //= 2
        
        if num == 1:
            return 1
        else:
            return 0
