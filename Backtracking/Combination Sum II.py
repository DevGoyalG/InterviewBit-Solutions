class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        def dfs(start, target, path):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(A)):
                if A[i] > target:
                    break
                if i > start and A[i] == A[i - 1]:
                    continue
                dfs(i + 1, target - A[i], path + [A[i]])

        A.sort()
        result = []
        dfs(0, B, [])
        return result
