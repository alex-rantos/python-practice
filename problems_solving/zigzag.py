"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        rowsLen = 0
        while n > 0:
            n -= numRows
            rowsLen += 1
            counter = 0
            while n > 0 and counter < numRows - 2:
                n -= 1
                counter += 1
                rowsLen += 1
        arr = [[None for __ in range(rowsLen)] for _ in range(numRows)]
        ch = i = j = 0
        zigzag = False
        while ch < len(s) and i in range(numRows) and j in range(rowsLen):
            if zigzag:
                while ch < len(s) and i > 0 and j < len(arr[i]):
                    arr[i][j] = s[ch]
                    i -= 1
                    j += 1
                    ch += 1
                zigzag = False
            else:
                while ch < len(s) and i < len(arr):
                    arr[i][j] = s[ch]
                    i += 1
                    ch += 1
                j += 1
                i = len(arr) - 2
                zigzag = True
        ans = ""
        for r in arr:
            for char in r:
                if char != None:
                    ans += char
        return ans

    def test(self):
        assert self.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
        assert self.convert("PAYPALISHIRING", 1) == "PAYPALISHIRING"
        assert self.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"


if __name__ == "__main__":
    sol = Solution()
    sol.test()
