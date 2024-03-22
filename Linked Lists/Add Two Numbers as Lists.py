# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def addTwoNumbers(self, A, B):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while A or B or carry:
            val1 = A.val if A else 0
            val2 = B.val if B else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if A:
                A = A.next
            if B:
                B = B.next

        return dummy.next
