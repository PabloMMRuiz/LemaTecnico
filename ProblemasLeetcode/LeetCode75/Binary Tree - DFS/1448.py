from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def rec(node, m):
            nonlocal res
            if not node:
                return
            if node.val >= m:
                res += 1
            m = max(m, node.val)
            rec(node.left, m)
            rec(node.right, m)
        
        rec(root, root.val)
        return res
    
# Better solution:
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            is_good = 1 if node.val >= max_so_far else 0
            max_so_far = max(max_so_far, node.val)
            return is_good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)

        return dfs(root, root.val)

'''