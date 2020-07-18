from typing import List
from collections import defaultdict, deque
"""
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
"""


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        order = []

        ind = {}
        for cId in range(numCourses):
            ind[cId] = 0

        adj = defaultdict(set)
        for src, dest in prerequisites:
            adj[dest].add(src)
            ind[src] += 1

        deq = deque([])
        visited = set()

        for k in ind:
            if ind[k] == 0:
                order.append(k)
                deq.append(k)

        while deq:
            courseId = deq.popleft()
            if courseId in visited:
                continue
            else:
                visited.add(courseId)

            for neigh in adj[courseId]:
                if neigh in visited:
                    continue
                ind[neigh] -= 1
                if ind[neigh] == 0:
                    order.append(neigh)
                    if len(order) == numCourses:
                        return order
                    deq.append(neigh)
        return order if len(order) == numCourses else []

    def test(self):
        assert self.findOrder(2, [[1, 0]]) == [0, 1]
        assert self.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]
                                  ]) == [0, 1, 2, 3] or [0, 2, 1, 3]
        assert self.findOrder(3, [[1, 0], [1, 2], [0, 1]]) == []


if __name__ == "__main__":
    sol = Solution()
    sol.test()