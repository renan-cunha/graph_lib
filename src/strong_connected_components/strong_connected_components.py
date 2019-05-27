from src.graph_matrix import GraphMatrix
from src.search.depth_first_search_digraph import DepthFirstSearch
from src.search.connected_components_digraph import ConnectedComponents
import numpy as np


def num_strong_connected_components(graph: GraphMatrix) -> int:
    dfs = DepthFirstSearch(graph)
    times = dfs.final_vertice_time
    transpose_graph = graph.transpose()
    list_vertices = list(reversed(np.argsort(times).tolist()))
    connected_components = ConnectedComponents(transpose_graph,
                                               list_vertices=list_vertices)

    return connected_components.get_count()


