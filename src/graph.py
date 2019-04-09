from typing import List, Dict, Tuple


class Graph:
    """A class to make basic operations with non-directed graphs"""
    
    def __init__(self, number_of_vertices: int):
        """
        Initializes a graph with number of vertices >= 0

        The graph is represented with dictionaries
        The keys are in int and represent the vertices
        The values are lists with ints representing the connected vertices.

        An example is:
            {1: [2,3], 2: [1], 3: [1], 4: [4]}

        The vertice 1 has a connection with the vertices 2 and 3.
        The vertice 4 has a loop
        """
        self.__assert_positive_vertice(number_of_vertices)
        self.graph: Dict[int: List[int]] = {}

        for i in range(number_of_vertices):
            self.graph[i] = []

        self.__number_of_vertices = number_of_vertices
        self.__number_of_edges = 0

    def number_of_vertices(self) -> int:
        """Returns number of vertices"""
        return self.__number_of_vertices

    def number_of_edges(self) -> int:
        """Returns number of edges"""
        return self.__number_of_edges

    def add_edge(self, v: int, w: int) -> None:
        """Adds an edge between vertices v and w"""
        self.__verify_vertices_exists([v, w])
        self.graph[v].append(w)

        # only adds two edges if not a loop
        if v != w:
            self.graph[w].append(v)

        self.__number_of_edges += 1

    def neighbourhood(self, v: int) -> List:
        """Returns a list with the vertices that have an edge with the vertice
        v"""
        self.__verify_vertices_exists([v])
        return self.graph[v]

    def degree(self, v: int) -> int:
        """Returns the number of edges that a vertice has.
        Remember: Loops count as two edges"""
        self.__verify_vertices_exists([v])
        count = 0
        for connected_vertice in self.neighbourhood(v):
            count += 2 if connected_vertice == v else 1
        return count

    def max_degree(self) -> Tuple[int, int]:
        """Returns a tuple with the vertice with maximum degree and it's
        degree"""

        max_vertice, max_degree = 0, 0

        for vertice in self.graph:
            vertice_degree = self.degree(vertice)

            if vertice_degree > max_degree:
                max_vertice, max_degree = vertice, vertice_degree

        return max_vertice, max_degree

    def number_of_loops_vertice(self, vertice: int) -> int:
        """Returns the number of loops on a vertice"""
        self.__verify_vertices_exists([vertice])

        count = 0
        for connected_vertice in self.neighbourhood(vertice):
            if connected_vertice == vertice:
                count += 1

        return count

    def number_of_loops_graph(self) -> int:
        """Returns the number of loops on the graph"""

        count = 0
        for vertice in self.graph:
            count += self.number_of_loops_vertice(vertice)
        return count

    def __str__(self) -> str:
        result = "\nVertices: Connected Vertices\n"
        for vertice in self.graph:
            result += f"{vertice}: {self.graph[vertice]}\n"
        return result

    def __verify_vertices_exists(self, vertices: list) -> None:
        """Raise an exception if vertice is not encountered"""
        for vertice in vertices:
            if vertice not in self.graph:
                raise ValueError(f"Vertice {vertice} does not exist on this"
                                 f" graph")

    @staticmethod
    def __assert_positive_vertice(number: int) -> None:
        """Raise an exception if vertice number is negative"""
        if type(number) != int or number < 0:
            raise ValueError("Vertice number should be a positive integer")


