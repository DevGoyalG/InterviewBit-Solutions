class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)

        for i in range(n):
            while 1 <= A[i] <= n and A[A[i] - 1] != A[i]:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]

        for i in range(n):
            if A[i] != i + 1:
                return i + 1

        return n + 1
