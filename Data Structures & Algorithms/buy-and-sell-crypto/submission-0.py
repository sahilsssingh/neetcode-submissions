class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest = prices[0]
        for i in range(1 , len(prices)):
            if (prices[i] - smallest) > profit:
                profit = prices[i] - smallest
            if prices[i] < smallest:
                smallest = prices[i]
        
        return profit