from typing import List
"""
Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

Conditions:

    You will pick exactly 2 numbers.
    You cannot pick the same element twice.
    If you have muliple pairs, select the pair with the largest number.
"""


def sum(nums: List[int], target: int) -> List[int]:
    if (len(nums) <= 1) or target - 30 < 0:
        return []
    target = target - 30
    remaining = {}
    targetPairs = []
    biggestNum = 0
    indexPair = -1
    for i, num in enumerate(nums):
        diff = target-num
        if diff < 0:
            continue
        if not diff in remaining:
            remaining[diff] = i
        if num in remaining and remaining[num] != i:
            targetPairs.append([remaining[num], i])
            if num > biggestNum or nums[remaining[num]] > biggestNum:
                biggestNum = max(nums[remaining[num]], num)
                indexPair = len(targetPairs) - 1
    return targetPairs[indexPair]


def test():
    assert sum([], 90) == []
    assert sum([0, 0], 30) == [0, 1]
    assert sum([0, 4, 30, 0], 60) == [0, 2]
    assert sum([1, 10, 25, 35, 60], 90) == [2, 3]
    assert sum([20, 50, 40, 25, 30, 10], 90) == [1, 5]


if __name__ == "__main__":
    test()
