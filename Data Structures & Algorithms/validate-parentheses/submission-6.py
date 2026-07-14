class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if (n % 2) != 0 or not s:
            return False
        
        stack = []
        stack.append(s[0])
        for i in range(1 , n):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stack.append(s[i])
            else:
                if s[i] == ']':
                    if not stack:
                        return False
                    el = stack.pop()
                    if el != '[':
                        return False
                elif s[i] == '}':
                    if not stack:
                        return False
                    el = stack.pop()
                    if el != '{':
                        return False
                else :
                    if not stack:
                        return False
                    el = stack.pop()
                    if el != '(':
                        return False                               
        return not stack