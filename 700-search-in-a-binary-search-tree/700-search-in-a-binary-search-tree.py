# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if not root or root.val == val:
        #     return root
        
        # elif root.val > val:
        #     return self.searchBST(root.left, val)
        
        # else:
        #     return self.searchBST(root.right, val)
        
        cur = root
        while(cur):
            if cur.val == val:
                return cur
            elif cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        return None
        
        