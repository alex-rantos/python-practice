from typing import List
from collections import Counter
"""You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks."""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        counter = Counter(tasks)
        maxFreqOccurence = 0
        maxFreq = 0
        for k, v in counter.most_common():
            if maxFreq <= v:
                maxFreq = v
                maxFreqOccurence += 1
        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxFreqOccurence)

    def test(self):
        assert self.leastInterval(tasks=["A", "A", "A", "B", "B", "B"],
                                  n=2) == 8
        assert self.leastInterval(tasks=["A", "A", "A", "B", "B", "B"],
                                  n=0) == 6
        assert self.leastInterval(
            tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
            n=2) == 16


if __name__ == "__main__":
    sol = Solution()
    sol.test()