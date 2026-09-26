class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        sol, res = [], []

        def backtrack(i):
            if len(sol) == k:
                res.append(sol[:])
                return
            if i > n:
                return

            # don't pick i
            backtrack(i + 1)

            # pick i
            sol.append(i)
            backtrack(i + 1)
            sol.pop()

        backtrack(1)
        return res