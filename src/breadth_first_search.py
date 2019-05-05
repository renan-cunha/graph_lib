from src.graph import Graph
from typing import List
from src.search_color import Color
from queue import Queue


class BreadthFirstSearch:
    """Class that performs the depth-first search algorithm"""
    def __init__(self, graph: Graph, start_vertice: int):
        self.color: List = [Color.WHITE]*graph.number_of_vertices()
        self.__run(graph, start_vertice)

    def __run(self, graph: Graph, vertice: int) -> None:
        queue: Queue = Queue()
        self.color[vertice] = Color.GRAY
        queue.put(vertice)
        while not queue.empty():
            new_vertice: int = queue.get()
            for adjacent_vertice in graph.neighbourhood(new_vertice):
                if self.color[adjacent_vertice] == Color.WHITE:
                    self.color[adjacent_vertice] = Color.GRAY
                    queue.put(adjacent_vertice)
            self.color[new_vertice] = Color.BLACK
