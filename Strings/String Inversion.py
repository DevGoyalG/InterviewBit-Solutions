class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        result=""
        for char in A:
            if char.islower():
                result+=char.upper()
            elif char.isupper():
                result+=char.lower()
            else:
                result+=char
        return result
