"""Given a binary array, find the maximum length of a subarray whos elements are changing continously or stay the same."""

def find_max_length(nums) -> int:
    length = len(nums)
    max_len = 0
    continuous = 1
    for i in range(len(nums) - 1):
        if not nums[i] ^ nums[i+1] == 1:
            max_len = max(continuous,max_len)
            continuous = 1
        else:
            continuous += 1
    if continuous > 1:
        max_len = max(continuous,max_len)
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

        
        