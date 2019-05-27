import pytest
from src.graph_matrix import GraphMatrix

@pytest.mark.parametrize("size_graph,edges", [
    (1, []),
    (1, [[0, 0]]),
    (2, []),
    (2, [[0, 0]]),
    (2, [[0, 0], [1, 1]]),
    (2, [[0, 0], [1, 1], [0, 1]]),
    (2, [[0, 0], [1, 1], [0, 1], [1, 0]]),
    (3, [[1, 2], [2, 1]]),
    (3, [[1, 2]]),
    (3, [[2, 1]]),
])
def test_num_edges(size_graph, edges):
    graph = GraphMatrix(size_graph, digraph=True)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.number_of_edges() == len(edges)


@pytest.mark.parametrize("edges,vertice,expected", [
    ([[0, 0]], 0, [0]),
    ([[0, 0], [0, 1]], 0, [0, 1]),
    ([[0, 0], [0, 1]], 1, []),
    ([[0, 0], [0, 1], [0, 2]], 0, [0, 1, 2]),
])
def test_out_neighbourhood(edges, vertice, expected):
    graph = GraphMatrix(3, digraph=True)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.out_neighbourhood(vertice) == expected


@pytest.mark.parametrize("edges,vertice,expected", [
    ([[0, 0]], 0, [0]),
    ([[0, 0], [0, 1]], 0, [0]),
    ([[0, 0], [0, 1]], 1, [0]),
    ([[0, 0], [0, 1], [0, 2]], 0, [0]),
])
def test_in_neighbourhood(edges, vertice, expected):
    graph = GraphMatrix(3, digraph=True)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.in_neighbourhood(vertice) == expected


@pytest.mark.parametrize("edges,vertice,expected", [
    ([[0, 0]], 0, 1),
    ([[0, 0], [0, 1]], 0, 2),
    ([[0, 0], [0, 1]], 1, 0),
    ([[0, 0], [0, 1], [0, 2]], 0, 3),
])
def test_out_degree(edges, vertice, expected):
    graph = GraphMatrix(3, digraph=True)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.out_degree(vertice) == expected


@pytest.mark.parametrize("edges,vertice,expected", [
    ([[0, 0]], 0, 1),
    ([[0, 0], [0, 1]], 0, 1),
    ([[0, 0], [0, 1]], 1, 1),
    ([[0, 0], [0, 1], [0, 2]], 0, 1),
    ([[0, 0], [0, 1], [2, 1]], 1, 2),
    ([[0, 0], [0, 1]], 2, 0),
])
def test_in_degree(edges, vertice, expected):
    graph = GraphMatrix(3, digraph=True)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.in_degree(vertice) == expected


@pytest.mark.parametrize("edges,expected", [
    ([[0, 0]], (0, 1)),
    ([[0, 0], [0, 1]], (0, 2)),
    ([[0, 0], [0, 1], [0, 2]], (0, 3)),
    ([[1, 1], [0, 1], [1, 2]], (1, 2)),
])
def test_max_out_degree(edges, expected):
    graph = GraphMatrix(3, digraph=True)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.max_out_degree() == expected


@pytest.mark.parametrize("edges,expected", [
    ([[0, 0]], (0, 1)),
    ([[0, 0], [0, 1], [2, 1]], (1, 2)),
    ([[0, 0], [1, 0], [2, 0]], (0, 3)),
    ([], (0, 0)),
])
def test_max_in_degree(edges, expected):
    graph = GraphMatrix(3, digraph=True)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.max_in_degree() == expected


@pytest.mark.parametrize("edges,expected", [
    ([[0, 0]], 1),
    ([[0, 0], [0, 1]], 1),
    ([[0, 0], [0, 1], [0, 2]], 1),
    ([[1, 1], [0, 1], [0, 2]], 1),
    ([[1, 1], [0, 0]], 2),
    ([[1, 2], [0, 1], [0, 2]], 0),
])
def test_num_loops_graph(edges, expected):
    graph = GraphMatrix(3, digraph=True)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.number_of_loops_graph() == expected


