from src.graph_matrix import GraphMatrix
from typing import List


class ConnectedComponents:
    """Returns the number of conex components of a graph"""

    def __init__(self, graph: GraphMatrix, list_vertices: List[int] = None):
        num_vertices: int = graph.number_of_vertices()
        self.marked: List[bool] = [False]*num_vertices
        self.id: List = [None]*num_vertices
        self.count: int = 0

        if not list_vertices:
            list_vertices = graph.get_vertices()
        for vertice in list_vertices:
            if not self.marked[vertice]:
                self.__dfs(graph, vertice)
                self.count += 1

    def __dfs(self, graph: GraphMatrix, start_vertice: int) -> None:
        self.marked[start_vertice] = True
        self.id[start_vertice] = self.count
        for adjacent_vertice in graph.out_neighbourhood(start_vertice):
            if not self.marked[adjacent_vertice]:
                self.__dfs(graph, adjacent_vertice)

    def get_count(self) -> int:
        return self.count


