from typing import List
"""
There are 2N people a company is planning to interview. 
The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
Constraints:
1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""

def twoCitySchedCost(costs: List[List[int]]) -> int:
    arr = []
    minCost = 0
    for costToA,costToB in costs:
        minCost += costToA
        arr.append(costToB-costToA)

    arr = sorted(arr)

    for i in range(len(arr)//2):
        minCost += arr[i]
        
    return minCost

if __name__ == "__main__":
    assert twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]) == 110