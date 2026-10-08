class Node:

    def __init__(self, value = 0, nextt = None):
        self.value = value
        self.next = nextt

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.ke = k
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.size == 0:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
            return True
        elif self.size < self.ke:
            self.tail.next = Node(value)
            self.tail = self.tail.next
            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.size:
            self.head = self.head.next
            self.size -= 1
            return True
        return False

    def Front(self) -> int:
        if self.size:
            return self.head.value
        return -1

    def Rear(self) -> int:
        if self.size:
            return self.tail.value
        return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.ke:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()