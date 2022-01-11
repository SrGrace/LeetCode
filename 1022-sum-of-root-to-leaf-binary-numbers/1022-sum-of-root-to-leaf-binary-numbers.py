# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = list()
        self.path(root, '', res)
        print(res)
        return sum([int(x, 2) for x in res])
    
    def path(self, root, st, res):
        st += str(root.val)
        if root.left:
            self.path(root.left, st, res)
        if root.right:
            self.path(root.right, st, res)
        
        if not root.left and not root.right:
            res.append(st)
        

        