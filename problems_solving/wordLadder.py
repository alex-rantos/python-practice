"""Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same."""

from typing import List
from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        # pre-processing
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wordToAdd = word[:i] + "*" + word[i + 1:]
                adj[wordToAdd].append(word)

        deq = deque([(beginWord, 1)])
        visited = set()
        while deq:
            curWord, k = deq.popleft()
            if curWord == endWord:
                return k
            if curWord in visited:
                continue
            visited.add(curWord)
            for i in range(len(curWord)):
                nextWord = curWord[:i] + "*" + curWord[i + 1:]
                for neigh in adj[nextWord]:
                    if neigh not in visited:
                        deq.append((neigh, k + 1))
        return 0

    def test(self):
        assert self.ladderLength(
            "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
        assert self.ladderLength("hit", "cog",
                                 ["hot", "dot", "dog", "lot", "log"]) == 0


if __name__ == "__main__":
    sol = Solution()
    sol.test()