from src.graph import Graph
from typing import List
from src.search.color import Color
from queue import Queue


class BreadthFirstSearch:
    """Class that performs the depth-first search algorithm"""
    def __init__(self, graph: Graph):
        number_of_vertices = graph.number_of_vertices()
        self.color: List[Color] = [Color.WHITE]*number_of_vertices
        self.dist_from_source: List = [None] * number_of_vertices
        self.parent_vertice: List = [None]*number_of_vertices
        for vertice in graph.get_vertices():
            if self.color[vertice] != Color.BLACK:
                self.__run(graph, vertice)

    def __run(self, graph: Graph, vertice: int) -> None:
        queue: Queue = Queue()
        self.color[vertice] = Color.GRAY
        self.dist_from_source[vertice] = 0
        queue.put(vertice)
        while not queue.empty():
            new_vertice: int = queue.get()
            for adjacent_vertice in graph.neighbourhood(new_vertice):
                if self.color[adjacent_vertice] == Color.WHITE:
                    self.color[adjacent_vertice] = Color.GRAY

                    self.parent_vertice[adjacent_vertice] = new_vertice

                    parent_distance: int = self.dist_from_source[new_vertice]
                    temp_distance: int = parent_distance + 1
                    self.dist_from_source[adjacent_vertice] = temp_distance

                    queue.put(adjacent_vertice)
            self.color[new_vertice] = Color.BLACK
