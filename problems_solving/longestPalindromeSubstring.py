from collections import defaultdict
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""


class Solution:
    def is_palindrome(self, s):
        middle = len(s) // 2
        for i in range(middle + 1):
            if s[i] != s[len(s) - i - 1]:
                return -1
        return int(len(s))

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        dic = defaultdict(list)
        for i, ch in enumerate(s):
            dic[ch].append(i)

        ans = s[0]
        longest = 0

        for _, valList in dic.items():
            if len(valList) < 2:
                continue
            for l in range(len(valList)):
                count = 0
                for r in range(len(valList) - 1, l - 1, -1):
                    if longest > r - l:
                        break
                    checkStr = s[valList[l]:valList[r] + 1]
                    count = self.is_palindrome(checkStr)
                    if count > longest:
                        ans = checkStr
                        longest = count
        print(ans)
        return ans

    def test(self):
        assert self.longestPalindrome("babad") == "bab"
        assert self.longestPalindrome("cbbd") == "bb"
        assert self.longestPalindrome("dcacdbd") == "dcacd"
        assert self.longestPalindrome("a") == "a"


if __name__ == "__main__":
    sol = Solution()
    sol.test()