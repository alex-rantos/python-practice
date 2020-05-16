"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree."""

def goodNodes(self, root: TreeNode) -> int:
    self.c = 0
    if root.left == None and root.right == None:
        if root.val != None:
            return 1
        else:
            return 0
    
    def util(maxval,node):
        if (node.val>=maxval):
            self.c+=1
        if (node.left!=None):
            util(max(maxval,node.val),node.left)
        if (node.right!=None):
            util(max(maxval,node.val),node.right)
    
    util(root.val,root)
    return self.c