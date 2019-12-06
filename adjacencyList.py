# A practice session to implement an adjacency list graph 
# Inspired by GeeksForGeeks: https://www.geeksforgeeks.org/graph-and-its-representations/

class Node:
        def __init__(self, label):
            self.label = label
            self.nextNode = None
        
        def getLabel(self):
            return self.label
            
        def setNext(self, node):
            self.nextNode = node
            
        def getNext(self):
            return self.nextNode
            
class AdjacencyListGraph:
    
    def __init__(self, size):
        self.vertices = [Node(i) for i in range(size)]
        
    def addEdge(self, vertice1, vertice2):
        self._updatePointers(vertice1, vertice2)
        self._updatePointers(vertice2, vertice1)
        
    def show(self):
        for vertice in self.vertices:
            print(self.vertices.index(vertice), end = "-")
            nextVertice = vertice.getNext()
            while nextVertice:
                print(nextVertice.getLabel(), end = "-")
                nextVertice = nextVertice.getNext()
            print("")
            
    def _updatePointers(self, vertice1, vertice2):
        vertice = self.vertices[vertice1]
        node = Node(vertice2)
        node.setNext(vertice.getNext())
        vertice.setNext(node)
        
graph = AdjacencyListGraph(5)
graph.addEdge(0, 1)
graph.addEdge(0, 4)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 3)
graph.addEdge(3, 4)
graph.show()