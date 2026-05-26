# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        
        l1 = head
        l2 = prev

        while l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2
        
        

        