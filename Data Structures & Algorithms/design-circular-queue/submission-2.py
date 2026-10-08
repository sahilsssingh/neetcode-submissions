class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.ke = k
        self.q = [0] * k
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.size < self.ke:
            self.rear = (self.rear + 1) % self.ke
            self.q[self.rear] = value
            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.size:
            self.front = (self.front + 1) % self.ke
            self.size -= 1
            return True
        return False

    def Front(self) -> int:
        if self.size:
            return self.q[self.front]
        return -1

    def Rear(self) -> int:
        if self.size:
            return self.q[self.rear]
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