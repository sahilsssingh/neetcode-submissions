class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.K = k 
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, -num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)

        popped = []
        for _ in range(self.K -1):
            popped.append(heapq.heappop(self.heap))
        largestK = self.heap[0]

        for el in popped:
            heapq.heappush(self.heap, el)
        
        return -largestK
