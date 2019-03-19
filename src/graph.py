from typing import List


class Graph:

    def __init__(self, number_of_vertices: int):
        """A class to make basic operations with non-directed graphs"""
        self.verify_vertice_number(number_of_vertices)
        self.__vertices: List[int] = list(range(number_of_vertices))
        self.__edges: List = []

    def number_of_vertices(self) -> int:
        """Return number of vertices"""
        return len(self.__vertices)

    def number_of_edges(self) -> int:
        """Return number of edges"""
        return len(self.__edges)

    def add_edge(self, v: int, w: int) -> None:
        """Adds an edge between vertice v and vertice w"""
        self.verify_vertice_exists([v, w])
        self.__edges.append((v, w))

    def neighbourhood(self, vertice: int) -> List:
        """Returns a list with the vertices that have an edge with the input
        vertice"""
        self.verify_vertice_exists([vertice])

        connected_vertices: list = []
        for edge in self.__edges:
            if vertice in edge:
                vertice_index: int = edge.index(vertice)
                other_vertice_index: int = abs(vertice_index - 1)
                connected_vertices.append(edge[other_vertice_index])

        # getting just unique values
        return list(set(connected_vertices))

    def __str__(self) -> str:
        return "Vertices: {0}\n" \
               "Edges: {1}".format(self.__vertices, self.__edges)

    @staticmethod
    def verify_vertice_number(number: int) -> None:
        """Raise an exception if vertice number is negative"""
        if type(number) != int or number < 0:
            raise ValueError("Vertice number should be a positive integer")

    def verify_vertice_exists(self, vertices: list) -> None:
        """Raise an exception if vertice is not encountered"""
        for vertice in vertices:
            if vertice not in self.__vertices:
                raise ValueError("Vertice does not existe on this graph")
