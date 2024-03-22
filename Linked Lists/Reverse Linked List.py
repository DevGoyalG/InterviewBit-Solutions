# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, A):
		prev = None
        current = A

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
