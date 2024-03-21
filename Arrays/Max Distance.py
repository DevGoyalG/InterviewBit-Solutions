class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)

        LMin = [0] * n
        LMin[0] = A[0]
        for i in range(1, n):
            LMin[i] = min(LMin[i-1], A[i])

        RMax = [0] * n
        RMax[n-1] = A[n-1]
        for i in range(n-2, -1, -1):
            RMax[i] = max(RMax[i+1], A[i])

        i, j, max_gap = 0, 0, 0
        while i < n and j < n:
            if LMin[i] <= RMax[j]:
                max_gap = max(max_gap, j - i)
                j += 1
            else:
                i += 1

        return max_gap
