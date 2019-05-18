from abc import ABC, abstractmethod
from typing import List, Tuple, Set, Callable


class AbstractDigraph(ABC):
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
        """Returns number of edges"""
        pass

    @abstractmethod
    def add_edge(self, v: int, w: int) -> None:
        """Adds an edge that goes from vertice v to w"""
        pass

    @abstractmethod
    def out_neighbourhood(self, v: int) -> Set[int]:
        """Returns the vertices that v has an edge to"""
        pass

    @abstractmethod
    def in_neighbourhood(self, v: int) -> Set[int]:
        """Returns the vertices that have and edge to v"""
        pass

    @abstractmethod
    def out_degree(self, v: int) -> int:
        """Returns the sum of edges that get out from v"""
        pass

    @abstractmethod
    def in_degree(self, v: int) -> int:
        """Returns the sum of edges that go to v"""
        pass

    def __max_degre(self, mode: str) -> Tuple[int, int]:
        degrees = []
        for vertice in self.get_vertices():
            if mode == "in":
                current_degrees = self.in_degree(vertice)
            elif mode == "out":
                current_degrees = self.out_degree(vertice)
            else:
                raise Exception(f"the mode {mode} is not acceptable, use"
                                f"'in' or 'out")
            degrees.append(current_degrees)
        maximum_degree = max(degrees)
        return degrees.index(maximum_degree), maximum_degree

    def max_out_degree(self) -> Tuple[int, int]:
        """Returns a tuple with the vertice with maximum degree and it's
        degree"""
        return self.__max_degre("out")

    def max_in_degree(self) -> Tuple[int, int]:
        """Returns a tuple with the vertice with maximum degree and it's
        degree"""
        return self.__max_degre("in")

    @abstractmethod
    def number_of_loops_vertice(self, vertice: int) -> int:
        pass

    def number_of_loops_graph(self) -> int:
        count = 0
        for vertice in self.get_vertices():
            count += self.number_of_loops_vertice(vertice)

        return count

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
