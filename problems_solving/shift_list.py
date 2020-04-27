"""You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations."""
def shift_list(s,shift):
    sh = 0
    for direction,amount in shift:
        if direction:
            # shift right
            sh -= amount
        else:
            # shift left
            sh += amount 
    sh = sh % len(s)
    return s[sh:] + s[:sh]

    

if __name__ == "__main__":
    s = "xqgwkiqpif"
    shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
    res = shift_list(s,shift)
    print(res)
    assert (res == "qpifxqgwki")