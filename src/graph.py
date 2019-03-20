from typing import List, Tuple


class Graph:
    """A class to make basic operations with non-directed graphs"""
    
    def __init__(self, number_of_vertices: int):
        """Initializes a graph with number of vertices >= 0
        It has a list of vertices and a list of edges"""
        self.__verify_vertice_number(number_of_vertices)
        self.vertices: List[int] = list(range(number_of_vertices))
        self.edges: List[Tuple[int, int]] = []

    def number_of_vertices(self) -> int:
        """Return number of vertices"""
        return len(self.vertices)

    def number_of_edges(self) -> int:
        """Return number of edges"""
        return len(self.edges)

    def add_edge(self, v: int, w: int) -> None:
        """Adds an edge between vertice v and vertice w"""
        self.__verify_vertice_exists([v, w])
        self.edges.append((v, w))

    def neighbourhood(self, vertice: int) -> List:
        """Returns a list with the vertices that have an edge with the input
        vertice"""
        self.__verify_vertice_exists([vertice])

        connected_vertices: list = []
        for edge in self.edges:
            if vertice in edge:
                vertice_index: int = edge.index(vertice)
                other_vertice_index: int = abs(vertice_index - 1)
                connected_vertices.append(edge[other_vertice_index])

        # getting just unique values
        return list(set(connected_vertices))

    def __str__(self) -> str:
        return "Vertices: {0}\n" \
               "Edges: {1}".format(self.vertices, self.edges)

    @staticmethod
    def __verify_vertice_number(number: int) -> None:
        """Raise an exception if vertice number is negative"""
        if type(number) != int or number < 0:
            raise ValueError("Vertice number should be a positive integer")

    def __verify_vertice_exists(self, vertices: list) -> None:
        """Raise an exception if vertice is not encountered"""
        for vertice in vertices:
            if vertice not in self.vertices:
                raise ValueError("Vertice does not existe on this graph")
