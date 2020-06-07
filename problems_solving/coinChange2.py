from typing import List

"""
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.
"""


class Solution:
    def changeRecursive(self, amount: int, coins: List[int]) -> int:
        self.coins = coins

        def util(cur, curCoin):
            if (cur == 0):
                return 1
            elif (cur < 0):
                return 0
            combos = 0
            for i in range(curCoin, len(self.coins)):
                combos += util(cur - self.coins[i], i)
            return combos

        return util(amount, 0)

    def changeDP(self, amount: int, coins: List[int]) -> int:
        #dp = [[i for i in coins] for i in coins]
        if not coins:
            return 0
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                if j >= coin:
                    dp[j] += dp[j-coin]
        return dp[-1]

    def testRecursive(self):
        assert self.changeRecursive(5, [1, 5, 2]) == 4
        assert self.changeRecursive(3, [2]) == 0
        assert self.changeRecursive(5, [5]) == 1
        # print(self.changeRecursive(500, [3, 5, 7, 8, 9, 10, 11]))  # slow

    def testDP(self):
        assert self.changeDP(5, [1, 5, 2]) == 4
        assert self.changeDP(3, [2]) == 0
        assert self.changeDP(5, [5]) == 1
        assert self.changeDP(500, [3, 5, 7, 8, 9, 10, 11]) == 35502874


if __name__ == "__main__":
    sol = Solution()
    sol.testRecursive()
    sol.testDP()
