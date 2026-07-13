import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        if k == 0 or not nums:
            return nums

        ans = []

        heap = []
        for i in range(0, k):
            heapq.heappush(heap , (-nums[i] , i))
        ans.append(-heap[0][0])

        for r in range(k , len(nums)):
            heapq.heappush(heap , (-nums[r] , r))
            while heap[0][1] < r - k + 1:
                heapq.heappop(heap)

            ans.append(-heap[0][0])

        return ans