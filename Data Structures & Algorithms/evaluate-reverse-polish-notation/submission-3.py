class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = "+-*/"
        for el in tokens:
            if el not in symbols:
                stack.append(int(el))
            else:
                if el == '+':
                    val = stack[-2] + stack[-1]

                elif el == '-':
                    val = stack[-2] - stack[-1]

                elif el == '*':
                    val = stack[-2] * stack[-1]

                elif el == '/':
                    val = int(stack[-2] / stack[-1])

                stack.pop()
                stack[-1] = val

        return stack[-1]