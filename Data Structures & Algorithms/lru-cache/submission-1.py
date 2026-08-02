class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash_dict = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.hash_dict:
            self.delete(self.hash_dict[key])
            self.insert(self.hash_dict[key])
            return self.hash_dict[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hash_dict:
            if len(self.hash_dict) == self.cap:
                del self.hash_dict[self.tail.prev.key]
                self.delete(self.tail.prev)
            self.insert(Node(key, value))
            self.hash_dict[key] = self.head.next
        else:
            self.hash_dict[key].val = value
            self.delete(self.hash_dict[key])
            self.insert(self.hash_dict[key])


    def insert(self, nodeReference):
        nodeReference.next = self.head.next
        nodeReference.prev = self.head
        self.head.next = nodeReference
        nodeReference.next.prev = nodeReference

    def delete(self, nodeReference):
        nodeReference.prev.next = nodeReference.next
        nodeReference.next.prev = nodeReference.prev
