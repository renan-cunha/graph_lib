import pytest
from src.graph_adjacency_list import GraphAdjacencyList
from src.graph_matrix import GraphMatrix
from src.search.connected_components import ConnectedComponents
from src.graph import Graph


@pytest.mark.parametrize("num_vertices,edges_list,expected", [
    (1, [], 1),
    (1, [(0, 0)], 1),
    (1, [(0, 0), (0, 0)], 1),

    (2, [], 2),
    (2, [(0, 0)], 2),
    (2, [(1, 1)], 2),
    (2, [(0, 0), (1, 1)], 2),
    (2, [(0, 1)], 1),
    (2, [(0, 0), (0, 1), (1, 1)], 1),

    (3, [], 3),
    (3, [(0, 0)], 3),
    (3, [(0, 0), (1, 1)], 3),
    (3, [(0, 0), (1, 1), (2, 2)], 3),
    (3, [(0, 1)], 2),
    (3, [(1, 2)], 2),
    (3, [(0, 2)], 2),
    (3, [(0, 2), (0, 0)], 2),
    (3, [(0, 2), (0, 0), (2, 2)], 2),
    (3, [(0, 2), (0, 0), (2, 2), (1, 1)], 2),
    (3, [(0, 2), (0, 0), (2, 2), (1, 1), (0, 2)], 2),
    (3, [(0, 2), (0, 0), (2, 2), (1, 1), (0, 2)], 2),
    (3, [(0, 1), (1, 2)], 1),
    (3, [(0, 1), (1, 2), (0, 2)], 1),
])
def test_connected_components_adjacency_list(num_vertices, edges_list,
                                             expected):
    graph: Graph = GraphAdjacencyList(num_vertices)
    num_edges: int = len(edges_list)
    if num_edges > 0:
        for x, y in edges_list:
            graph.add_edge(x, y)
    connected_components = ConnectedComponents(graph)
    num_components = connected_components.get_count()
    assert num_components == expected


@pytest.mark.parametrize("num_vertices,edges_list,expected", [
    (1, [], 1),
    (1, [(0, 0)], 1),

    (2, [], 2),
    (2, [(0, 0)], 2),
    (2, [(1, 1)], 2),
    (2, [(0, 0), (1, 1)], 2),
    (2, [(0, 1)], 1),
    (2, [(0, 0), (0, 1), (1, 1)], 1),

    (3, [], 3),
    (3, [(0, 0)], 3),
    (3, [(0, 0), (1, 1)], 3),
    (3, [(0, 0), (1, 1), (2, 2)], 3),
    (3, [(0, 1)], 2),
    (3, [(1, 2)], 2),
    (3, [(0, 2)], 2),
    (3, [(0, 2), (0, 0)], 2),
    (3, [(0, 2), (0, 0), (2, 2)], 2),
    (3, [(0, 2), (0, 0), (2, 2), (1, 1)], 2),
    (3, [(0, 1), (1, 2)], 1),
    (3, [(0, 1), (1, 2), (0, 2)], 1),
])
def test_connected_components_matrix(num_vertices, edges_list,
                                             expected):
    graph: Graph = GraphMatrix(num_vertices)
    num_edges: int = len(edges_list)
    if num_edges > 0:
        for x, y in edges_list:
            graph.add_edge(x, y)
    connected_components = ConnectedComponents(graph)
    num_components = connected_components.get_count()
    assert num_components == expected
