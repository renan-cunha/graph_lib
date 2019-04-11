from typing import List, Tuple
from src.graph import Graph


class GraphMatrix(Graph):

    """A class that represents graphs with matrix"""

    def __init__(self, number_of_vertices: int):
        """
        Initializes a graph with number of vertices >= 0

        The graph is represented with matrix
        Each column and line represents an vertice


        An example is:
            V 0 1 2
            0 1 0 0
            1 0 0 1
            2 0 1 0

        The vertice 0 has a loop
        The vertice 1 and 2 have an edge
        """
        super().__init__(number_of_vertices)
        self.__graph: List[List[int]] = []

        list_zeros = [0]*number_of_vertices

        for i in range(number_of_vertices):
            self.__graph.append(list_zeros.copy())

    def number_of_edges(self) -> int:
        """Returns number of edges"""
        count = 0
        for row in range(self.number_of_vertices()):
            for col in range(row, self.number_of_vertices()):
                count += self.__graph[row][col]
        return count

    def add_edge(self, v: int, w: int) -> None:
        """Adds an edge between vertices v and w"""
        self._assert_vertices_exists([v, w])
        self.__graph[v][w] = 1
        self.__graph[w][v] = 1

    def neighbourhood(self, v: int) -> List:
        """Returns a list with the vertices that have an edge with the vertice
        v"""
        self._assert_vertices_exists([v])

        result = set()
        for w in range(self.number_of_vertices()):
            if self.__graph[v][w] == 1:
                result.add(w)
        return list(result)

    def degree(self, vertice: int) -> int:
        """Returns the sum of all edges"""
        self._assert_vertices_exists([vertice])
        result = sum(self.__graph[vertice])
        if self.__graph[vertice][vertice] == 1:
            result += 1
        return result

    def max_degree(self) -> Tuple[int, int]:
        """Returns a tuple with the vertice with maximum degree and it's
        degree"""
        num_vertices = self.number_of_vertices()
        degrees = []
        for vertice in range(num_vertices):
            degrees.append((vertice, self.degree(vertice)))
        return max(degrees, key=lambda x: x[0])

    def number_of_loops_graph(self) -> int:

        count = 0
        for index in range(self.number_of_vertices()):
            count += self.__graph[index][index]
        return count

    def __str__(self) -> str:
        result = "\nV   "
        for i in range(self.number_of_vertices()):
            result += f"{i}  "
        result += "\n"

        for vertice in range(self.number_of_vertices()):
            result += f"{vertice}  {self.__graph[vertice]}\n"

        return result