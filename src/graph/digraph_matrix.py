from typing import List, Tuple, Set
from src.graph.abstract_digraph import AbstractDigraph


class DigraphMatrix(AbstractDigraph):

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
            2 0 0 0

        The vertice 0 has a loop
        The vertice 1 has an edge to vertice 2

        This class does not support parallel edges, use DigraphList instead
        """
        super().__init__(number_of_vertices)
        self.__graph: List[List[int]] = []

        list_zeros = [0]*number_of_vertices

        for i in range(number_of_vertices):
            self.__graph.append(list_zeros.copy())

    def __verify_edge_exists(self, v: int, w: int) -> bool:
        return bool(self.__graph[v][w])

    def __raise_exception_if_edge_exists(self, v: int, w: int) -> None:
        if self.__verify_edge_exists(v, w):
            raise ValueError(f"The edge from vertice {v} to vertice {w}"
                             f"exists already, to use parallel edges, switch"
                             f"to the DigraphList class")

    def add_edge(self, v: int, w: int) -> None:
        self._assert_vertices_exists([v, w])
        self.__raise_exception_if_edge_exists(v, w)
        self.__graph[v][w] = 1

    def number_of_edges(self) -> int:
        count = 0
        for row in range(self.number_of_vertices()):
            count += sum(self.__graph[row])
        return count

    def __neighbourhood(self, v: int, mode: str) -> Set[int]:
        self._assert_vertices_exists([v])
        AbstractDigraph._assert_mode_out_in(mode)

        result = set()
        for w in range(self.number_of_vertices()):

            first_index = -1
            last_index = -1
            if mode == "out":
                first_index, last_index = v, w
            elif mode == "in":
                first_index, last_index = w, v

            if self.__graph[first_index][last_index] == 1:
                result.add(w)

        return result

    def out_neighbourhood(self, v: int) -> Set[int]:
        return self.__neighbourhood(v, "out")

    def in_neighbourhood(self, v: int) -> Set[int]:
        return self.__neighbourhood(v, "in")

    def out_degree(self, vertice: int) -> int:
        self._assert_vertices_exists([vertice])
        return sum(self.__graph[vertice])

    def in_degree(self, vertice: int) -> int:
        self._assert_vertices_exists([vertice])
        result = 0
        for v in self.get_vertices():
            result += self.__graph[v][vertice]
        return result

    def number_of_loops_vertice(self, v:int) -> int:
        return self.__graph[v][v]

    def __str__(self) -> str:
        result = "\nV   "
        for i in range(self.number_of_vertices()):
            result += f"{i}  "
        result += "\n"

        for vertice in range(self.number_of_vertices()):
            result += f"{vertice}  {self.__graph[vertice]}\n"

        return result

    def __repr__(self) -> str:
        return self.__str__()
