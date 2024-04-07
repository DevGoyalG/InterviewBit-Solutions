class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        target = len(A) - 1
        for i in range(len(A) - 2, -1, -1):
            if i + A[i] >= target:
                target = i
        return 1 if target == 0 else 0
