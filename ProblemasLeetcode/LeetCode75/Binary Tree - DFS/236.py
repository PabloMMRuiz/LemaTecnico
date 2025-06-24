class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if the current node is None or matches one of the target nodes
        if root is None or root == p or root == q:
            return root
        
        # Recur on left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are not None, current node is LCA
        if left and right:
            return root
        
        # Otherwise return the non-null child (could be LCA or one of the target nodes)
        return left if left else right
