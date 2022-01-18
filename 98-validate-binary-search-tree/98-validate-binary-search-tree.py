# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, mn, mx):
            if not root:
                return 1
            if not (mn < root.val < mx):
                return 0
            return helper(root.left, mn, root.val) and helper(root.right, root.val, mx)
        
        return helper(root, mn=float('-inf'), mx=float('inf'))
    
    