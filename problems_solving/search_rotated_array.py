"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array."""

def search(nums, target: int) -> int:
    n = len(nums)
    if n == 1:
        if nums[0] == target: 
            return 0
        else:
            return -1
    low = (n-1)//2
    high = low + 1 if n%2 == 0 else low
    while low >= 0 and high < n:
        if nums[low] == target: return low
        if nums[high] == target: return high
        low -= 1
        high += 1
    return -1

if __name__ == "__main__":
    arr = [4,5,6,7,0,1,3]
    res1 = search(arr,0)
    res2 = search(arr,2)
    assert res1 == 4
    assert res2 == -1