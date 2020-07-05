"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xorResult = x ^ y
        hd = 0
        while xorResult > 0:
            hd += xorResult & 1
            xorResult >>= 1
        return hd

    def test(self):
        self.hammingDistance(1, 4) == 2


if __name__ == "__main__":
    sol = Solution()
    sol.test()