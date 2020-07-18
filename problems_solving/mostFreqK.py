from typing import List
from collections import Counter 

"""Given a non-empty array of integers, return the k most frequent elements."""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        if len(counter.keys()) < k:
            return list(counter.keys())
        else:
            res = []
            for k,v in counter.most_common(k):
                res.append(k)
            return res
    
    def test(self):
        assert self.topKFrequent(nums = [1,1,1,2,2,3], k = 2) == [1,2]
        assert self.topKFrequent(nums = [1], k = 1) == [1]
        assert self.topKFrequent(nums = [], k = 36) == []
        assert self.topKFrequent(nums = [1,1,1,2,2,3], k = 4) == [1,2,3]

if __name__ == "__main__":
    sol = Solution()
    sol.test()