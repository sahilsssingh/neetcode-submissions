class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1
        count = 0
        while l < r:
            
            if s[l] == s[r]:
                l += 1
                r -= 1

            if s[l] != s[r]:
                #left
                left = l + 1
                right = r
                left_res = True
                while left < right:
                    if s[left] == s[right]:
                        left += 1
                        right -= 1
                    else:
                        left_res = False
                        break
                
                #right
                left = l
                right = r - 1
                right_res = True
                while left < right:
                    if s[left] == s[right]:
                        left += 1
                        right -= 1
                    else:
                        right_res = False
                        break
                
                return left_res or right_res
        
        return True