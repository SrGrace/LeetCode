# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        qu, res = collections.deque(), []
        qu.append(root)
        while(len(qu) > 0):
            tmp = []
            for _ in range(len(qu)):
                x = qu.popleft()
                tmp.append(x.val)
                if x.left:
                    qu.append(x.left)
                if x.right:
                    qu.append(x.right)
            
            res.append(tmp)
        return res
                
        