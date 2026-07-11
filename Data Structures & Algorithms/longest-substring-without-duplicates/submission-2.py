class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        left = 0
        hash_dict = {}
        max_count = 0
        for right in range(n):
            if s[right] in hash_dict and hash_dict[s[right]] >= left:
                left = hash_dict[s[right]] + 1
            hash_dict[s[right]] = right
            max_count = max(max_count , right - left + 1)

        return max_count