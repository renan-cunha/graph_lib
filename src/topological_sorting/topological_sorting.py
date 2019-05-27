from src.graph_matrix import GraphMatrix
from typing import List
from src.search.depth_first_search_digraph import DepthFirstSearch


def topological_sorting(graph: GraphMatrix) -> List[int]:
    dfs = DepthFirstSearch(graph)
    times = dfs.final_vertice_time
    print(times)
    len_times = len(times)
    times = [[i, times[i]] for i in range(len_times)]
    times.sort(key=lambda x: x[1], reverse=True)
    return [times[i][0] for i in range(len_times)]





