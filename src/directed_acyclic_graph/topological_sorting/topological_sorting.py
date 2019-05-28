from src.graph_matrix import GraphMatrix
from typing import List
from src.directed_acyclic_graph.depth_first_search_dag import DepthFirstSearchDAG


def topological_sorting(graph: GraphMatrix) -> List[int]:
    if not graph.digraph:
        raise ValueError("Not a digraph")

    dfs = DepthFirstSearchDAG(graph)

    if not dfs.is_dag():
        raise ValueError("Not a DAG")

    times = dfs.final_vertice_time
    len_times = len(times)
    times = [[i, times[i]] for i in range(len_times)]
    times.sort(key=lambda x: x[1], reverse=True)
    return [times[i][0] for i in range(len_times)]




