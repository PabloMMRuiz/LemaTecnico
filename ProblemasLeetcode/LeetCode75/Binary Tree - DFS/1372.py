from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, is_left, length):
            if not node:
                return
            self.res = max(self.res, length)
            if is_left:
                dfs(node.right, False, length + 1)  # Continue ZigZag
                dfs(node.left, True, 1)             # Restart from left child
            else:
                dfs(node.left, True, length + 1)    # Continue ZigZag
                dfs(node.right, False, 1)           # Restart from right child

        dfs(root.left, True, 1)
        dfs(root.right, False, 1)
        return self.res
