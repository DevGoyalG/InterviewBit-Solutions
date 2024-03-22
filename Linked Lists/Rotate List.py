# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def rotateRight(self, A, B):
		if not A or B == 0:
            return A

        length = 0
        current = A
        while current:
            length += 1
            current = current.next

        k = B % length

        if k == 0:
            return A

        slow = A
        fast = A
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = A

        return new_head
