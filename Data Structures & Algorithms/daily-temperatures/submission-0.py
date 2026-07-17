class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results =[0] * len(temperatures)
        for i in range(0 , len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                results[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            if not stack or temperatures[i] <= stack[-1][0]:
                stack.append([temperatures[i] , i])
        return results