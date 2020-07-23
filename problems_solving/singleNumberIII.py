from typing import List

"""Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
 Find the two elements that appear only once."""

class Solution: 
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        ans = []
        i = 0
        while i in range(len(nums) - 1):
            if nums[i+1] != nums[i]:
                ans.append(nums[i])
            else:
                while i in range(len(nums) - 1) and nums[i+1] == nums[i]:
                    i += 1
            i+=1
            
        if nums[-1] != nums[-2]:
            ans.append(nums[-1])
            
        return ans
            