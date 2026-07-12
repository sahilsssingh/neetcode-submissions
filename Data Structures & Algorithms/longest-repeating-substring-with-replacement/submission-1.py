class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = max_lenght = l = 0
        hash_array = [0] * 26

        for r in range(len(s)):
            hash_array[ord(s[r]) - ord('A')] += 1
            max_freq = max(max_freq , hash_array[ord(s[r]) - ord('A')])

            while (r - l + 1) - max_freq > k:
                hash_array[ord(s[l]) - ord('A')] -= 1
                l += 1

            max_length = max(max_lenght , r - l + 1)

        return max_length