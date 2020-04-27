"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""
class Graph(object):
    def __init__(self,grid):
        self.grid = grid
        self.visited = {} # tuples as keys [(i,j)] 
        self.islands = 0

    def check_neighbors(self,i,j,init = False):
        if i < 0 or i > len(self.grid) - 1 or j < 0 or j > len(self.grid[0]) - 1 or (i,j) in self.visited or self.grid[i][j] != 1:
            return 

        if (init != False):
            self.islands += 1

        self.visited[(i,j)] = True

        self.check_neighbors(i-1,j)
        self.check_neighbors(i+1,j)
        self.check_neighbors(i,j-1)
        self.check_neighbors(i,j+1)

def num_islands(grid) -> int:
    graph = Graph(grid)
    for i,x in enumerate(grid):
        for j in range(len(x)):
            if grid[i][j] == 1 and (i,j) not in graph.visited:
                graph.check_neighbors(i,j,True)
    print(graph.visited)
    return graph.islands
        

if __name__ == "__main__":
    grid1 = [
        [1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]
    ]
    r1 = num_islands(grid1)
    assert r1 == 1
    grid2 = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]
    ]
    r2 = num_islands(grid2)
    print(r2)
    assert r2 == 3
