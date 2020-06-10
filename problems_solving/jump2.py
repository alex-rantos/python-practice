from typing import List

"""Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps."""


class Solution:

    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        dp = [float('inf')] * len(nums)

        dp[0] = 1

        for i, num in enumerate(nums):

            for j in range(i, num + i + 1):
                if j >= len(dp):
                    break
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1] - 1

    def jumpRecursive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        self.min_jumps = float('inf')

        def util(nums, jumps):
            if (nums[0] >= len(nums) - 1):
                jumps += 1
                self.min_jumps = min(jumps, self.min_jumps)
                return
            for i in range(1, nums[0] + 1):
                if i >= len(nums):
                    break
                if nums[i] != 0:
                    util(nums[i:], jumps + 1)

        util(nums, 0)

        return self.min_jumps

    def testRecursive(self) -> None:
        assert (self.jump([5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1,
                           5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5])) == 5
        assert self.jump([2, 3, 1, 1, 4]) == 2
        assert self.jumpRecursive([2, 2, 4, 5, 1, 1, 3, 0, 0, 4]) == 3
        assert self.jumpRecursive([0]) == 0


if __name__ == "__main__":
    sol = Solution()
    sol.testRecursive()

    nums = [2, 3, 1, 1, 4]
    step = 0
    max_range = 0
    max_jump = [i + nums[i] for i in range(len(nums))]
    print(max_jump)
    # cache max value before i.
    max_before_i = [0] * len(nums)
    _max = max_jump[0]
    for (i, val) in enumerate(max_jump):
        if _max < val:
            _max = val
        max_before_i[i] = _max

    while max_range < len(nums) - 1:
        step += 1
        max_range = max_before_i[max_range]

    print(step)
