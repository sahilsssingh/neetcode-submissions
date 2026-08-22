import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stone = [-stone for stone in stones]
        heapq.heapify(neg_stone)

        while len(neg_stone) > 1:
            y = -(heapq.heappop(neg_stone))
            x = -(heapq.heappop(neg_stone))

            if x != y:
                heapq.heappush(neg_stone, -(y - x))

        return -(heapq.heappop(neg_stone)) if neg_stone else 0