# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
        result = []
        stack = []
        current = A
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            
            result.append(current.val)
            
            current = current.right
        
        return result
