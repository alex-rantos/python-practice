"""
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
"""


class Solution:
    def isSubsequenceDP(self, s: str, t: str) -> bool:
        """ A Dynamic Programming approach """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        n = len(s)
        m = len(t)

        dp = [[0 for i in range(m)] for _ in range(n)]
        dp[0][0] = 1 if s[0] == t[0] else 0

        for i in range(1, n):
            if s[i] == t[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i-1][0]

        for i in range(1, m):
            dp[0][i] = 1 if t[i] == s[0] else dp[0][i-1]

        for i in range(1, n):
            for j in range(1, m):
                if s[i] == t[j]:
                    dp[i][j] = max(dp[i-1][j-1] + 1, dp[i][j-1])
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[-1][-1] == len(s)

    def testDP(self) -> None:
        assert self.isSubsequenceDP(s="abc", t="ahbgdc") == True
        assert self.isSubsequenceDP(s="axc", t="ahbgdc") == False

    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False

    def test(self) -> None:
        assert self.isSubsequenceDP(s="abc", t="ahbgdc") == True
        assert self.isSubsequenceDP(s="axc", t="ahbgdc") == False


if __name__ == "__main__":
    sol = Solution()
    sol.test()
