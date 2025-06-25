from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        while True:
            if current.val == val:
                return current
            elif current.val < val:
                if current.right: 
                    current = current.right
                else:
                    return None
            else:
                if current.left:
                    current = current.left
                else:
                    return None