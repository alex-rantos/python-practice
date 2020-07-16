from typing import List
"""Rotate the image by 90 degrees (clockwise). Do it in-place."""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()
        return matrix

    def test(self):
        assert self.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1],
                                                                  [8, 5, 2],
                                                                  [9, 6, 3]]
        assert self.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7],
                            [15, 14, 12, 16]]) == [[15, 13, 2,
                                                    5], [14, 3, 4, 1],
                                                   [12, 6, 8, 9],
                                                   [16, 7, 10, 11]]


if __name__ == "__main__":
    sol = Solution()
    sol.test()