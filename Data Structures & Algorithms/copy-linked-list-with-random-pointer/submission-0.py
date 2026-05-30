"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtoCopy = {None: None}

        # copy all the original nodes and store its copy as value
        ptr = head
        while ptr:
            oldtoCopy[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        # copy all the random and next pointers
        ptr = head
        while ptr:
            copyNode = oldtoCopy[ptr]
            copyNode.next = oldtoCopy[ptr.next]
            copyNode.random = oldtoCopy[ptr.random]
            ptr = ptr.next
        
        return oldtoCopy[head]

        