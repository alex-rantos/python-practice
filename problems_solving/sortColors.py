from typing import List
"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
"""


class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        # O(n) solution
        cur = zeros = 0
        twos = len(nums)-1
        while (cur <= twos):
            if (nums[cur] == 0):
                nums[cur], nums[zeros] = nums[zeros], nums[cur]
                cur += 1
                zeros += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[twos] = nums[twos], nums[cur]
                twos -= 1

    def sortColorsN2(self, nums: List[int]) -> List[int]:
        # O(n^2) solution
        dic = {
            0: [],
            1: [],
            2: []
        }
        for i, c in enumerate(nums):
            dic[c].append(i)

        for i in range(len(nums)):
            if i < len(dic[0]):
                nums[i] = 0
            elif i < len(dic[0])+len(dic[1]):
                nums[i] = 1
            else:
                nums[i] = 2
