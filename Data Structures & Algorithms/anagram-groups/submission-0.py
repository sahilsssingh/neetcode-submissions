class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        visited = [False] * len(strs)
        
        for i in range(0, len(strs)):
            if visited[i]:
                continue  # already grouped, skip
            
            s = [strs[i]]
            visited[i] = True
            
            for j in range(i + 1, len(strs)):
                if visited[j]:
                    continue  # already grouped, skip
                
                if len(strs[i]) == len(strs[j]):
                    count = [0] * 26
                    for char in strs[i]:
                        count[ord(char) - ord("a")] += 1
                    for char in strs[j]:
                        count[ord(char) - ord("a")] -= 1

                    is_anagram = True
                    for char in count:
                        if char != 0:
                            is_anagram = False
                            break
                    
                    if is_anagram:
                        s.append(strs[j])
                        visited[j] = True  # mark as grouped
            
            res.append(s)
        
        return res