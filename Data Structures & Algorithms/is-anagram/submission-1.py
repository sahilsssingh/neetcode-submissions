class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = {}
        hash2 = {}
        for x in s:
            hash1[x] = hash1.get(x , 0) + 1
        for x in t:
            hash2[x] = hash2.get(x , 0) + 1
        for key in hash1:
            if key in hash2:
                if hash1[key] != hash2[key]:
                    return False
            else:
                return False
        return True