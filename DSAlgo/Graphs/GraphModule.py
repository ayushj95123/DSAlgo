from collections import defaultdict


class Graph:
    def __init__(self, nodes, undirected=False):
        self.v = nodes
        self.adjList = defaultdict(list)
        self.undirected = undirected

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        if self.undirected:
            self.adjList[v].append(u)

    def printGraph(self):
        for key, value in self.adjList.items():
            print(key, "=>", value)


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.printGraph()
