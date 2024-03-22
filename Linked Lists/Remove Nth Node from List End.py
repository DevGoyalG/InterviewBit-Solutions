# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, A, B):
		if not A or B <= 0:
            return A

        length = 0
        current = A
        while current:
            length += 1
            current = current.next

        if B >= length:
            return A.next

        target_index = length - B
        prev, current = None, A

        for _ in range(target_index):
            prev, current = current, current.next

        prev.next = current.next

        return A
