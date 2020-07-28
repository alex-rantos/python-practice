from typing import List
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
                return []
        
        def bfs(node, depth, nodesList):
            if not node:
                return nodesList
            
            if len(nodesList) <= depth:
                nodesList.append([])
            nodesList[depth].append(node.val)
            
            bfs(node.left, depth + 1, nodesList)            
            bfs(node.right, depth + 1, nodesList)
                
            return nodesList
        
        nodesList = [[]]
        nodesList = bfs(root,0,nodesList)
        for i in range(len(nodesList)):
            if i%2 == 1:
                nodesList[i] = nodesList[i][::-1]
        return nodesList
        