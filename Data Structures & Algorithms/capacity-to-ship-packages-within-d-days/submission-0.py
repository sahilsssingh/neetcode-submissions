class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        tweight = 0
        max_el = weights[0]
        for w in weights:
            tweight += w
            max_el = max(max_el, w)

        ans = tweight
        l = max_el
        r = tweight
        while l <= r:
            m = (l + r) // 2
            tdays = self.calculateDays(weights, m)

            if tdays <= days:
                ans = m
                r = m - 1
            
            else:
                l = m + 1

        return ans

    def calculateDays(self, weights, cap):
        tdays = 1
        summ = 0
        for w in weights:
            if summ + w <= cap:
                summ = summ + w

            elif summ + w > cap:
                summ = w
                tdays += 1
        
        return tdays