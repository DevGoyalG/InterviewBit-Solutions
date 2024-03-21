class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 1
        result = []

        for digit in reversed(A):
            current_sum = digit + carry
            result.append(current_sum % 10)
            carry = current_sum // 10

        if carry:
            result.append(carry)

        result.reverse()

        while result and result[0] == 0:
            result.pop(0)

        return result or [0] 
