class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n == 0:
            return 0

        left = 0
        for right in range(1, n):
            if A[right] != A[left]:
                left += 1
                A[left] = A[right]

        return left + 1
