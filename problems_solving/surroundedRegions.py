from typing import List

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


class Solution:
    border = False

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        onBorder = set()

        def bordered(i, j):
            nonlocal board
            if i == 0 or j == 0:
                return True
            if i == len(board) - 1 or j == len(board[i])-1:
                return True
            return False

        def dfs(row, col, v=False):
            nonlocal visited
            nonlocal board

            if not v:
                v = bordered(row, col)
                if v:
                    self.border = True

            visited.add((row, col))

            if row+1 < len(board) and (row+1, col) not in visited and board[row+1][col] == 'O':
                dfs(row+1, col, v)
            if row-1 >= 0 and (row-1, col) not in visited and board[row-1][col] == 'O':
                dfs(row-1, col, v)
            if col+1 < len(board[row]) and (row, col+1) not in visited and board[row][col+1] == 'O':
                dfs(row, col+1, v)
            if col-1 >= 0 and (row, col-1) not in visited and board[row][col-1] == 'O':
                dfs(row, col-1, v)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and (i, j) not in onBorder:
                    dfs(i, j, False)
                    if not self.border:
                        #print("CHANGING" + str(visited))
                        for r, c in visited:
                            board[r][c] = 'X'
                    else:
                        #print("BORDER" + str(visited))
                        onBorder &= visited

                    visited.clear()
                    self.border = False
