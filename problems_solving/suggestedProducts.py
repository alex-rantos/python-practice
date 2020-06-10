"""Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. """

from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        if searchWord == "":
            return [[]]
        ans = []  # List[List[str]]
        arr = []  # List[str]
        for p in products:
            if p[0] == searchWord[0]:
                arr.append(p)
        if len(arr) > 3:
            ans.append(sorted(arr)[:3])
        else:
            ans.append(sorted(arr))

        for i in range(2, len(searchWord) + 1):
            curarr = []
            for w in arr:
                if (w[:i] == searchWord[:i]):
                    curarr.append(w)
            if len(curarr) > 3:
                ans.append(sorted(curarr)[:3])
            else:
                ans.append(sorted(curarr))
        return ans

    def test(self):
        assert self.suggestedProducts(products=["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord="mouse") == [
            ["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
        assert self.suggestedProducts(products=["havana"], searchWord="havana") == [
            ["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
        assert self.suggestedProducts(products=["havana"], searchWord="tatiana") == [
            [], [], [], [], [], [], []]
        assert self.suggestedProducts(["bags", "baggage", "banner", "box", "cloths"], searchWord="bags") == [
            ["baggage", "bags", "banner"], ["baggage", "bags", "banner"], ["baggage", "bags"], ["bags"]]


if __name__ == "__main__":
    sol = Solution()
    sol.test()
