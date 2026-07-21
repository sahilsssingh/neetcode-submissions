class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return self.getIndex(l, nums, target)

    def getIndex(self, index, nums, target):

        if target >= nums[index] and target <= nums[-1]:
            L = index
            R = len(nums) - 1
        else: 
            L = 0
            R = index - 1

        while L <= R:
            M = (L + R) // 2
            if nums[M] < target:
                L = M + 1
            elif nums[M] == target:
                return M
            else:
                R = M - 1
        return -1