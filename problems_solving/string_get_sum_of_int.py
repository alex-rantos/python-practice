"""
Write a function that takes a list of strings and 
returns the sum of the list items that represent an integer (skipping the other items)
"""

# functions assumes that list contains ONLY strings
def get_sum_iterative(l:[str])->int:
    _sum = 0
    for s in l:
        if s.isdigit(): _sum += 1
    return _sum

class Solution():
    def __init__(self):
        self._sum = 0
    def get_sum_recursive(self, l:[str])->int:

        def util(l):
            if not l: return 
            if l[0].isdigit():
                util(l[1:])
                self._sum += 1
            else:
                util(l[1:])
        util(l)
        return self._sum

if __name__ == "__main__":
    assert get_sum_iterative(["45","da","d3","tw","5264","513","3e0","002"]) == 4
    sol = Solution()
    assert sol.get_sum_recursive(["45","da","d3","tw","5264","513","3e0","002"]) == 4
