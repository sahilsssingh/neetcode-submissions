class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res, sol = [], []
        
        digit_map = {
            2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }
        
        def backtrack(i):
            if len(sol) == len(digits):
                res.append("".join(sol))
                return
            
            num = int(digits[i])
            for char in digit_map[num]:
                sol.append(char)
                backtrack(i + 1)
                sol.pop()
                
        backtrack(0)
        return res