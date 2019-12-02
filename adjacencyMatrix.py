import numpy as np

exampleGraph = [
    [[0],[1],[0],[0],[1]],
    [[1],[0],[1],[1],[1]],
    [[0],[1],[0],[1],[0]],
    [[0],[1],[1],[0],[1]],
    [[1],[1],[0],[1],[0]]
]

class AdjacencyMatrix:
    def __init__(self, size):
        self.matrix = np.zeros((size, size))
    
    def addEdge(self, vertice1, vertice2):
        self.matrix[vertice1][vertice2] = 1
        self.matrix[vertice2][vertice1] = 1
        
    def show(self):
        print(self.matrix)
    
graph = AdjacencyMatrix(5)
graph.addEdge(0,1)
graph.addEdge(0,4)
graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(1,4)
graph.addEdge(2,3)
graph.addEdge(3,4)


graph.show()
print(exampleGraph)