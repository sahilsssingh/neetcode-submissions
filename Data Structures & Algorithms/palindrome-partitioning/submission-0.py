class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []

        def is_palindrome(substring):
            for i in range(len(substring) // 2):
                if substring[i] != substring[len(substring) - i - 1]:
                    return False
            return True

        def backtrack(start_index):
            if start_index == len(s):
                res.append(sol[:])
                return
            
            for end_index in range(start_index + 1, len(s) + 1):
                substring = s[start_index:end_index]

                if is_palindrome(substring):
                    sol.append(substring)
                    backtrack(end_index)
                    sol.pop()


        backtrack(0)
        return res