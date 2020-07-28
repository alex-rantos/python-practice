from typing import List
from collections import defaultdict

"""
You are given N fractions. Fractions are represented as 2 arrays, Y and Y of length N,
containing the fraction numerators and denominators respectively.

Write a function that given such arrays X,Y returns the total number of possible ways 
to choose a pair of fractions that sum up to 1. Since the answer can be large,
provide it module 10^9 + 7

NOTE: 1 fraction can form multiple pairs
"""


class Solution:
    def sumFractions(self, X: List[int], Y: List[int]) -> int:
        combinations = 0
        diffSet = defaultdict(int)
        for i in range(len(X)):
            left = round(1 - X[i]/Y[i],2)
            currentFract = round(X[i]/Y[i],2)
            if currentFract in diffSet:
                combinations += diffSet[currentFract]
            diffSet[left] += 1
        return combinations % (10^9 + 7)

    def test(self):
        assert self.sumFractions([1,1,2], [3,2,3]) == 1
        assert self.sumFractions([1,1,1], [2,2,2]) == 3
        assert self.sumFractions([1,2,3,1,2,12,8,4], [5,10,15,2,4,15,10,5]) == 10

if __name__ == "__main__":
    sol = Solution()
    sol.test()