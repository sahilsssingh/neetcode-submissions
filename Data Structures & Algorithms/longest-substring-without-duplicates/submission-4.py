class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = r = 0
        seen = set()
        max_count = 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            max_count = max(max_count, r - l + 1)
            r += 1

        return max_count