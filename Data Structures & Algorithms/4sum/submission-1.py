class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        i = 0
        while i < len(nums) - 3:
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):

                j = i + 1
                while j < len(nums) - 2:
                    if j == i + 1 or (j > i + 1 and nums[j] != nums[j - 1]):

                        k = j + 1
                        l = len(nums) - 1
                        while k < l:

                            tsum = nums[i] + nums[j] + nums[k] + nums[l]
                            if tsum < target:
                                k += 1
                    
                            elif tsum > target:
                                l -= 1
                    
                            else:
                                res.append([nums[i], nums[j], nums[k], nums[l]])
                                k += 1
                                l -= 1

                                while k < l and nums[k] == nums[k - 1]:
                                    k += 1
                                while k < l and nums[l] == nums[l + 1]:
                                    l -= 1
                
                    j += 1
            
            i += 1

        return res