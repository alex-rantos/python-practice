from typing import List
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


class Solution:
    mapping = [
        "0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    ]

    def letterCombinations(self, digits: str) -> List[str]:
        # digits = list(digits)
        # print(digits)
        # ans = [""]*(3**len(digits))
        # print(ans)
        # for i,dig in enumerate(digits):
        #     combinations = 3 ** (len(digits)-i)
        #     asciiCode = (int(dig)-2)*3 + ord('a')
        #     letters = [chr(num) for num in range(asciiCode, asciiCode + 3)]
        #     print(letters)
        #     print(combinations)
        #     for j,l in enumerate(letters):
        #         startingPoint = j*(combinations//3)
        #         for pos in range(startingPoint, startingPoint+3**i,3**i):
        #             print(l,str(pos))
        #             ans[pos] += l
        #     print(ans)
        #     print()
        #     for pos in range(i*)
        if not digits:
            return []

        ans = []
        mapping = self.mapping

        def util(curStr, depth):
            nonlocal mapping
            nonlocal ans
            nonlocal digits
            if len(curStr) == len(digits):
                ans.append(curStr)
                return
            currentNumber = int(digits[depth])

            for c in mapping[currentNumber]:
                util(curStr + c, depth + 1)

        util("", 0)
        return ans

    def test(self):
        assert self.letterCombinations("") == []
        assert self.letterCombinations("23") == [
            "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"
        ]
        assert self.letterCombinations("23456") == [
            "adgjm", "adgjn", "adgjo", "adgkm", "adgkn", "adgko", "adglm",
            "adgln", "adglo", "adhjm", "adhjn", "adhjo", "adhkm", "adhkn",
            "adhko", "adhlm", "adhln", "adhlo", "adijm", "adijn", "adijo",
            "adikm", "adikn", "adiko", "adilm", "adiln", "adilo", "aegjm",
            "aegjn", "aegjo", "aegkm", "aegkn", "aegko", "aeglm", "aegln",
            "aeglo", "aehjm", "aehjn", "aehjo", "aehkm", "aehkn", "aehko",
            "aehlm", "aehln", "aehlo", "aeijm", "aeijn", "aeijo", "aeikm",
            "aeikn", "aeiko", "aeilm", "aeiln", "aeilo", "afgjm", "afgjn",
            "afgjo", "afgkm", "afgkn", "afgko", "afglm", "afgln", "afglo",
            "afhjm", "afhjn", "afhjo", "afhkm", "afhkn", "afhko", "afhlm",
            "afhln", "afhlo", "afijm", "afijn", "afijo", "afikm", "afikn",
            "afiko", "afilm", "afiln", "afilo", "bdgjm", "bdgjn", "bdgjo",
            "bdgkm", "bdgkn", "bdgko", "bdglm", "bdgln", "bdglo", "bdhjm",
            "bdhjn", "bdhjo", "bdhkm", "bdhkn", "bdhko", "bdhlm", "bdhln",
            "bdhlo", "bdijm", "bdijn", "bdijo", "bdikm", "bdikn", "bdiko",
            "bdilm", "bdiln", "bdilo", "begjm", "begjn", "begjo", "begkm",
            "begkn", "begko", "beglm", "begln", "beglo", "behjm", "behjn",
            "behjo", "behkm", "behkn", "behko", "behlm", "behln", "behlo",
            "beijm", "beijn", "beijo", "beikm", "beikn", "beiko", "beilm",
            "beiln", "beilo", "bfgjm", "bfgjn", "bfgjo", "bfgkm", "bfgkn",
            "bfgko", "bfglm", "bfgln", "bfglo", "bfhjm", "bfhjn", "bfhjo",
            "bfhkm", "bfhkn", "bfhko", "bfhlm", "bfhln", "bfhlo", "bfijm",
            "bfijn", "bfijo", "bfikm", "bfikn", "bfiko", "bfilm", "bfiln",
            "bfilo", "cdgjm", "cdgjn", "cdgjo", "cdgkm", "cdgkn", "cdgko",
            "cdglm", "cdgln", "cdglo", "cdhjm", "cdhjn", "cdhjo", "cdhkm",
            "cdhkn", "cdhko", "cdhlm", "cdhln", "cdhlo", "cdijm", "cdijn",
            "cdijo", "cdikm", "cdikn", "cdiko", "cdilm", "cdiln", "cdilo",
            "cegjm", "cegjn", "cegjo", "cegkm", "cegkn", "cegko", "ceglm",
            "cegln", "ceglo", "cehjm", "cehjn", "cehjo", "cehkm", "cehkn",
            "cehko", "cehlm", "cehln", "cehlo", "ceijm", "ceijn", "ceijo",
            "ceikm", "ceikn", "ceiko", "ceilm", "ceiln", "ceilo", "cfgjm",
            "cfgjn", "cfgjo", "cfgkm", "cfgkn", "cfgko", "cfglm", "cfgln",
            "cfglo", "cfhjm", "cfhjn", "cfhjo", "cfhkm", "cfhkn", "cfhko",
            "cfhlm", "cfhln", "cfhlo", "cfijm", "cfijn", "cfijo", "cfikm",
            "cfikn", "cfiko", "cfilm", "cfiln", "cfilo"
        ]


if __name__ == "__main__":
    sol = Solution()
    sol.test()