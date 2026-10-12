import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        ans_arr = []
        hash_dict = {}
        for char in s:
            if char not in hash_dict:
                hash_dict[char] = 1
            else:
                hash_dict[char] += 1

        heap = []
        for key, value in hash_dict.items():
            heap.append((-value, key))

        heapq.heapify(heap)

        prev = None
        while heap:
            _freq, _char = heapq.heappop(heap)
            ans_arr.append(_char)
            freq = _freq + 1
            
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            if freq < 0:
                prev = (freq, _char)
            
        if len(ans_arr) != len(s):
            return ""

        return "".join(ans_arr) 