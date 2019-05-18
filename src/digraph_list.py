from src.abstract_digraph import AbstractDigraph
from typing import Dict, List, Tuple, Set


class DigraphList(AbstractDigraph):
    """A class that represent a graph with adjacency list"""

    def __init__(self, number_of_vertices: int):
        """
        Initializes a digraph with number of vertices >= 0

        The digraph is represented with dictionaries
        The keys are in int and represent the vertices
        The values are lists with ints representing the connected vertices.

        An example is:
            {1: [2,3], 2: [], 3: [], 4: [4]}

        The vertice 1 has an edge to vertices 2 and 3.
        The vertice 4 has a loop
        """
        super().__init__(number_of_vertices)

        self.__graph: Dict[int, List[int]] = {}

        for i in range(number_of_vertices):
            self.__graph[i] = []

    def number_of_edges(self) -> int:
        count = 0
        for vertice in self.__graph:
            count += len(self.__graph[vertice])
        return count

    def add_edge(self, v: int, w: int) -> None:
        self._assert_vertices_exists([v, w])
        self.__graph[v].append(w)

    def out_neighbourhood(self, v: int) -> Set[int]:
        self._assert_vertices_exists([v])
        return set(self.__graph[v])

    def in_neighbourhood(self, v: int) -> Set[int]:
        self._assert_vertices_exists([v])
        result: Set[int] = set()
        for vertice in self.get_vertices():
            if v in self.out_neighbourhood(vertice):
                result.add(vertice)
        return result

    def out_degree(self, v: int) -> int:
        self._assert_vertices_exists([v])
        return len(self.__graph[v])

    def in_degree(self, v: int) -> int:
        self._assert_vertices_exists([v])
        return len(self.__graph[v])


    def max_in_degree(self) -> Tuple[int, int]:
        """Returns a tuple with the vertice with maximum degree and it's
        degree"""
        degrees = [self.degree(vertice) for vertice in self.__graph]
        maximum_degree = max(degrees)
        return degrees.index(maximum_degree), maximum_degree

    def max_out_degree(self) -> Tuple[int, int]:
        """Returns a tuple with the vertice with maximum degree and it's
        degree"""
        pass

    def number_of_loops_vertice(self, vertice: int) -> int:
        """Returns the number of loops on a vertice"""
        self._assert_vertices_exists([vertice])

        count = 0
        for connected_vertice in self.__graph[vertice]:
            if connected_vertice == vertice:
                count += 1

        return count // 2

    def number_of_loops_graph(self) -> int:
        """Returns the number of loops on the graph"""

        count = 0
        for vertice in self.__graph:
            count += self.number_of_loops_vertice(vertice)

        return count

    def __str__(self) -> str:
        result = "\nVertices: Edges\n"
        for vertice in self.__graph:
            result += f"{vertice}: {self.__graph[vertice]}\n"
        return result

    def __repr__(self) -> str:
        return self.__str__()
