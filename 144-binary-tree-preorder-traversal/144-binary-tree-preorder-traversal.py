# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        pre_traverse = list()
        self._traverse(root, pre_traverse)
        return pre_traverse
    
    def _traverse(self, root, pre_traverse=list()):
        # DLR
        pre_traverse.append(root.val)
        if root.left:
            self._traverse(root.left, pre_traverse)
        if root.right:
            self._traverse(root.right, pre_traverse)
            