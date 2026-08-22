import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [stone for stone in stones]
        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            y = heapq.heappop_max(max_heap)
            x = heapq.heappop_max(max_heap)

            if x != y:
                heapq.heappush_max(max_heap, y - x)

        return max_heap[0] if max_heap else 0