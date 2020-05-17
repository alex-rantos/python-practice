"""Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100."""

from collections import Counter

class Solution:
    # non optimal solution
    def findAnagrams(self, s: str, p: str) -> [int]:
        orig = Counter(p)
        self.temp = {}
        self.ans = []
        self.add = False
        self.added,i = 0,0
        while i<len(s):
            x = s[i]
            if x not in orig:
                self.cleanDS(True)
                i+=1
                continue
            else:
                if self.add == False:
                    self.ans.append(i)
                    self.add = True
                if x in self.temp:
                    self.temp[x]+=1
                    if (self.temp[x] > orig[x]):
                        i = self.ans[-1] + 1 if len(self.ans) > 0 else i
                        self.cleanDS(True)
                        continue # dont go to next elem
                else:
                    self.temp[x]=1
                self.added+=1
            if self.added == len(p):
                if self.temp == orig:
                    i = self.ans[-1] + 1 if len(self.ans) > 0 else i
                    self.cleanDS()
                    continue # dont go to next elem
            i+=1
        if self.temp != orig and self.add:
            del self.ans[-1]
        return self.ans

    def cleanDS(self, everything = False):
        if everything == True:
            if self.add == True:
                del self.ans[-1]
        self.added = 0
        self.temp = {}
        self.add = False


if __name__ == "__main__":
    sol = Solution()
    assert [0,6] == sol.findAnagrams("cbaebabacd","abc")
    assert [0,1,2] == sol.findAnagrams("abab","ab")
    assert [1,2,3,5] == sol.findAnagrams("abacbabc","abc")