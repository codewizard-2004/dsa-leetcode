# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeLists(lists[i], lists[i-1])

        return lists[-1]

    def mergeLists(self, l1, l2):
        head = ListNode()
        ptr = head

        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next

        # Add the remaining nodes
        if l1:
            ptr.next = l1
        if l2:
            ptr.next = l2

        return head.next