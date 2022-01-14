# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        in_traverse = list()
        self._traverse(root, in_traverse)
        return in_traverse
    
    def _traverse(self, root, in_traverse=list()):
        # LDR
        if root.left:
            self._traverse(root.left, in_traverse)
        
        in_traverse.append(root.val)
        
        if root.right:
            self._traverse(root.right, in_traverse)
        