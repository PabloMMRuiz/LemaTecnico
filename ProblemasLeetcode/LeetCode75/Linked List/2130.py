# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head == None: return 0
        # 1. Find the half of the list, we will uso two pointers one of speed 1 and the other speed 2
        dummy = ListNode(0,head)
        half = dummy
        while head != None and head.next != None:
            head = head.next.next
            half = half.next
        half = half.next
        head = dummy.next
        # 2. Reverse the list from the half
        node = None
        while half:
            temp = half.next
            half.next = node
            node = half
            half = temp
        # 3. Transverse the two new lists and add pair's values
        max = -float("inf")
        while node and head:
            v = node.val + head.val
            if v > max:
                max = v
            node = node.next
            head = head.next
        return max