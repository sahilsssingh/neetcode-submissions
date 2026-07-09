class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[char.lower() for char in s if char.isalnum()]
        for i in range(0 , len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True