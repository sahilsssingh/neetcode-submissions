class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol, hash_set = [], [], set()
        
        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for num in nums:
                if num not in hash_set:
                    sol.append(num)
                    hash_set.add(num)
                    backtrack()
                    hash_set.discard(num)
                    sol.pop()

        backtrack()
        return res