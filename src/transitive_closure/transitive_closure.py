from src.graph_matrix import GraphMatrix
from typing import List


def warshall(graph: GraphMatrix) -> List[List[int]]:
    matrix = graph.get_matrix()
    size = len(matrix)

    for k in range(size):
        for i in range(size):
            for j in range(size):
                matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
    return matrix