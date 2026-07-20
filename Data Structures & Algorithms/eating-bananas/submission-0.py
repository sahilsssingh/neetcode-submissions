import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxel = max(piles)

        l = 1
        r = maxel
        ans = maxel
        while l <= r:
            m = (l + r) // 2
            totalH = self.totalhrs(piles, m)
            if totalH <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans

    def totalhrs(self, piles, m):
        total = 0
        for pile in piles:
            total += math.ceil(pile / m)
        return total