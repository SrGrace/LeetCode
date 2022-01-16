# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_cnt = []
        self._path(root, 0, max_cnt)
        return max(max_cnt)
    
    def _path(self, root, cnt, max_cnt):
        cnt += 1
        if root.left:
            self._path(root.left, cnt, max_cnt)
        if root.right:
            self._path(root.right, cnt, max_cnt)
        
        if not root.left and not root.right:
            max_cnt.append(cnt)
        
        