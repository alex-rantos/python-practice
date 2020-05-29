from typing import List


def countBits(num: int) -> List[int]:
    ans = [0] * (num + 1)
    for n in range(0, num+1):
        """
        n >> 1: Divide the number by 2
        n & 1 : Add 1 to the binary form. 
        """
        ans[n] = ans[n >> 1] + (n & 1)
    return ans


if __name__ == "__main__":
    assert countBits(5) == [0, 1, 1, 2, 1, 2]
