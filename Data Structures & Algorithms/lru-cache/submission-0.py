class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.right = self.right
        self.right.left = self.left

    def remove(self, node):
        # remove a node from the list
        prev, nxt = node.left, node.right
        prev.right, nxt.left = nxt, prev
    
    def insert(self, node):
        # insert a node at the end of list but before self.right
        prev = self.right.left
        prev.right = node
        node.left = prev

        self.right.left = node
        node.right = self.right

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key]) # remove the node from current place
        self.insert(self.cache[key]) # replace the node to most recent right
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.remove(node)
            self.insert(node)
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.right
            self.remove(lru)
            del self.cache[lru.key]
        
