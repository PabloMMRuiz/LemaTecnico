from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = [root]
        res = []
        while True:
            if len(level) == 0:
                return res
            new = []
            res.append(level[-1].val)
            for n in level:
                if n.left: new.append(n.left)
                if n.right: new.append(n.right)
            level = new

            
        