class Solution:
    def findDigitsInBinary(self, A):
        if A == 0:
            return "0"
        
        binary = ""
        while A > 0:
            binary = str(A % 2) + binary
            A //= 2
        
        return binary
