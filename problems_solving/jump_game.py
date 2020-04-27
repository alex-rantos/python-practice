"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""
def can_jump(nums: [int]) -> bool:
    n = len(nums)
    if n == 1: return True
    max_jump = 0
    for i in range(0,n):
        if nums[i] == 0 and max_jump <= i:
            if max_jump != n - 1:
                return False
        max_jump = max(max_jump,i+nums[i])
    return True


if __name__ == "__main__":
    
    assert can_jump([2,3,1,1,4]) == True
    assert can_jump([3,2,1,0,4]) == False
    assert can_jump([2,0,0]) == True