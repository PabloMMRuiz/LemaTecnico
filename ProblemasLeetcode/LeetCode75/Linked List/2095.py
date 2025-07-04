from typing import Optional
# Definition for singly-linked list.
class ListNode:
      def __init__(self, val=0, next=None):
          self.val = val
          self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None and head.next == None: return None
        slow = ListNode(0, head)
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return head