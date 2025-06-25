from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        i = 1
        if not root:
            return 0
        level = [root]
        sum_per_level = {}
        while True:
            if len(level) == 0:
                return max(sum_per_level.items(), key=lambda i:i[1])[0]
            new = []
            value = sum(n.val for n in level)
            if value not in sum_per_level.values():
                sum_per_level[i] = value
            i+=1
            for n in level:
                if n.left: new.append(n.left)
                if n.right: new.append(n.right)
            level = new
