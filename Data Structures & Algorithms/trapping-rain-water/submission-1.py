class Solution:
    def trap(self, height: List[int]) -> int:
        right_max_arr = [0] * len(height)
        right_max = 0
        for i in range(len(height) - 1, -1, -1):
            right_max_arr[i] = right_max
            right_max = max(height[i], right_max)

        max_water = 0
        left_max = 0
        for i in range(0, len(height)):
            difference= min(right_max_arr[i], left_max) - height[i]
            if difference > 0:
                max_water += difference
            left_max = max(left_max, height[i])
            
        return max_water