"""
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
"""
def is_valid_sequence_pythonic_way(root: TreeNode, arr: List[int]) -> bool:
    if not root: return False

    def is_leaf(current: TreeNode) -> bool:
        return current.left == None and current.right == None
    
    def traverse(cur: TreeNode, arr: List[int]) -> bool:
        if (not cur and arr) or not cur:
            return False

        if arr[0] != cur.val:
            return False

        if arr == [cur.val] and is_leaf(cur):
            return True
        
        if traverse(cur.left, arr[1:]) or traverse(cur.right,arr[1:]):
            return True
        
    return traverse(root,arr)
        

    



def is_valid_sequence(root: TreeNode, arr: List[int]) -> bool:
    if root.val != arr[0]:
        return False
    n, index, cur = len(arr), 1, root
    if n == 1:
        if root.left == None and root.right == None:
            return True
        else:
            return False
    q = []
    while True:
        if cur.left != None and cur.left.val == arr[index]:
            if cur.right and cur.right.val == arr[index]:
                q.append((cur.right, index))
            cur = cur.left
        elif cur.right != None and cur.right.val == arr[index]:
            cur = cur.right
        else:
            try:
                cur, index = q.pop()
            except:
                return False
            continue
        index += 1
        if index == n:
            if cur.left == None and cur.right == None:
                return True
            try:
                cur, index = q.pop()
            except:
                return False
    return False


if __name__ == "__main__":
    assert is_valid_sequence(
        root=[0, 1, 0, 0, 1, 0, None, None, 1, 0, 0], arr=[0, 1, 0, 1]) == True
    assert is_valid_sequence(
        root=[0, 1, 0, 0, 1, 0, None, None, 1, 0, 0], arr=[0, 0, 1]) == False
    assert is_valid_sequence(
        [0, 1, 0, 0, 1, 0, None, None, 1, 0, 0], arr=[0, 1, 1]) == False
