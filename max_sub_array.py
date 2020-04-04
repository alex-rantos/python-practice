
def max_sub_array( nums):
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    :type nums: List[int]
    :rtype: int
    """
    """ Brute force
    current_sum = 0
    neg = False
    max_sum = float('-inf')
    size = len(nums)
    for i in range(size): 
        for j in range(i, size):
            if (nums[j] < 0):
                neg = True
            current_sum += nums[j]
            if (current_sum > max_sum):
                max_sum = current_sum
        if (i == 1):
            if (neg == False):
                return max_sum
        current_sum = 0
    return max_sum"""

    """ 
    neg = False
    non_negative = 0
    max_sum = 0

    for x in nums:
        non_negative += x
        if (non_negative < 0):
            non_negative = 0
        else:
            neg = True

        if (non_negative > max_sum):
            max_sum = non_negative

    if neg == False:
        return max(nums)
    else:
        return max_sum"""
    
    # Fastest solution
    cur_sum = 0
    max_sum = 0
    for x in nums:
        cur_sum = max(cur_sum + x,x)
        max_sum = max(max_sum,cur_sum)
    return max_sum



if __name__ == '__main__':
    
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    _sum = sol.max_sub_array(arr)
    print(_sum)