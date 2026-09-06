class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol, hash_arr = [], [], [False] * len(nums)
        
        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in range(0, len(nums)):
                if not hash_arr[i]:
                    sol.append(nums[i])
                    hash_arr[i] = True
                    backtrack()
                    sol.pop()
                    hash_arr[i] = False

        backtrack()
        return res