class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        def backtrack(start, parts):
            if start == len(A) and len(parts) == 4:
                result.append(".".join(parts))
                return
            if len(parts) > 4:
                return
            for i in range(1, 4):
                if start + i <= len(A):
                    segment = A[start:start + i]
                    if (segment[0] != '0' or segment == '0') and 0 <= int(segment) <= 255:
                        backtrack(start + i, parts + [segment])

        result = []
        backtrack(0, [])
        return result
