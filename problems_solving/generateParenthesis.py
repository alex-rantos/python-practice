from typing import List
""" 
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. 
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def util(left, right, current):
            nonlocal ans
            nonlocal n
            if left == n and right == n:
                ans.append(current)
                return
            if left == 0 or left < n:
                util(left + 1, right, current + "(")
            if right < left:
                util(left, right + 1, current + ")")

        util(0, 0, "")

        return ans

    def test(self):
        assert self.generateParenthesis(3) == [
            "((()))", "(()())", "(())()", "()(())", "()()()"
        ]
        assert self.generateParenthesis(0) == [""]
        assert self.generateParenthesis(5) == [
            "((((()))))", "(((()())))", "(((())()))", "(((()))())",
            "(((())))()", "((()(())))", "((()()()))", "((()())())",
            "((()()))()", "((())(()))", "((())()())", "((())())()",
            "((()))(())", "((()))()()", "(()((())))", "(()(()()))",
            "(()(())())", "(()(()))()", "(()()(()))", "(()()()())",
            "(()()())()", "(()())(())", "(()())()()", "(())((()))",
            "(())(()())", "(())(())()", "(())()(())", "(())()()()",
            "()(((())))", "()((()()))", "()((())())", "()((()))()",
            "()(()(()))", "()(()()())", "()(()())()", "()(())(())",
            "()(())()()", "()()((()))", "()()(()())", "()()(())()",
            "()()()(())", "()()()()()"
        ]


if __name__ == "__main__":
    sol = Solution()
    sol.test()