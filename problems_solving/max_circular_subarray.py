class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        ans, ans2 = float("-inf"), float("-inf")
        s,minElem = float("-inf"), 0
        start, temp, end = 0, 0, 0
        for i,x in enumerate(A):
            minElem = min(x,minElem)
            s += x
            if (s<x):
                s = x
                start = i
            if (s>=ans):
                ans = s
                end = i
        print(start,end,ans)
        if (end==len(A)-1):
            if (start == 0 and start is not end): return ans - minElem
            for i in range(0,start):
                s += A[i]
                if (s<A[i]):
                    s = A[i]
                if (s>ans):
                    ans = s
        elif (start == 0):
            s = ans
            for i in range(len(A) - 1,end, -1):
                print(A[i],i)
                s += A[i]
                if (s<A[i]):
                    s = A[i]
                if (s>ans):
                    ans = s
        return ans
        
class SolutionOptimal:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        k = self.kadane(A)
        c = 0
        for i in range(len(A)):
            c += A[i]
            A[i] =- A[i]
        c += self.kadane(A)
        if c > k and c != 0:
            return c
        else:
            return k
        
    def kadane(self,a): 
        n = len(a) 
        max_so_far = a[0]
        max_ending_here = a[0]
        for i in range(1, n): 
            max_so_far = max(max_so_far+a[i], a[i])
            max_ending_here = max(max_ending_here,max_so_far)
        return max_ending_here 
                                