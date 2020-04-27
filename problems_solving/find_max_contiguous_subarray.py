"""Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1."""

def find_max_length(nums) -> int:
    max_len = 0
    counter = 0
    dic = {0:-1}
    for i in range(len(nums)):
        counter = counter + 1 if nums[i] else counter - 1
        if counter not in dic:
            dic[counter] = i
        else:
            max_len = max(max_len, i - dic[counter])
    return max_len 



if __name__ == "__main__":
    a1 = [0,1]
    r1 = find_max_length(a1)
    print(r1)
    a2 = [0,1,0]
    r2 = find_max_length(a2)
    print(r2)
    a3 = [0,1,0,1]
    r3 = find_max_length(a3)
    assert(r3 == 4)
    assert(r1 == 2)
    assert(r2 == 2)

        
        