# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import copy

def invertTree(self, root: TreeNode) -> TreeNode:
    ans = copy.deepcopy(root)

    def util(ansTree: TreeNode, node: TreeNode) -> None:
        if (node.left != None):
            ansTree.right = node.left
            util(ansTree.right,node.left)
        else:
            ansTree.right = None

        if (node.right != None):
            ansTree.left = node.right
            util(ansTree.left ,node.right)
        else:
            ansTree.left = None

    return ans
    
            