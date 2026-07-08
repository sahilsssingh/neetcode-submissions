class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                product = product * num
            else: 
                zero_count += 1
        
        res = []
        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            for num in nums:
                res.append(product if num == 0 else 0)
        else:
            for num in nums:
                res.append(product // num)
        return res