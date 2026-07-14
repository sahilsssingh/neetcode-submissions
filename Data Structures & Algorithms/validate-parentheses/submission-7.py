class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if (n % 2) != 0 or not s:
            return False
        
        stack = []
        for i in range(n):
            if s[i] in '([{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                el = stack.pop()
                if s[i] == ')' and el != '(':
                    return False
                elif s[i] == ']' and el != '[':
                    return False
                elif s[i] == '}' and el != '{':
                    return False
        
        return not stack