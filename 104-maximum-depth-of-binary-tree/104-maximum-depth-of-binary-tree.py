# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        # max_cnt = []
        # self._path(root, 0, max_cnt)
        # return max(max_cnt)
        
        return self.dfs(root, 0)
    
    # def _path(self, root, cnt, max_cnt):
        # cnt += 1
        # if root.left:
        #     self._path(root.left, cnt, max_cnt)
        # if root.right:
        #     self._path(root.right, cnt, max_cnt)
        
        # if not root.left and not root.right:
        #     max_cnt.append(cnt)
        
    def dfs(self, root, depth):
        if not root:
            return depth
        left_depth = self.dfs(root.left, depth+1)
        right_depth = self.dfs(root.right, depth+1)
        
        return left_depth if left_depth > right_depth else right_depth
        
        