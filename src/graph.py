from typing import List, Dict, Tuple, Set
from abc import ABC, abstractmethod


class Graph(ABC):
    """Abstract Class of graphs"""

    def __init__(self, number_of_vertices: int):
        self.__assert_positive_vertice(number_of_vertices)
        self.__number_of_vertices = number_of_vertices

    def number_of_vertices(self) -> int:
        """Returns number of vertices in int"""
        return self.__number_of_vertices

    @abstractmethod
    def number_of_edges(self) -> int:
        """Returns number of edges in int"""
        pass

    @abstractmethod
    def add_edge(self, v: int, w: int) -> None:
        """Adds an edge between vertices v and w"""
        pass

    @abstractmethod
    def neighbourhood(self, v: int) -> Set:
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
    def number_of_loops_vertice(self, vertice: int) -> int:
        """Returns an int with the number of loops on a vertice"""
        pass

    @abstractmethod
    def number_of_loops_graph(self) -> int:
        """Returns an int with the number of loops on the graph"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Returns the string representation of the graph"""
        pass

    @staticmethod
    def __assert_positive_vertice(number: int) -> None:
        """Raise an exception if vertice number is negative"""
        if type(number) != int or number < 0:
            raise ValueError("Vertice number should be a positive integer")


class GraphAdjacencyList(Graph):
    """A class that represent a graph with adjacency list"""
    
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
        super().__init__(number_of_vertices)

        self.__graph: Dict[int: List[int]] = {}

        for i in range(number_of_vertices):
            self.__graph[i] = []

    def number_of_edges(self) -> int:
        """Returns number of edges in int"""
        count = 0
        for vertice in self.__graph:
            count += len(self.__graph[vertice])
        return count // 2

    def add_edge(self, v: int, w: int) -> None:
        """Adds an edge between vertices v and w"""
        self.__graph[v].append(w)
        self.__graph[w].append(v)

    def neighbourhood(self, v: int) -> Set:
        """Returns a set with the vertices that have an edge with the vertice
        v"""
        return set(self.__graph[v])

    def degree(self, v: int) -> int:
        """Returns the sum of all edges of a vertice"""
        return len(self.__graph[v])

    def max_degree(self) -> Tuple[int, int]:
        """Returns a tuple with the vertice with maximum degree and it's
        degree"""
        degrees = [self.degree(vertice) for vertice in self.__graph]
        maximum_degree = max(degrees)
        return degrees.index(maximum_degree), maximum_degree

    def number_of_loops_vertice(self, vertice: int) -> int:
        """Returns the number of loops on a vertice"""

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


class GraphMatrix(Graph):
    """A class that represents graphs with matrix"""

    def __init__(self, number_of_vertices: int):
        """
        Initializes a graph with number of vertices >= 0

        The graph is represented with matrix
        Each column and line represents an vertice


        An example is:
            - 0 1 2
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
            self.__graph.append(list_zeros)

    def number_of_edges(self) -> int:
        """Returns number of edges"""
        count = 0
        for row in range(self.number_of_vertices()):
            for col in range(row, self.number_of_vertices()):
                count += self.__graph[row][col]
        return count

    def add_edge(self, v: int, w: int) -> None:
        """Adds an edge between vertices v and w"""
        self.__graph[v][w] = 1
        self.__graph[w][v] = 1

    def neighbourhood(self, v: int) -> Set:
        """Returns a list with the vertices that have an edge with the vertice
        v"""
        result = set()
        for w in range(self.number_of_vertices()):
            if self.__graph[v][w] == 1:
                result.add(w)
        return result

    def degree(self, vertice: int) -> int:
        """Returns the sum of all edges"""
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

    # TODO
    def __str__(self) -> str:
        result = "\nVertices: Edges\n"
        for vertice in self.__graph:
            result += f"{vertice}: {self.__graph[vertice]}\n"
        return result



