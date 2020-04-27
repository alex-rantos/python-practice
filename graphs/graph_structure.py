class MyGraph:
    """
    An undirected weighted graph structure that saves all the nodes in the dictionary 'self.nodes' and
    the edges in an array of dictionaries (adjacency list).
    Each key of the 'self.nodes' dict represents the id of the node and the value is the position of that node to the array 'self.edges'.
    Accordingly, each key of the 'self.edges[i]' represents the id of the neighbor node and the value is the weight of that edge.
    The form of each edge is 'edges[src][dest] = weight'.
    """
    nodes = {}
    edges = []
    
    """ Initialize the graph from a list of nodes' ids """
    def __init__(self, nodes_array):
        self.nodes = {key:count for count, key in enumerate(nodes_array)}
        self.edges = [dict() for i in range(len(nodes_array))]
    
    """ Add an undirected edge from src to dest and updates the edge's weight """
    def addDoubleEdge(self, src, dest):
        src_pos = self.nodes[src]
        dest_pos = self.nodes[dest]
        "Add the edge from src -> dest"
        if dest not in self.edges[src_pos]:
            print("Created edge from {}:{} -> {}:{}".format(src,src_pos,dest,dest_pos))
            self.edges[src_pos][dest] = 1
        else:
            self.edges[src_pos][dest] += 1
            print("Inc weight from {}:{} -> {}:{}".format(src,src_pos,dest,dest_pos))
            
        "Add the edge from dest -> src"
        if src not in self.edges[dest_pos]:
            print("Created edge from {}:{} -> {}:{}".format(dest,dest_pos,src,src_pos))
            self.edges[dest_pos][src] = 1
        else:
            self.edges[dest_pos][src] += 1
            print("Inc weight from {}:{} -> {}:{}".format(dest,dest_pos,src,src_pos))
    
    def printNodes(self):
        print("The nodes' id dictionary [id]:pos_to_self.edges")
        print(self.nodes)
        
    def printEdges(self):
        for i in self.nodes:
            for e in self.edges[self.nodes[i]]:
                print("{} has edge to {} with weight {}".
                      format(i,e,self.edges[self.nodes[i]][e]))
            
if __name__ == '__main__':
    graph = MyGraph([2,1,3,4,20,50,5])
    
    graph.addDoubleEdge(1,2)
    graph.addDoubleEdge(1,2)
    graph.addDoubleEdge(1,2)
    graph.addDoubleEdge(1,2)
    graph.addDoubleEdge(2,3)
    graph.addDoubleEdge(3,5)
    graph.addDoubleEdge(4,5)
    graph.addDoubleEdge(20,50)
    graph.addDoubleEdge(20,50)
    graph.addDoubleEdge(2,50)
    graph.addDoubleEdge(20,5)
    
    graph.printNodes()
    graph.printEdges()
    
    