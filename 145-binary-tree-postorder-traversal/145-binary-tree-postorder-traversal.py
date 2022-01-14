# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        post_traverse = list()
        self._traverse(root, post_traverse)
        return post_traverse
    
    def _traverse(self, root, post_traverse=list()):
        # LRD
        if root.left:
            self._traverse(root.left, post_traverse)
        if root.right:
            self._traverse(root.right, post_traverse)
        
        post_traverse.append(root.val)
        