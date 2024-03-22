# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
		temp = ListNode(0)
        current = temp

        while A and B:
            if A.val < B.val:
                current.next = A
                A = A.next
            else:
                current.next = B
                B = B.next
            current = current.next

        if A:
            current.next = A
        else:
            current.next = B

        return temp.next
