class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            destroyed = False

            if asteroid > 0:
                stack.append(asteroid)
            
            elif asteroid < 0:
                while stack and stack[-1] > 0:
                    if stack[-1] < abs(asteroid):
                        stack.pop()
                    elif stack[-1] > abs(asteroid):
                        destroyed = True
                        break
                    else:
                        stack.pop()
                        destroyed = True
                        break
                    
                if (not stack or stack[-1] < 0) and not destroyed:
                    stack.append(asteroid)
                
        return stack