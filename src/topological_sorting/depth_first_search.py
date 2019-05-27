from src.graph_matrix import GraphMatrix
from typing import List
from src.search.color import Color


class DepthFirstSearch:
    """Class that performs the depth-first search algorithm"""
    def __init__(self, graph: GraphMatrix):
        if not graph.digraph:
            raise ValueError("this graph is not directed")
        self.color: List[Color] = [Color.WHITE] * graph.number_of_vertices()
        self.discovered_vertice_time: List = [None]*graph.number_of_vertices()
        self.final_vertice_time: List = [None]*graph.number_of_vertices()
        self.predecessor: List = [None]*graph.number_of_vertices()
        self.count: int = 0

        for vertice in graph.get_vertices():
            if self.color[vertice] != Color.BLACK:
                self.run(graph, vertice)

    def run(self, graph: GraphMatrix, vertice: int) -> None:
        self.color[vertice] = Color.GRAY
        self.count += 1
        self.discovered_vertice_time[vertice] = self.count
        for connected_vertice in graph.out_neighbourhood(vertice):
            if self.color[connected_vertice] == Color.WHITE:
                self.predecessor[connected_vertice] = vertice
                self.run(graph, connected_vertice)
        self.color[vertice] = Color.BLACK
        self.count += 1
        self.final_vertice_time[vertice] = self.count



