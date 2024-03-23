class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        def is_palindrome(word):
            return word == word[::-1]

        words = A.split()
        count = 0

        for word in words:
            if is_palindrome(word):
                count += 1

        return count
