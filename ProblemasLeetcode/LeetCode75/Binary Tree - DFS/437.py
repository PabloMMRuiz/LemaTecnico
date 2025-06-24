from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs_from_node(node, current_sum):
            if not node:
                return 0
            current_sum += node.val
            return (current_sum == targetSum) + dfs_from_node(node.left, current_sum) + dfs_from_node(node.right, current_sum)
        
        def traverse(node):
            if not node:
                return 0
            return dfs_from_node(node, 0) + traverse(node.left) + traverse(node.right)
        
        return traverse(root)



            