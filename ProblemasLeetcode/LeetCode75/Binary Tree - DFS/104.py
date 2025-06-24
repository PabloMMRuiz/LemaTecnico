from typing import Optional
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def recursion(node, num):
            nonlocal maxi
            if node == None:
                maxi = max(maxi, num)
                return
            recursion(node.left, num+1)
            recursion(node.right, num+1)
        
        recursion(root, 0)
        return maxi
    
# Easier solution:
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
'''