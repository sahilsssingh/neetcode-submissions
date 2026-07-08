import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_dict = {}
        for num in nums:
            hash_dict[num] = hash_dict.get(num , 0) + 1
        
        heap = []
        for key , value in hash_dict.items():
            heapq.heappush(heap , (-value , key))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res