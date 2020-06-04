from typing import List

"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s)//2):
        s[i],s[-i-1] = s[-i-1],s[i]
    return s
    #return s.reverse()

if __name__ == "__main__":
    assert reverseString(["h","e","l","l","o"]) == ["o","l","l","e","h"]
