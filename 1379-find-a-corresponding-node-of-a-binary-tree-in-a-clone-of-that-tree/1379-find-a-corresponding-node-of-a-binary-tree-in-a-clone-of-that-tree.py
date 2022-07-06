# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def searching(node):
            if not node:
                return None
            elif node.val == target.val:
                return node
            return searching(node.left) or searching(node.right)
        
        return searching(cloned) 