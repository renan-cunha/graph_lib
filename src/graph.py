from typing import List, Tuple
from abc import ABC, abstractmethod


class Graph(ABC):
    """Abstract Class of graphs"""

    def __init__(self, number_of_vertices: int):
        self.__assert_positive_vertice(number_of_vertices)
        self.__number_of_vertices = number_of_vertices

    def number_of_vertices(self) -> int:
        """Returns number of vertices in int"""
        return self.__number_of_vertices

    def _assert_vertices_exists(self, vertices: List[int]) -> None:
        """Raises and exception if vertice does not exist on graph"""
        for v in vertices:
            self.__assert_positive_vertice(v)
            if v >= self.number_of_vertices():
                raise ValueError(f"Vertice {v} does not exist on this graph")

    def get_vertices(self) -> List[int]:
        """Returns a list with vertices"""
        return list(range(self.number_of_vertices()))

    @abstractmethod
    def number_of_edges(self) -> int:
        """Returns number of edges in int"""
        pass

    @abstractmethod
    def add_edge(self, v: int, w: int) -> None:
        """Adds an edge between vertices v and w"""
        pass

    @abstractmethod
    def neighbourhood(self, v: int) -> List:
        """Returns a set with the vertices that have an edge with the vertice
        v"""
        pass

    @abstractmethod
    def degree(self, v: int) -> int:
        """Returns an int with the sum of all edges of a vertice"""
        pass

    @abstractmethod
    def max_degree(self) -> Tuple[int, int]:
        """Returns a tuple with the vertice with maximum degree and it's
        degree"""
        pass

    @abstractmethod
    def number_of_loops_graph(self) -> int:
        """Returns an int with the number of loops on the graph"""
        pass

    def is_connected(self) -> bool:
        """Returns a boolean variable saying if the graph is conex"""
        vertice_index = 0
        marked_vertices = [0]

        while vertice_index < len(marked_vertices):
            vertice = marked_vertices[vertice_index]
            connected_vertices = self.neighbourhood(vertice)
            for v in connected_vertices:
                if v not in marked_vertices:
                    marked_vertices.append(v)

            if self.get_vertices() == sorted(marked_vertices):
                return True
            else:
                vertice_index += 1
        return False

    def is_euler_graph(self) -> bool:
        """Returns a boolean variable saying if it's an euler graph"""
        if not self.is_connected() or self.number_of_vertices() < 2:
            return False
        for vertice in self.get_vertices():
            if self.degree(vertice) % 2 == 1:
                return False
        return True

    def has_open_euler_path(self) -> bool:
        """Returns a boolean variable saying it the graph has an open euler
        path"""
        if not self.is_connected() or self.number_of_vertices() < 2:
            return False
        count = 0
        for vertice in self.get_vertices():
            count += self.degree(vertice) % 2
        if count == 2:
            return True
        else:
            return False

    @abstractmethod
    def __str__(self) -> str:
        """Returns the string representation of the graph"""
        pass

    @staticmethod
    def __assert_positive_vertice(number: int) -> None:
        """Raise an exception if vertice number is negative"""
        if type(number) != int or number < 0:
            raise ValueError(f"Vertice number {number} is not a positive "
                             f"integer")
