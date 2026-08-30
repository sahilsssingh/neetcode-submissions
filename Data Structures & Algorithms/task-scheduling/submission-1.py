import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_dict = {}
        for task in tasks:
            hash_dict[task] = hash_dict.get(task, 0) + 1

        maxHeap = [-count for count in hash_dict.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while q or maxHeap:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time