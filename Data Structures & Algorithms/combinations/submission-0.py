class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        res = []

        def backtrack(num):
            if len(sol) == k:
                res.append(sol[:])
                return
            
            for i in range(num, n + 1):
                sol.append(i)
                backtrack(i + 1)
                sol.pop()

        backtrack(1)
        return res