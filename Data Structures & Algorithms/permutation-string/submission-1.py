class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_s1 = [0] * 26
        hash_s2 = [0] * 26
        if len(s1) > len(s2):
            return False
            
        for i in range(len(s1)):
            hash_s1[ord(s1[i]) - ord('a')] += 1

        for r in range(len(s1)):
            hash_s2[ord(s2[r]) - ord('a')] += 1
            if hash_s1 == hash_s2:
                return True

        for r in range(len(s1), len(s2)):
            hash_s2[ord(s2[r]) - ord('a')] += 1
            hash_s2[ord(s2[r - len(s1)]) - ord('a')] -= 1
            if hash_s1 == hash_s2:
                return True
        return False