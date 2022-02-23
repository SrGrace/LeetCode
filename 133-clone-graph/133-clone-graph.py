"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        cpy = {node: Node(node.val)}
        deque = collections.deque([node])
        while(deque):
            n = deque.popleft()
            for neigh in n.neighbors:
                if neigh not in cpy:
                    deque.append(neigh)
                    cpy[neigh] = Node(neigh.val)
                cpy[n].neighbors.append(cpy[neigh])
                
        return cpy[node]
    
    