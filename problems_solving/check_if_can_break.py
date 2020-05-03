"""Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa (in other words s2 can break s1).

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1."""

def check_if_can_break(s1: str, s2: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)
    if n1!=n2 : return None
    arr1 = sorted([ord(x) for x in s1])
    arr2 = sorted([ord(x) for x in s2])
    i = 0
    while arr1[i]==arr2[i]:
        i += 1
    ret = (arr1[i] > arr2[i])
    for i in range(i,n1):
        if (x:=arr1[i] > arr2[i]) != ret:
            if arr1[i] == arr2[i]: 
                continue
            else:
                return False
    return True

if __name__ == "__main__":
    assert check_if_can_break(s1 = "abc", s2 = "xya") == True
    assert check_if_can_break(s1 = "abe", s2 = "acd") == False
    assert check_if_can_break(s1 = "leetcodee", s2 = "interview") == True