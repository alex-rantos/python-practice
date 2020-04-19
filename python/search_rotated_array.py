""" Print the product of the array except of array[i] without division """
def array_product(nums):
    if len(nums) == 1:
        return nums

    left = [0]*len(nums)
    right = [0] * len(nums)
    left[0] = 1
    right[-1] = 1
    for i in range(1,len(nums)):
        left[i] = left[i-1] * nums[i-1] 

    for i in range(len(nums) - 2, -1, -1):
        right[i] = nums[i+1] * right[i+1]
    for i in range(len(nums)):
        right[i] = (right[i] * left[i])
        
    return right

if __name__ == "__main__":
    a = [1,2,3,4]
    p = array_product(a) 
    print(p)