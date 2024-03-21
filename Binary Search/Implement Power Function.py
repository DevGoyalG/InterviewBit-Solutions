class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if n == 0:
            return 1 % d
        
        result = 1
        x %= d
        
        while n > 0:
            if n % 2 == 1:
                result = (result * x) % d
            x = (x * x) % d
            n //= 2
        
        return result
