# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        less_than = ListNode(0)  
        greater_than_or_equal = ListNode(0)  
        less_than_head = less_than  
        greater_than_or_equal_head = greater_than_or_equal  
        
        current = A
        while current:
            if current.val < B:
                less_than.next = current
                less_than = less_than.next
            else:
                greater_than_or_equal.next = current
                greater_than_or_equal = greater_than_or_equal.next
            current = current.next
        
        less_than.next = greater_than_or_equal_head.next
        greater_than_or_equal.next = None  
        
        return less_than_head.next
