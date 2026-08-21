class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.K = k 
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        while len(self.heap) > self.K:
            heapq.heappop(self.heap)
        
        return self.heap[0]