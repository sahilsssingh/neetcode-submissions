import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        n = len(tasks)

        indexed_tasks = []
        for i in range(n):
            enqueue_time = tasks[i][0]
            processing_time = tasks[i][1]
            indexed_tasks.append((enqueue_time, processing_time, i))

        indexed_tasks.sort()

        heap = []
        res = []
        time = indexed_tasks[0][0]
        i = 0

        while len(res) < n:
            
            while i < n and indexed_tasks[i][0] <= time:
                enqueue_time, processing_time, original_index = indexed_tasks[i]
                heapq.heappush(heap, (processing_time, original_index))
                i += 1

            if heap:
                processing_time, original_index = heapq.heappop(heap)
                time += processing_time
                res.append(original_index)
            else:
                time = indexed_tasks[i][0]

        return res