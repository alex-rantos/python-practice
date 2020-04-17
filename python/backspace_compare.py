"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Requirements:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
"""
def get_char(s,pos):
    if pos >= 0:
        return s[pos]
    else:
        return ""

def backspace_compare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    x = len(S) - 1
    y = len(T) - 1
    c1 = c2 = 0
    while (x >= 0 or y >= 0):
        while (get_char(S,x) == "#"):
            x -= 1
            c1 += 1
        while (get_char(T,y) == "#"):
            y -= 1
            c2 += 1
        while(c1 > 0 and get_char(S,x) != '#'):
            x -= 1
            c1 -= 1
        while(c2 > 0 and get_char(T,y) != '#'):
            y -= 1
            c2 -= 1
        if (c1 == 0 and c2 == 0 and get_char(S,x) != '#' and get_char(T,y) != '#'):
            if get_char(S,x) == get_char(T,y):
                x -= 1
                y -= 1
            else:
                return False
    return True

if __name__ == "__main__":
    S1 = "ab#c"
    T1 = "ad#c"
    r1 = backspace_compare(S1,T1)
    assert r1 == True
    S2 = "a##c"
    T2 = "#a#c"
    r2 = backspace_compare(S2,T2)
    assert r2 == True
    S3 = "a#c"
    T3 = "b"
    r3 = backspace_compare(S3,T3)
    print(r3)
    assert r3 == False
    S4 = "ab##"
    T4 = "c#d#"
    r4 = backspace_compare(S4,T4)
    assert r4 == True
    S5 = "bbbextm"
    T5 = "bbb#extm"
    r5 = backspace_compare(S5,T5)
    assert r5 == False
    