"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
""" FASTEST SOLUTION:        
    for i in range(1, len(grid[0])):
        grid[0][i] += grid[0][i-1]
    
    for i in range(1, len(grid)):
        grid[i][0] += grid[i-1][0]
    
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    return grid[-1][-1]
"""
def minimum_path_sum(grid):
    if not grid:
        return 0
    dp = [[0] * len(grid[0])]*len(grid)
    dp[0][0] = grid[0][0]
    for i in range(len(grid)):
        if (i > 0):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,len(grid[0])):
            if i == 0 and j > 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
    return dp[-1][-1]

if __name__ == "__main__":
    grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
    ]
    result = minimum_path_sum(grid)
    assert result == 7