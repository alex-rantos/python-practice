"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(-1)
    r = head
    add = 0
    while l1 != None and l2 != None:
        sum_ = l1.val + l2.val + add
        add = 0
        if sum_ > 10:
            add = sum_ - 10
            cur = ListNode(add)
            r.next = cur
            r = cur
            add = 1
        elif sum_ == 10:
            cur = ListNode(0)
            r.next = cur
            r = cur
            add = 1
        else:
            cur = ListNode(sum_)
            r.next = cur
            r = cur
        l1 , l2 = l1.next, l2.next
        
    if l1 != None:
        while l1 != None:
            sum_ = l1.val +  add
            add = 0
            if sum_ > 10:
                add = sum_ - 10
                cur = ListNode(add)
                r.next = cur
                r = cur
                add = 1
            elif sum_ == 10:
                cur = ListNode(0)
                r.next = cur
                r = cur
                add = 1
            else:
                cur = ListNode(sum_)
                r.next = cur
                r = cur
            l1  = l1.next
            print(sum_)
            print(l1)
    else:
        while l2 != None:
            sum_ = l2.val +  add
            add = 0
            if sum_ > 10:
                add = sum_ - 10
                cur = ListNode(add)
                r.next = cur
                r = cur
                add = 1
            elif sum_ == 10:
                cur = ListNode(0)
                r.next = cur
                r = cur
                add = 1
            else:
                cur = ListNode(sum_)
                r.next = cur
                r = cur
            l2  = l2.next
            
    if (add > 0):
        cur = ListNode(add)
        r.next = cur
        r = cur

    return head.next