# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : integer
    # @return a list of TreeNode 
    def generateTrees(self, A):
        def generateTreesHelper(start, end):
            if start > end:
                return [None]
            
            result = []
            for i in range(start, end + 1):
                left_subtrees = generateTreesHelper(start, i - 1)
                right_subtrees = generateTreesHelper(i + 1, end)
                for left_tree in left_subtrees:
                    for right_tree in right_subtrees:
                        root = TreeNode(i)
                        root.left = left_tree
                        root.right = right_tree
                        result.append(root)
            return result
        
        return generateTreesHelper(1, A)
