"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        isCloned = {}
        
        def recurse(node):
            if node in isCloned:
                return isCloned[node]

            copy = Node(node.val)
            isCloned[node] = copy

            for neighbor in node.neighbors:
                # recurse(neighbor)
                copy.neighbors.append(recurse(neighbor))
            
            return copy
        
        return recurse(node) if node else None
                
                
            
            