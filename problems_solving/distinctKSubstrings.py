"""
Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. 
If the given string doesn't have k distinct characters, return 0.
"""


def distinctSubstrings(s: str, k: int) -> int:
    if not s:
        return 1 if k == 0 else 0
    counter = 0
    distinctCharacters = set()
    start = 0
    i = 0
    while start < len(s) - k + 1:
        c = s[i]
        if len(distinctCharacters) == k:
            if c in distinctCharacters:
                counter += 1
                print(start, i)
            else:
                start += 1
                i = start
                distinctCharacters.clear()
                continue
        elif len(distinctCharacters) < k:
            distinctCharacters.add(c)
            if len(distinctCharacters) == k:
                counter += 1
                print(start, i)
        i += 1
        if i >= len(s):
            start += 1
            i = start
            distinctCharacters.clear()
    return counter


def test():
    assert distinctSubstrings(s="pqpqs", k=2) == 7
    assert distinctSubstrings(s="aabab", k=3) == 0
    assert distinctSubstrings(s="aabab", k=2) == 9


if __name__ == "__main__":
    test()
