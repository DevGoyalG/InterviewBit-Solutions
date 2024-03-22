# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        if not A or not B:
            return None

        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        lenA, lenB = getLength(A), getLength(B)
        diff = abs(lenA - lenB)

        if lenA > lenB:
            for _ in range(diff):
                A = A.next
        else:
            for _ in range(diff):
                B = B.next

        while A and B:
            if A == B:
                return A
            A = A.next
            B = B.next

        return None
