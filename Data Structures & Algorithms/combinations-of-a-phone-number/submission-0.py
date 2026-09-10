class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, sol = [], []
        digit_str = [0, 0, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def backtrack(i):
            if len(sol) == len(digits):
                res.append("".join(sol[:]))
                return

            num = int(digits[i])
            for j in range(len(digit_str[num])):
                sol.append(digit_str[num][j])
                backtrack(i + 1)
                sol.pop()

        if digits:
            backtrack(0)
        return res