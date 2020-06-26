"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        def bfs(node, s):
            if node:
                s = s * 10 + node.val
            if node.left and node.right:
                return bfs(node.left, s) + bfs(node.right, s)
            elif node.left:
                return bfs(node.left, s)
            elif node.right:
                return bfs(node.right, s)
            return s

        return bfs(root, 0)