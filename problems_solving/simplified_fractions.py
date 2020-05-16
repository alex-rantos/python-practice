"""Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. The fractions can be in any order."""

def simplifiedFractions(self, n: int) -> List[str]:
    ans = []
    dic = set()
    if n == 1: return ans
    for i in range(1,n):
        for j in range(2,n+1):
            if (i>=j): continue
            if i/j in dic:
                continue
            else:
                num = str(i)+"/"+str(j)
                ans.append(num)
                print(num)
                dic.add(i/j)
            
    return ans
    