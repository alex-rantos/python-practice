from typing import List
"""Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.
Note:The same word in the dictionary may be reused multiple times in the segmentation.You may assume the dictionary does not contain duplicate words."""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set([word for word in wordDict])

        def dfs(target: str, index: int) -> bool:
            nonlocal wordSet
            nonlocal memo
            if target == "":
                return True
            if target in memo:
                return memo[target]
            for i in range(len(target) + 1):
                if target[:i] in wordSet and dfs(target[i:], i):
                    memo[target[i:]] = True
                    return True

            memo[target] = False
            return False

        ans = dfs(s, 0)
        return ans

    def wordBreakTLE(self, s: str, wordDict: List[str]) -> bool:
        #TLE : Time Limit Exceeded O(2^n)
        startSet = set(c for c in s)
        wSet = set()
        for w in wordDict:
            for c in w:
                wSet.add(c)

        def util(s, wordDict):
            if not s:
                return True
            n = len(s)
            for word in wordDict:
                l = len(word)
                if l > n:
                    continue
                else:
                    if s[:l] == word:
                        if util(s[l:], wordDict):
                            return True

        if startSet.intersection(wSet) == startSet:
            return util(s, sorted(wordDict)[::-1])
        else:
            return False

    def test(self):
        assert self.wordBreak(s="leetcode", wordDict=["leet", "code"]) == True
        assert self.wordBreak(s="applepenapple", wordDict=["apple",
                                                           "pen"]) == True
        assert self.wordBreak(s="catsandog",
                              wordDict=["cats", "dog", "sand", "and",
                                        "cat"]) == False
        assert self.wordBreak(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            [
                "aa", "aaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa",
                "aaaaaaaaaaaaaaaaaaaaaaaaa"
            ]) == False
        assert self.wordBreak(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            [
                "aa", "aaaaaaa", "aaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa",
                "aaaaaaaaaaaaaaaaaaaaaaaaa"
            ]) == True


if __name__ == "__main__":
    sol = Solution()
    sol.test()