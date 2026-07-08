class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_dict = {}
        for num in nums:
            hash_dict[num] = hash_dict.get(num , 0) + 1
        for el in hash_dict:
            if hash_dict[el] > 1:
                return True
        return False