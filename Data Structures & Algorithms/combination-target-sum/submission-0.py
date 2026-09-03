class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol, res = [], []

        def backtrack(i, csum):
            if i == len(nums) or csum > target:
                return
            
            if csum == target:
                res.append(sol[:])
                return

            #dont pick
            backtrack(i + 1, csum)

            #pick again
            sol.append(nums[i])
            backtrack(i, csum + nums[i])
            sol.pop()  


        backtrack(0, 0)
        return res