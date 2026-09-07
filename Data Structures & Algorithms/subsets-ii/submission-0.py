class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, sol = [], []

        def backtrack(i):
            if i == len(nums):
                res.append(sol[:])
                return
            
            #pick
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            #dont pick
            el = nums[i]
            while i < len(nums) and nums[i] == el:
                i += 1
            backtrack(i)
        
        backtrack(0)
        return res