# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


def maximal_square(matrix: [[str]]) -> int:
    n = len(matrix)
    m = 0
    if n > 0:
        m = len(matrix[n - 1])

    dp = [[0] * (m+1) for _ in range(n+1)]
    max_sq = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if ord(matrix[i - 1][j - 1]) > 48:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_sq = max(dp[i][j], max_sq)
    return max_sq**2


if __name__ == "__main__":
    assert maximal_square([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
                          "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]) == 4
    assert maximal_square([[]]) == 0
    assert maximal_square([["0"]]) == 0
