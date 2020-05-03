"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.
"""

from collections import Counter

def can_construct(ransomNote: str, magazine: str) -> bool:
    r = Counter(ransomNote)
    m = Counter(magazine)
    
    for x in r.keys():
        
        if x not in m:
            return False
        else:
            if r[x] > m[x]:
                return False
    return True
        
if __name__ == "__main__":
    assert can_construct("a", "b") == False
    assert can_construct("aa", "ab") == False
    assert can_construct("aa", "aab") == True