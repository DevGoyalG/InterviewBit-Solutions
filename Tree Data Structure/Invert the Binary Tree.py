# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : TreeNode
    # @return the root node in the inverted tree
    def invertTree(self, A):
        if not A:
            return None
        
        A.left, A.right = A.right, A.left
        
        self.invertTree(A.left)
        self.invertTree(A.right)
        
        return A
