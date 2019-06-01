from src.graph_matrix import GraphMatrix
from typing import List


class Warshall:
    def __init__(self, graph: GraphMatrix):
        self.graph = graph

    def run(self) -> List[List[int]]:
        matrix = self.graph.get_matrix()
        size = len(matrix)

        for k in range(size):
            for i in range(size):
                for j in range(size):
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
        return matrix

    def __str__(self) -> str:
        matrix = self.run()
        result = "Transitive Closure (Warshall):\n" \
                 "V   "
        for i in range(len(matrix)):
            result += f"{i}  "
        result += "\n"

        for vertice in range(len(matrix)):
            result += f"{vertice}  {matrix[vertice]}\n"

        return result