class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        if A == "0" or B == "0":
            return "0"

        len_a, len_b = len(A), len(B)
        result = [0] * (len_a + len_b)

        for i in range(len_a - 1, -1, -1):
            carry = 0
            for j in range(len_b - 1, -1, -1):
                temp = (ord(A[i]) - ord('0')) * (ord(B[j]) - ord('0')) + carry
                carry, remainder = divmod(temp + result[i + j + 1], 10)
                result[i + j + 1] = remainder

            result[i] += carry

        result_str = "".join(map(str, result))
        result_str = result_str.lstrip('0')  

        return result_str if result_str else "0"
