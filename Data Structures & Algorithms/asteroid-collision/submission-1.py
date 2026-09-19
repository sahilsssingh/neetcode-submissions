class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                diff = a + stack[-1]

                if diff < 0:
                    stack.pop()

                elif diff > 0:
                    a = 0
                    break

                else:
                    stack.pop()
                    a = 0
                    break

            if a:
                stack.append(a)

        return stack