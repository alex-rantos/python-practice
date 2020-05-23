"""Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists."""

def intervalIntersection(A: [[int]], B: [[int]]) -> [[int]]:
    a, b = 0, 0
    n1, n2 = len(A), len(B)
    ans = []
    while a<n1 and b<n2:
        start = max(A[a][0], B[b][0])
        end = min(A[a][1], B[b][1])
        if (start <= end):
            ans.append([start,end])
        if A[a][1] > B[b][1]:
            b+=1
        else:
            a+=1
    return ans

if __name__ == "__main__":
    assert intervalIntersection(A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]