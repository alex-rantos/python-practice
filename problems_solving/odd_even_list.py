"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def oddEvenList(self, head: ListNode) -> ListNode:
    if head == None: return None
    if (head.next == None): return head
    
    odd = ListNode(head.val)
    hodd = odd
    even = ListNode(head.next.val)
    heven=even
    cur = head.next
    c = 3
    
    while(cur.next != None):
        if (c%2==0):
            even.next = ListNode(cur.next.val)
            even = even.next
        else:
            odd.next=ListNode(cur.next.val) 
            odd=odd.next
        c+=1
        cur = cur.next
    
    odd.next=heven
    return hodd