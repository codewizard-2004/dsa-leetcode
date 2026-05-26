# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        ptr = head
        length = 0
        while ptr:
            length += 1
            ptr = ptr.next
        
        rem = length - n
        if rem == 0:
            return head.next

        ptr = head
        for _ in range(rem - 1):
            ptr = ptr.next
        
        ptr.next = ptr.next.next

        return head