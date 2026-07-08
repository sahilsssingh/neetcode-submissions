class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        el = 0
        while el < len(s):
            num_str = ""
            while s[el] != "#":
                num_str += s[el]
                el += 1
            num = int(num_str)
            
            el += 1  
            
            string = ""
            for _ in range(num):
                string += s[el]
                el += 1
            
            res.append(string)
        
        return res