class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        if not A:
            return 0
        
        i = 0
        sign = 1
        result = 0
        max_int = 2**31 - 1
        min_int = -2**31
        
        while i < len(A) and A[i].isspace():
            i += 1
        
        if i < len(A) and (A[i] == '+' or A[i] == '-'):
            sign = -1 if A[i] == '-' else 1
            i += 1
        
        while i < len(A) and A[i].isdigit():
            digit = int(A[i])
            if result > max_int // 10 or (result == max_int // 10 and digit > max_int % 10):
                return max_int if sign == 1 else min_int
            result = result * 10 + digit
            i += 1
        
        return sign * result
