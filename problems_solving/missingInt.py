"""Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000]."""


def solution(A):
    # write your code in Python 3.6
    if not A:
        return None
    A = sorted(A)
    A = list(filter(lambda x : x>0, A))
    print(A)
    if not A:
        return 1
    if A[0] > 1:
        return 1
    for i in range(len(A) - 1):
        if A[i] > 0:
            if A[i+1] - A[i] not in range(2):
                return A[i] + 1
    return A[-1] + 1

def test():
    assert solution([-1,-4])
    assert solution([1,2,4,5]) == 3
    assert solution([1,2,3,4,5]) == 6
    #assert solution([]) == 3

if __name__ == "__main__":
    test()
    