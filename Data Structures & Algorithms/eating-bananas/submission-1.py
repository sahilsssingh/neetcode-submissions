import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_el = max(piles)
        l = 1
        r = max_el
        ans = max_el
        while l <= r:
            m = (l + r) // 2
            totalhr = self.helper(piles, m)

            if totalhr <= h:
                ans = m
                r = m - 1

            else:
                l = m + 1

        return ans

    def helper(self, piles, mid):
        totalhr = 0
        for pile in piles:
            totalhr += math.ceil(pile / mid)
        
        return totalhr