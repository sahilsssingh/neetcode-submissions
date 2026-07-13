class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t or len(t) > len(s):
            return ""
        
        hash_array = [0] * 256
        for el in t:
            hash_array[ord(el)] += 1
        
        count = 0
        min_len = float('inf')
        start_index = -1

        l = 0
        for r in range(0 , len(s)):
            if hash_array[ord(s[r])] > 0:
                count += 1
            hash_array[ord(s[r])] -= 1
            
            while count == len(t):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start_index = l

                hash_array[ord(s[l])] += 1
                
                if hash_array[ord(s[l])] > 0:
                    count -= 1
                l += 1
        
        if start_index == -1:
            return ""

        return s[start_index : start_index + min_len]