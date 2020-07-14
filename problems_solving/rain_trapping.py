from typing import List
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
"""


class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        count = 0
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        while l < r:
            if height[l] < height[r]:
                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    count += (lmax - height[l])
                l += 1
            else:
                if height[r] >= rmax:
                    rmax = height[r]
                else:
                    count += (rmax - height[r])
                r -= 1
        return count

    def test(self):
        assert self.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
        assert self.trap([]) == 0
        assert self.trap([1, 1, 1, 1, 2]) == 0
        assert self.trap([10, 1, 1, 22]) == 18


if __name__ == "__main__":
    sol = Solution()
    sol.test()
