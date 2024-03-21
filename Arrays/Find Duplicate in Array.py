class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        slow = A[0]
        fast = A[A[0]]

        while slow != fast:
            slow = A[slow]
            fast = A[A[fast]]

        slow = 0
        while slow != fast:
            slow = A[slow]
            fast = A[fast]

        return slow if slow != 0 else -1
