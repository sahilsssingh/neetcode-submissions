import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap, (- ((point[0] ** 2 + point[1] ** 2) ** 0.5), point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [point[1] for point in heap]