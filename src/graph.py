from typing import List, Tuple, Set
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

    def vertices_with_edges(self) -> List[int]:
        """Returns a list with the vertices with degree > 0"""
        result = []
        vertices = self.get_vertices()
        for vertice in vertices:
            if self.degree(vertice) > 0:
                result.append(vertice)
        return result

    def has_path(self, begin:int , end:int) -> bool:
        """Returns a boolean variable saying if a path between the two
        vertices, begin and ends exist"""
        self._assert_vertices_exists([begin, end])

        connected_vertices = self.neighbourhood(begin)
        for vertice in connected_vertices:
            if vertice == end:
                return True
            new_connected_vertices = self.neighbourhood(vertice)
            for new_vertice in new_connected_vertices:
                if new_vertice not in connected_vertices:
                    connected_vertices.append(new_vertice)
        return False
        
    def has_acessible_edges(self) -> bool:
        """Returns a boolean variable saying if all the edges are 
        accessible from any vertice"""
        vertices_with_positive_degree = self.vertices_with_edges()
        
        if len(vertices_with_positive_degree) == 0:
            return True

        begin = vertices_with_positive_degree.pop()
        for vertice in vertices_with_positive_degree:
            if not self.has_path(begin, vertice):
                return False
        return True

    def is_euler_graph(self) -> bool:
        """Returns a boolean variable saying if it's an euler graph"""
        if not self.has_acessible_edges():
            return False
        for vertice in self.get_vertices():
            if self.degree(vertice) % 2 == 1:
                return False
        return True

    def has_open_euler_path(self) -> bool:
        """Returns a boolean variable saying it the graph has an open euler
        path"""
        if not self.has_acessible_edges():
            return False
        count = 0
        for vertice in self.get_vertices():
            count += self.degree(vertice) % 2
        if count == 2:
            return True
        else:
            return False

    def dfs(self, start_vertice=0,
            visited_vertices=None) -> Set:
        """Returns the edges of the depth-first search algorithm"""
        if not visited_vertices:
            visited_vertices = set()
        visited_vertices.add(start_vertice)
        connected_vertices = self.neighbourhood(start_vertice)
        for vertice in connected_vertices:

            if vertice not in visited_vertices:
                print(start_vertice)
                visited_vertices.add(vertice)
                visited_vertices.union(self.dfs(start_vertice=vertice,
                                                visited_vertices=visited_vertices))
                print(vertice)
        return visited_vertices

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
