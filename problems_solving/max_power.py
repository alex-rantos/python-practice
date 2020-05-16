"""Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.
"""
def maxPower(self, s: str) -> int:
    c = 1
    ans= 0
    found=False
    for i in range(0,len(s)-1):
        if s[i] == s[i+1]:
            c+=1
            found=True
        else:
            ans = max(c,ans)
            c=1
    return max(ans,c)