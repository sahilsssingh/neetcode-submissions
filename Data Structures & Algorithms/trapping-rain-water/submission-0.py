class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        for i in range(1 , n):
            prefix[i] = max(height[i - 1] , prefix[i - 1])
        
        sufix = [0] * n
        for i in range(n - 2 , -1 , -1):
            sufix[i] = max(height[i + 1] , sufix[i + 1])
        
        total = 0
        for i in range(0 , n):
            if height[i] < prefix[i] and height[i] < sufix[i]:
                total += min(prefix[i] , sufix[i]) - height[i]
        
        return total