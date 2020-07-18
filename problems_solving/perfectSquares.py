"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
"""

import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)

        for i in range(1,n+1):
            for j in range(1,int(math.sqrt(i) + 1)):
                dp[j] = min(dp[j], dp[i-j*j]+1)
        print(dp)
        return dp[-1]
    
    def test(self):
        assert self.numSquares(0) == 0
        assert self.numSquares(1) == 1
        assert self.numSquares(2) == 1
        assert self.numSquares(4) == 2
        assert self.numSquares(5) == 3
        assert self.numSquares(12) == 3
        assert self.numSquares(13) == 2

if __name__ == "__main__":
    sol = Solution()
    sol.test()
        