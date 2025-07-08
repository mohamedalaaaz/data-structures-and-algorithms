class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtarck(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtarck(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtarck(openN, closedN + 1)
                stack.pop()

        backtarck(0, 0)
        return res






