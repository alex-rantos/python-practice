import collections
from typing import List


def canFinish(gitnumCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    indegrees = collections.defaultdict(int)
    for u, v in prerequisites:
        graph[v].append(u)
        indegrees[u] += 1
    for i in range(numCourses):
        zeroDegree = False
        for j in range(numCourses):
            if indegrees[j] == 0:
                zeroDegree = True
                break
        if not zeroDegree:
            return False
        indegrees[j] = -1
        for node in graph[j]:
            indegrees[node] -= 1
    return True


if __name__ == "__main__":
    assert canFinish(numCourses=2, prerequisites=[[1, 0]]) == True
    assert canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]) == False
