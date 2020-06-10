from copy import deepcopy


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.


class Solution:
    def mergeTwoListsOptimalSpace(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        cur = head

        while l1 and l2:
            if(l1.val < l2. val):
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2

        return head.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 == None or l2 == None:
            return l1 if l2 == None else l2

        head = deepcopy(l1) if l1.val < l2.val else deepcopy(l2)

        if head.val == l1.val:
            l1 = l1.next
        else:
            l2 = l2.next

        cur = head

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = deepcopy(l1)
                l1 = l1.next
            else:
                cur.next = deepcopy(l2)
                l2 = l2.next
            cur = cur.next

        while l1 != None:
            cur.next = deepcopy(l1)
            l1 = l1.next
            cur = cur.next

        while l2 != None:
            cur.next = deepcopy(l2)
            l2 = l2.next
            cur = cur.next

        return head
