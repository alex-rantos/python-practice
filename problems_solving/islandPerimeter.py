from typing import List
"""You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def bfs(i, j):
            nonlocal grid
            currentBlockDiameter = 0
            if i not in range(len(grid)) or j not in range(len(
                    grid[i])) or grid[i][j] == 0:
                currentBlockDiameter += 1
                return currentBlockDiameter
            if grid[i][j] == -1:
                return 0
            grid[i][j] = -1
            moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for x, y in moves:
                currentBlockDiameter += bfs(i + x, j + y)
            #grid[i][j] = 1
            return currentBlockDiameter

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return bfs(r, c)
        return 0

    def test(self):
        assert self.islandPerimeter([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                                     [0, 0, 0, 0]]) == 0
        assert self.islandPerimeter([]) == 0
        assert self.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0],
                                     [1, 1, 0, 0]]) == 16
        assert self.islandPerimeter([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
                                     [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1,
                                                                  1]]) == 20
        assert self.islandPerimeter([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],
                                     [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0],
                                     [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1],
                                     [1, 1, 1, 1], [1, 1, 1, 1]]) == 36


if __name__ == "__main__":
    sol = Solution()
    sol.test()