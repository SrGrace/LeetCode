# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hsh = list()
        cur = [root]
        while(cur):
            node = cur.pop(0)
            if k - node.val in hsh:
                return True
            
            hsh.append(node.val)
            
            if node.left:
                cur.append(node.left)
            if node.right:
                cur.append(node.right)
                
        return False
                