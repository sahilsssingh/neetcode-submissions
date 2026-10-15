class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sol = []
        read = [0] * len(nums)

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in range(len(nums)):
                if read[i] == 0:
                    if (i == 0 or nums[i] != nums[i - 1]) or read[i - 1] == 1:
                        sol.append(nums[i])
                        read[i] = 1
                        backtrack()
                        sol.pop()
                        read[i] = 0

        backtrack()
        return res