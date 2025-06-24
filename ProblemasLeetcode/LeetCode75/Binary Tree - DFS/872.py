from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []
        def findleafs(node, l):
            if node.left == None and node.right == None:
                l.append(node.val)
                return
            else:
                if node.left: findleafs(node.left, l)
                if node.right: findleafs(node.right, l)
        findleafs(root1, l1)
        findleafs(root2, l2)
        return l1 == l2
        