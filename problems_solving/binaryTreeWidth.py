import collections
"""Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. 
The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes 
(the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        indexDic = collections.defaultdict(list)

        def rightTraverse(node, index, depth):
            nonlocal indexDic
            if depth not in indexDic:
                indexDic[depth] = [index, index]
            else:
                indexDic[depth][0] = min(indexDic[depth][0], index)
                indexDic[depth][1] = max(indexDic[depth][1], index)
            #print(f'{depth} :: {node.val} -> {index}')
            nextIndex = index * 2
            if node.left:
                rightTraverse(node.left, nextIndex - 1, depth + 1)
            if node.right:
                rightTraverse(node.right, nextIndex, depth + 1)

        rightTraverse(root, 1, 0)

        ans = 0
        for depth in indexDic.keys():
            ans = max(ans, indexDic[depth][1] - indexDic[depth][0] + 1)
        return ans