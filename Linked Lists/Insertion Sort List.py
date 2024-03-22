# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def insertionSortList(self, A):
        dummy = ListNode(0)
        current = A

        while current:
            next_node = current.next

            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            current.next = prev.next
            prev.next = current

            current = next_node

        return dummy.next
