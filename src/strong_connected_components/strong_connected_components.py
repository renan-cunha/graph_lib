from src.graph_matrix import GraphMatrix
from src.search.depth_first_search_digraph import DepthFirstSearch
from src.search.connected_components_digraph import ConnectedComponents
import numpy as np
from typing import List, Dict


class StrongComponents:

    def __init__(self, graph: GraphMatrix):
        self.graph = graph

    def run(self) -> Dict[int, List[int]]:
        dfs = DepthFirstSearch(self.graph)
        times = dfs.final_vertice_time
        transpose_graph = self.graph.transpose()
        list_vertices = list(reversed(np.argsort(times).tolist()))
        self.connected_components = ConnectedComponents(transpose_graph,
                                                        list_vertices)
        ids = self.connected_components.id

        result: Dict[int, List[int]] = {}
        for id in range(self.get_count()):
            result[id] = []

        for index, id in enumerate(ids):
            result[id].append(index)
        return result

    def get_count(self) -> int:
        return self.connected_components.get_count()

    def __str__(self) -> str:
        dict = self.run()
        result = ""
        for key in dict:
            result += f"{dict[key]}\n"
        return result[:-1]



