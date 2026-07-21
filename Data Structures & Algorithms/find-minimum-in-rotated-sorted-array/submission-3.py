class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]
        el = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            elif nums[mid] < nums[0]:
                el = nums[mid]
                right = mid - 1
                
        return el