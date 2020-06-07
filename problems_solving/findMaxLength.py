from typing import List

def findMaxLength(nums: List[int]) -> int:
    dic = {0:-1}
    count = ans = 0
    for i,num in enumerate(nums):
        count += 1 if num == 1 else -1
        if count not in dic:
            dic[count] = i
        elif ans < i - dic[count]:
            ans = i - dic[count]
    return ans
        


if __name__ == '__main__':
    assert findMaxLength([0,1,0]) == 2
    assert findMaxLength([0,1,0,1]) == 4
    