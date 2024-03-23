class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        words=A.split()
        reversed_words = words[::-1]
        reversed_string = ' '.join(reversed_words)
        return reversed_string
