"""You are given two non-empty linked lists representing two non-negative 
integers. The most significant digit comes first and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = 0
        while l1:
            n1 = n1 * 10 + int(l1.val)
            l1 = l1.next

        n2 = 0
        while l2:
            n2 = n2 * 10 + int(l2.val)
            l2 = l2.next

        num = str(n1 + n2)
        l = ListNode()
        cur = l
        for c in num:
            cur.next = ListNode(int(c))
            cur = cur.next
        return l.next