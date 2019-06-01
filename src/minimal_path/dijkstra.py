from src.graph_matrix import GraphMatrix
from typing import Dict, List, Tuple, Set
import numpy as np


class Dijkstra:

    def __init__(self, graph: GraphMatrix):
        self.graph = graph

        self.__inf = float("Inf")
        self.__num_vertices = graph.number_of_vertices()
        self.__reset()

    def __empty(self) -> bool:
        """Returns True if all vertices are marked, False otherwise"""
        if self.priority_list == [self.__inf]*self.__num_vertices:
            result = True
        else:
            result = False
        return result

    def __get(self) -> int:
        """Gets the vertice with minimum distance that is not marked"""
        return int(np.argmin(self.priority_list))

    def run(self, start_vertice: int) -> Dict[int, Tuple[float, List[int]]]:
        """It returns a dict of a dicts like
            {vertice1: (cost, [vertice,B,...,vertice1),...}"""
        vertice = start_vertice
        self.minimal_distance[vertice] = 0
        self.priority_list[vertice] = 0
        self.marked.add(vertice)

        while not self.__empty():
            vertice = self.__get()
            self.priority_list[vertice] = self.__inf
            for adjacent_vertice in self.graph.out_neighbourhood(vertice):
                if adjacent_vertice not in self.marked:
                    weight = self.graph.weight[vertice][adjacent_vertice]
                    self.__relax(vertice, adjacent_vertice, weight)
            self.marked.add(vertice)
        return self.__output(start_vertice)

    def __output(self, start_vertice: int) -> Dict[int, Tuple[float,
                                                              List[int]]]:
        """Makes the final dict of the class vectors"""
        output: Dict[int, Tuple[float, List[int]]] = {}
        for vertice in range(self.__num_vertices):
            min_distance = self.minimal_distance[vertice]
            path = self.__path(start_vertice, vertice)
            output[vertice] = (min_distance, path)
        self.__reset()
        return output

    def __path(self, begin_vertice: int, end_vertice: int) -> List[int]:
        """Makes a path from the class vectors"""
        path: List = [end_vertice]
        vertice = end_vertice
        while vertice != begin_vertice:
            try:
                predecessor = self.predecessor[vertice]
            except TypeError:
                break
            path.append(predecessor)
            vertice = predecessor

        path.reverse()
        return path

    def __reset(self) -> None:
        self.minimal_distance: List[float] = [self.__inf]*self.__num_vertices
        self.predecessor: List = [None]*self.__num_vertices
        self.priority_list: List[float] = [self.__inf]*self.__num_vertices
        self.marked: Set[int] = set()

    def __relax(self, vertice_from: int, vertice_to: int,
                weight: float) -> None:
        """Decreases the minimum distance to a vertice if it is possible"""
        cond1 = self.minimal_distance[vertice_to]
        cond2 = self.minimal_distance[vertice_from] + weight

        if cond1 > cond2:
            self.minimal_distance[vertice_to] = cond2
            self.priority_list[vertice_to] = cond2
            self.predecessor[vertice_to] = vertice_from


