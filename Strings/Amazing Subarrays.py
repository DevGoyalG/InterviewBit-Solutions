class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = "aeiouAEIOU"
        n = len(A)
        count = 0
        for i in range(n):
            if A[i] in vowels:
                count += n - i
        return count % 10003
