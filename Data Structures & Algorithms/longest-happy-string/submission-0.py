import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []

        heap = []
        if a:
            heap.append((-a, "a"))
        if b:
            heap.append((-b, "b"))
        if c:
            heap.append((-c, "c"))
        heapq.heapify(heap)

        while len(heap) > 1:
            _val, _char = heapq.heappop(heap)
            if len(res) < 2 or (res[-1] != _char or res[-2] != _char):
                res.append(_char)
                _val += 1
            else:
                _vall, _charr = heapq.heappop(heap)
                res.append(_charr)
                _vall += 1
                if _vall:
                    heapq.heappush(heap, (_vall, _charr))

            if _val:
                heapq.heappush(heap, (_val, _char))

        if heap:
            _val, _char = heapq.heappop(heap)
            while (_val) and (len(res) < 2 or (res[-1] != _char or res[-2] != _char)):
                res.append(_char)
                _val += 1

        return "".join(res)