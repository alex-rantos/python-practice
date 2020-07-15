from collections import deque, Counter, defaultdict
"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t) or not t or not s:
            return ""

        t_set = Counter(t)
        orig = Counter(t)
        found = defaultdict(int)

        target_count = len(t)
        found_count = 0
        ans = ""
        l = 0
        currentLen = float('inf')

        for i, c in enumerate(s):

            if c in t_set:
                if not found:
                    l = i
                found[c] += 1
                if t_set[c] > 0:
                    t_set[c] -= 1
                    found_count += 1
                else:
                    if s[l] == c:
                        while l <= i:
                            if s[l] in t_set:
                                if found[s[l]] <= orig[s[l]]:
                                    break
                                else:
                                    found[s[l]] -= 1
                            l += 1

                if found_count == target_count:
                    r = i
                    curLen = r - l + 1
                    if curLen == target_count:
                        return s[l:r + 1]
                    else:
                        if curLen < currentLen:
                            currentLen = curLen
                            ans = s[l:r + 1]

        return ans

    def test(self):
        assert self.minWindow("ABB", "AD") == ""
        assert self.minWindow("ABBDAV", "ADV") == "DAV"
        assert self.minWindow("ADOBECODEBANC", "ABC") == "BANC"
        assert self.minWindow("AAABABAA", "AAABB") == "AABAB"


if __name__ == "__main__":
    sol = Solution()
    sol.test()
