
def move_zeroes( nums):
    """
    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    :type nums: List[int]
    """
    for x in nums:
        if x == 0:
            nums.remove(0)
            nums.append(0)

if __name__ == '__main__':
    
    nums = [0,1,0,3,12]
    move_zeroes(nums)

