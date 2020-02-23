
""" 
    If @arg 's' is palindrome return the length of the palindrome 
    If not return -1
"""
def is_palindrome(s):
    middle = len(s)//2
    for i in range(middle + 1):
        if s[i] != s[len(s) - i - 1]:
            return -1
    return int(len(s))

""" 
    Find the longest palindrome in a string

    Save each letter as a key in a dictionary and the each value is an array representing the position in each string
"""
def longest_palindrome(s):
    print(s)
    if len(s) <= 1:
        return len(s)

    d = {}
    for (i,ch) in enumerate(s):
        if ch not in d:
            d[ch] = [i]
        else:
            d[ch] += [i]
    longest = 1
    for (k,v) in d.items():
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                if (j == len(v)):
                    longest = max(longest, is_palindrome( s[v[i]:] ))
                else:        
                    longest = max(longest, is_palindrome( s[ v[i]:(v[j] + 1) ] ))
    return longest
        
if __name__ == '__main__':
    assert (longest_palindrome("a") == 1)
    assert (longest_palindrome("aa") == 2)
    assert (longest_palindrome("baa") == 2)
    assert (longest_palindrome("aab") == 2)
    assert (longest_palindrome("abcdefghba") == 1)
    assert (longest_palindrome("baablkj12345432133d") == 9)

""" @ fenring76(1 kyu)
def longest_palindrome(s):
    for size in range(len(s),0,-1):
        for i in range(len(s)-size+1):
            if s[i:i+size] == s[i:i+size][::-1]:
                return size
    return 0
"""