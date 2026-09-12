class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, sol = [], []
        cols, diag1, diag2 = set(), set(), set()

        def backtrack(row):
            if len(sol) == n:
                res.append(sol[:])
                return

            for col in range(n):
                if col not in cols and (row + col) not in diag1 and (row - col) not in diag2:

                    temp = ["."] * n
                    temp[col] = "Q"
                    sol.append("".join(temp))

                    cols.add(col)
                    diag1.add(row + col)
                    diag2.add(row - col)

                    backtrack(row + 1)

                    sol.pop()
                    cols.discard(col)
                    diag1.discard(row + col)
                    diag2.discard(row - col)
                
        backtrack(0)
        return res