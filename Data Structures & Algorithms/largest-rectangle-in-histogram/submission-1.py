class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        nse = self.NSE(heights)
        pse = self.PSE(heights)

        for i in range(0 , len(heights)):
            max_area = max(max_area , heights[i] * (nse[i] - pse[i] - 1))
        return max_area

    def NSE(self, heights):
        stack = []  
        ans = [len(heights)] * len(heights)  

        for i in range(len(heights) - 1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) > 0:
                ans[i] = stack[-1]
            stack.append(i)
        return ans

    def PSE(self, heights):
        stack = []  
        ans = [-1] * len(heights)  
        for i in range(0, len(heights)):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) > 0:
                ans[i] = stack[-1]
            stack.append(i)
        return ans