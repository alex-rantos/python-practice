"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool self.is_bad_version(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call self.is_bad_version(3) -> false
call self.is_bad_version(5) -> true
call self.is_bad_version(4) -> true

Then 4 is the first bad version. 
# The self.is_bad_version API is already defined for you.
# @param version, an integer
# @return a bool
# def is_bad_version(version):
2126753390
1702766719
"""
class Game(object):
    def __init__(self, first_bad_version):
        self.version = first_bad_version
    
    def set_version(self, first_bad_version):
        self.version = first_bad_version

    def is_bad_version(self,version_to_check):
        if version_to_check >= self.version:
            return True
        return False

    def first_bad_version(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0 : return None
        if self.is_bad_version(1) == True: return 1
        if self.is_bad_version(n) == True and not self.is_bad_version(n-1): return n
        
        low, high = 2, n - 1
        
        while low < high:
            median = low + (high - low)//2
            if self.is_bad_version(median):
                high = median
            else:
                low = median + 1
            print(low, high)
        return low

if __name__ == "__main__":
    obj = Game(100000)
    assert obj.first_bad_version(2000000) == 100000