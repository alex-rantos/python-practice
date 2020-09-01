from typing import List
"""Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        ans = set()

        if set(s) > set(''.join(wordDict)):
            return []

        def util(s, wordSet, path, ans):
            if s == "":
                ans.add(path.strip())
                return

            for prefix in wordSet:
                if len(prefix) > len(s):
                    continue

                if s.startswith(prefix):
                    util(s[len(prefix):], wordSet,
                         path + " " + s[:len(prefix)], ans)

            return

        util(s, wordSet, "", ans)
        return (list(ans))

    def test(self):
        assert self.wordBreak(s="catsandog",
                              wordDict=["cats", "dog", "sand", "and",
                                        "cat"]) == []
        assert self.wordBreak(s="catsanddog",
                              wordDict=["cat", "cats", "and", "sand", "dog"
                                        ]) == ["cat sand dog", "cats and dog"]
        self.wordBreak("aaaaaaaaaaaaaaaa", ["a", "aa", "aaaaa", "aaaaaa"])


if __name__ == "__main__":
    sol = Solution()
    sol.test()