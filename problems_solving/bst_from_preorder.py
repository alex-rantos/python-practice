class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bst_from_preorder_recursive(self, preorder: List[int]) -> TreeNode:
    if not preorder: return None

    root = TreeNode(preorder[0])

    i = 1
    while i < len(preorder) and  preorder[i] < root.val:
        i+=1

    root.left = self.bst_from_preorder_recursive(preorder[1:i])
    root.right = self.bst_from_preorder_recursive(preorder[i:])

    return root

# geeks
def bst_from_preorder(self, pre: List[int]) -> TreeNode:
    root = TreeNode(pre[0]) 

    s = [] 

    # append root 
    s.append(root) 

    i = 1

    # Iterate through rest of the size-1 
    # items of given preorder array 
    while ( i < len(pre)):  
        temp = None

        # Keep on popping while the next value  
        # is greater than stack's top value.  
        while (len(s) > 0 and pre[i] > s[-1].val):  
            temp = s.pop() 
            
        # Make this greater value as the right child 
        # and append it to the stack 
        if (temp != None):  
            temp.right = TreeNode(pre[i]) 
            s.append(temp.right) 
            
        # If the next value is less than the stack's top 
        # value, make this value as the left child of the  
        # stack's top node. append the new node to stack 
        else : 
            temp = s[-1] 
            temp.left = TreeNode(pre[i]) 
            s.append(temp.left) 
        i = i + 1
        
    return root 