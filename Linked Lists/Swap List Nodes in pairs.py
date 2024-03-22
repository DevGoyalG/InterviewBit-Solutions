# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):
        if not A or not A.next:
            return A

        new_head = A.next
        prev, current = None, A
        while current and current.next:
            first, second = current, current.next
            if prev:
                prev.next = second
            first.next, second.next = second.next, first
            prev, current = first, first.next
        return new_head
