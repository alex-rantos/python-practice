from typing import List
from collections import Counter

"""Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first."""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        ans = []
        for key, val in counter.items():
            ans.append((key, val))
        ans.sort(key=lambda k: (-k[1], k[0]))
        ans = list(map(lambda k: k[0], ans))
        return ans[:k]

    def test(self):
        assert self.topKFrequent(["the", "day", "is", "sunny", "the", "the",
                                  "the", "sunny", "is", "is"], k=4) == ["the", "is", "sunny", "day"]
        assert self.topKFrequent(
            ["i", "love", "leetcode", "i", "love", "coding"], k=2) == ["i", "love"]
        assert self.topKFrequent(["i", "love", "leetcode", "leetcode",
                                  "i", "love", "coding", "coding"], 2) == ["coding", "i"]

if __name__ == "__main__":
    sol = Solution()
    sol.test()
