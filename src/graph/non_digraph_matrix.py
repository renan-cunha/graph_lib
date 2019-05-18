from typing import List, Tuple, Set
from src.graph.digraph_matrix import DigraphMatrix
from src.graph.abstract_digraph import AbstractDigraph


class NonDigraphMatrix(DigraphMatrix):

    """A class that represents non directed graphs with matrix"""

    def __init__(self, number_of_vertices: int):
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
        The vertice 1 has an edge with vertice 2

        This class does not support parallel edges, use DigraphList instead
        """
        super().__init__(number_of_vertices)

    def add_edge(self, v: int, w: int) -> None:
        """Adds and undirected edge between vertices v and w"""
        super().add_edge(v, w)
        if v != w:
            super(NonDigraphMatrix, self).add_edge(w, v)

    def number_of_edges(self) -> int:
        graph_matrix = super().get_matrix()
        result = 0
        for v in super().get_vertices():
            for j in range(v, super().number_of_vertices()):
                result += graph_matrix[v][j]
        return result

    def neighbourhood(self, v: int) -> Set[int]:
        """Returns the vertices that have and edge with vertice 'v'"""
        in_adj_vertices = super().in_neighbourhood(v)
        out_adj_vertices = super().out_neighbourhood(v)
        return in_adj_vertices.union(out_adj_vertices)

    def degree(self, v: int) -> int:
        """Returns the degree of the vertice i.e. how many connections it
        has, obs: loop count as 2 conections"""
        graph_matrix = super().get_matrix()
        return sum(graph_matrix[v]) + super().number_of_loops_vertice(v)

    def max_degree(self) -> Tuple[int, int]:
        """Returns a tuple, the first element is the vertice with maximum
        degree, the second element is the degree of this vertice"""
        degrees = [self.degree(v) for v in super().get_vertices()]
        max_degree = max(degrees)
        return degrees.index(max_degree), max_degree


