class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        for i in range(0 , len(nums)):
            if target - nums[i] in hash_dict:
                return [hash_dict[target - nums[i]] , i]
            hash_dict[nums[i]] = i