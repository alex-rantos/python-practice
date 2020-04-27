"""
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.
Constraints:
    1 <= arr.length <= 1000
    0 <= arr[i] <= 1000
"""

def counting_elemenets(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    count_duplicates = 0
    dic = {}
    for x in arr:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
    for k in dic:
        if k+1 in dic:
            count_duplicates +=  dic[k]
    return count_duplicates


if __name__ == '__main__':
    arr1 = [1,2,3]
    arr2 = [1,1,3,3,5,5,7,7]
    arr3 = [1,3,2,3,5,0]
    arr4 = [1,1,2,2]
    r1 = counting_elemenets(arr1)
    r2 = counting_elemenets(arr2)
    r3 = counting_elemenets(arr3)
    r4 = counting_elemenets(arr4)
    assert(r1 == 2)
    assert(r2 == 0)
    assert(r3 == 3)
    assert(r4 == 2)
