from src.graph.abstract_digraph import AbstractDigraph
from typing import List


class DepthFirstSearch:
    """Class that performs the depth-first search algorithm"""
    def __init__(self, graph: AbstractDigraph, start_vertice: int):
        self.marked_vertices: List[bool] = [False]*graph.number_of_vertices()
        self.discovered_vertice_time: List = [None]*graph.number_of_vertices()
        self.final_vertice_time: List = [None]*graph.number_of_vertices()
        self.predecessor: List = [None]*graph.number_of_vertices()
        self.count: int = 0
        self.run(graph, start_vertice)

    def run(self, graph: AbstractDigraph, vertice: int) -> None:
        self.marked_vertices[vertice] = True
        self.count += 1
        self.discovered_vertice_time[vertice] = self.count
        for connected_vertice in graph.neighbourhood(vertice):
            if not self.marked_vertices[connected_vertice]:
                self.predecessor[connected_vertice] = vertice
                self.run(graph, connected_vertice)
        self.count += 1
        self.final_vertice_time[vertice] = self.count



