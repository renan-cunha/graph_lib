from typing import List, Tuple
from src.graph import Graph
import copy


class GraphMatrix(Graph):

    """A class that represents graphs with matrix"""

    def __init__(self, number_of_vertices: int, digraph: bool = False):
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
        self.digraph = digraph

        list_zeros = [0]*number_of_vertices

        for i in range(number_of_vertices):
            self.__graph.append(list_zeros.copy())

    def get_matrix(self) -> List[List[int]]:
        return self.__graph.copy()

    def __number_of_edges_non_digraph(self) -> int:
        count = 0
        for row in range(self.number_of_vertices()):
            for col in range(row, self.number_of_vertices()):
                count += self.__graph[row][col]
        return count

    def __number_of_edges_digraph(self) -> int:
        count = 0
        for row in range(self.number_of_vertices()):
            count += sum(self.__graph[row])
        return count

    def number_of_edges(self) -> int:
        """Returns number of edges"""
        if self.digraph:
            return self.__number_of_edges_digraph()
        else:
            return self.__number_of_edges_non_digraph()

    def __add_edge_non_digraph(self, v: int, w: int) -> None:
        self.__graph[v][w] = 1
        self.__graph[w][v] = 1

    def __add_edge_digraph(self, v: int, w: int) -> None:
        self.__graph[v][w] = 1

    def add_edge(self, v: int, w: int) -> None:
        """Adds an edge between vertices v and w"""
        self._assert_vertices_exists([v, w])
        if self.digraph:
            self.__add_edge_digraph(v, w)
        else:
            self.__add_edge_non_digraph(v, w)

    def __assert_digraph(self) -> None:
        if not self.digraph:
            raise ValueError("This is graph is not directed")

    def __assert_not_digraph(self) -> None:
        if self.digraph:
            raise ValueError("This is graph is directed")

    def neighbourhood(self, v: int) -> List[int]:
        """Returns a list with the vertices that have an edge with the vertice
        v"""
        self._assert_vertices_exists([v])
        self.__assert_not_digraph()

        result = set()
        for w in range(self.number_of_vertices()):
            if self.__graph[v][w] == 1:
                result.add(w)
        return list(result)

    def transpose(self) -> "GraphMatrix":
        graph = copy.copy(self)
        matrix = graph.__graph
        matrix_transposed = list(map(list, zip(*matrix)))
        graph.__graph = matrix_transposed
        return graph

    @staticmethod
    def __assert_mode_in_out(mode: str) -> None:
        if mode != "in" and mode != "out":
            raise ValueError(f"mode {mode} is not 'in' or 'out'")

    def __neighbourhood(self, v: int, mode: str) -> List[int]:
        self._assert_vertices_exists([v])
        GraphMatrix.__assert_mode_in_out(mode)

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

        return list(result)

    def out_neighbourhood(self, v: int) -> List[int]:
        self.__assert_digraph()
        return self.__neighbourhood(v, "out")

    def in_neighbourhood(self, v: int) -> List[int]:
        self.__assert_digraph()
        return self.__neighbourhood(v, "in")

    def degree(self, vertice: int) -> int:
        """Returns the sum of all edges"""
        self._assert_vertices_exists([vertice])
        self.__assert_not_digraph()
        result = sum(self.__graph[vertice])
        if self.__graph[vertice][vertice] == 1:
            result += 1
        return result

    def out_degree(self, vertice: int) -> int:
        self._assert_vertices_exists([vertice])
        self.__assert_digraph()
        return sum(self.__graph[vertice])

    def in_degree(self, vertice: int) -> int:
        self.__assert_digraph()
        self._assert_vertices_exists([vertice])
        result = 0
        for v in self.get_vertices():
            result += self.__graph[v][vertice]

        return result

    def __max_degree(self, mode: str) -> Tuple[int, int]:
        """Returns a tuple with the vertice with maximum degree and it's
        degree"""
        if mode != "in" and mode != "out" and mode != "non":
            raise ValueError(f"Mode should be in, out or non. Is {mode} "
                             f"instead")

        num_vertices = self.number_of_vertices()
        degrees = []
        for vertice in range(num_vertices):
            if mode == "non":
                degrees.append((vertice, self.degree(vertice)))
            elif mode == "in":
                degrees.append((vertice, self.in_degree(vertice)))
            elif mode == "out":
                degrees.append((vertice, self.out_degree(vertice)))
        return max(degrees, key=lambda x: x[1])

    def max_degree(self) -> Tuple[int, int]:
        self.__assert_not_digraph()
        return self.__max_degree("non")

    def max_in_degree(self) -> Tuple[int, int]:
        self.__assert_digraph()
        return self.__max_degree("in")

    def max_out_degree(self) -> Tuple[int, int]:
        self.__assert_digraph()
        return self.__max_degree("out")

    def number_of_loops_graph(self) -> int:
        """Returns the number of loops on the graph"""

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

    def __repr__(self) -> str:
        return self.__str__()


