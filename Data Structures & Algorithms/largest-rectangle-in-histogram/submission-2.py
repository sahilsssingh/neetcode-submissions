class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(len(heights) + 1):
            cur_height = heights[i] if i < len(heights) else 0
            while stack and cur_height < heights[stack[-1]]:
                height = heights[stack.pop()]
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary - 1
                max_area = max(max_area , height * width)
            stack.append(i)
        
        return max_area