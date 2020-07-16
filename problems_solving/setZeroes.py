from typing import List
"""Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place."""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def zero(i, j):
            nonlocal matrix
            for col in range(len(matrix[i])):
                matrix[i][col] = 0
            for row in range(len(matrix)):
                matrix[row][j] = 0

        arr = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    arr.append((row, col))

        for i, j in arr:
            zero(i, j)
        return matrix

    def test(self):
        assert self.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1],
                                                                     [0, 0, 0],
                                                                     [1, 0, 1]]
        assert self.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2],
                               [1, 3, 1, 5]]) == [[0, 0, 0, 0], [0, 4, 5, 0],
                                                  [0, 3, 1, 0]]


if __name__ == "__main__":
    sol = Solution()
    sol.test()