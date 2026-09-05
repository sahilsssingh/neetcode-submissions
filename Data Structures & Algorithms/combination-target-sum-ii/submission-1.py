class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, sol = [], []
        
        def backtrack(i, csum):
            if csum == target:
                res.append(sol[:])
                return

            if i == len(candidates) or csum > target:
                return

            #pick
            sol.append(candidates[i])
            backtrack(i + 1, csum + candidates[i])
            sol.pop()

            #dont pick
            el = candidates[i]
            while i < len(candidates) and candidates[i] == el:
                i += 1
            backtrack(i, csum)

            
        backtrack(0, 0)
        return res