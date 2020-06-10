from typing import List

"""Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array."""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        low, high = 0, len(nums) - 1

        while low <= high:
            if target > nums[low]:
                low += 1
            elif target == nums[low]:
                return low
            else:
                if low == 0:
                    return 0
                else:
                    if target > nums[low-1]:
                        return low

            if target < nums[high]:
                high -= 1
            elif target == nums[high]:
                return high
            else:
                if high == len(nums)-1:
                    return len(nums)
                else:
                    if target < nums[high - 1]:
                        return high
        return low

    def searchInsertOptimal(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (high + low) // 2
            if (target == nums[mid]):
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return low

    def test(self):
        assert self.searchInsert([1, 3, 5, 6], 5) == 2
        assert self.searchInsert([1, 3, 5, 6], 0) == 0
        assert self.searchInsert([1, 3, 5, 6], 2) == 1
        assert self.searchInsert([1, 3, 5, 6], 7) == 4
        assert self.searchInsert([1, 3], 2) == 1
        assert self.searchInsertOptimal([1, 3, 5, 6], 5) == 2
        assert self.searchInsertOptimal([1, 3, 5, 6], 0) == 0
        assert self.searchInsertOptimal([1, 3, 5, 6], 2) == 1
        assert self.searchInsertOptimal([1, 3, 5, 6], 7) == 4
        assert self.searchInsertOptimal([1, 3], 2) == 1

        print("Tests passed successfully")


if __name__ == "__main__":
    sol = Solution()
    sol.test()
