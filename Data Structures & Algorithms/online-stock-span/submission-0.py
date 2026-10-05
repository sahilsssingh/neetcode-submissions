class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        count = 0
        temp = []
        while self.stack and self.stack[-1] <= price:
            count += 1
            temp.append(self.stack.pop())

        while temp:
            self.stack.append(temp.pop())

        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)