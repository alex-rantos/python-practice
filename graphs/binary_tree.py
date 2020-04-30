""" 
A Binary Tree structure. Tree is initialized from an array containing 
numbers and None. 

Example: 

Input: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
"""

from collections import deque
import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class BinaryTree(object):
    def __init__(self, arr:[int]):
        self.array = copy.deepcopy(arr)
        if arr:
            self.root = TreeNode(arr[0])
            del arr[0]
            print(arr)
        else:
            return
        cur = self.root
        queue = deque([])
        counter = 0
        for n in arr:
            if n != None:
                if cur.left != None and cur.right != None or counter == 2:
                    try:
                        cur = queue.popleft()
                    except:
                        print(cur.val)
                    counter = 0
                
                if cur.left == None:
                    cur.left = TreeNode(n)
                    queue.append(cur.left)
                elif cur.right == None:
                    cur.right = TreeNode(n)
                    queue.append(cur.right)
                else:
                    raise Exception("Check input. Invalid State")
            else:
                counter += 1
                if (counter == 2):
                    queue.popleft()
                    cur = queue.popleft()
                    counter = 0

    def __str__(self):
        # TODO
        return "Binary Tree"

if __name__ == "__main__":
    tree = BinaryTree([1,2,3])
    print(tree)
    tree2 = BinaryTree([-10,9,20,None,None,15,7,5,None,4])
    print(tree2)