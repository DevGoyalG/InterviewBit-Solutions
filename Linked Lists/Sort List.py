# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def sortList(self, A):
        if not A or not A.next:
            return A

        def merge(left, right):
            dummy = ListNode(0)
            current = dummy

            while left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next

            if left:
                current.next = left
            elif right:
                current.next = right

            return dummy.next

        def find_middle(head):
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge_sort(head):
            if not head or not head.next:
                return head

            mid = find_middle(head)
            right = merge_sort(mid.next)
            mid.next = None
            left = merge_sort(head)

            return merge(left, right)

        return merge_sort(A)
