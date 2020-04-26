"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
 
If there is no common subsequence, return 0.
"""
import collections
def longest_common_subsequence(text1: str, text2: str) -> int:
    n1 = len(text1) +1 
    n2 = len(text2) + 1
    dp = [[0 for i in range(n2)]for i in range(n1)]
    for i in range(1,n1):
        for j in range(1,n2):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    #print(dp)
    return (dp[-1][-1])

if __name__ == "__main__":
    assert longest_common_subsequence(text1 = "abcde", text2 = "ace") == 3
    assert longest_common_subsequence(text1 = "abc", text2 = "abc")   == 3
    assert longest_common_subsequence(text1 = "abc", text2 = "def")   == 0
    assert longest_common_subsequence(text1 = "pmjghexybyrgzczy", text2 = "hafcdqbgncrcbihkd") == 4