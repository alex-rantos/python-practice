import pdb
"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
"""
class SingleList(object):
    def __init__(self):
        self.head = None

    def insert_array(self, arr):
        if not self.head:
            self.head = ListNode(arr.pop(0))
        cur = self.head
        while cur.next:
            cur = cur.next
        for x in arr:
            cur.next = ListNode(x)
            cur = cur.next
    

    def print(self):
        print("Printing Single Linked List")
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
        print("")
    


class ListNode(object):
    def __init__(self, x):
       self.val = x
       self.next = None

    def set_next(self,node):
        self.next = node

def middle_node(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head = SingleList()
    head.insert_array(arr)
    head.print()

    middle_node = middle_node(head.head)
    print("Print the end half of the list:")
    while middle_node:
        print(middle_node.val)
        middle_node = middle_node.next
    