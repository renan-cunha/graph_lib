import pytest
import random
from src.graph.digraph_list import DigraphList


@pytest.mark.parametrize("input,expected", [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (7, 7),
])
def test_number_of_edges(input, expected):
    graph = DigraphList(10)
    for i in range(input):
        edge1 = random.randint(0, 9)
        edge2 = random.randint(0, 9)
        graph.add_edge(edge1, edge2)
    assert graph.number_of_edges() == expected


@pytest.mark.parametrize("edges,vertice,expected", [
    ([[0, 0]], 0, {0}),
    ([[0, 0], [0, 1]], 0, {0, 1}),
    ([[0, 0], [0, 1]], 1, set()),
    ([[0, 0], [0, 1], [0, 2]], 0, {0, 1, 2}),
])
def test_out_neighbourhood(edges, vertice, expected):
    graph = DigraphList(3)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.out_neighbourhood(vertice) == expected


@pytest.mark.parametrize("edges,vertice,expected", [
    ([[0, 0]], 0, {0}),
    ([[0, 0], [0, 1]], 0, {0}),
    ([[0, 0], [0, 1]], 1, {0}),
    ([[0, 0], [0, 1], [0, 2]], 0, {0}),
])
def test_in_neighbourhood(edges, vertice, expected):
    graph = DigraphList(3)
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
    graph = DigraphList(3)
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
    graph = DigraphList(3)
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
    graph = DigraphList(3)
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
    graph = DigraphList(3)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.max_in_degree() == expected


@pytest.mark.parametrize("edges,vertice,expected", [
    ([[0, 0]], 0, 1),
    ([[0, 0], [0, 1]], 0, 1),
    ([[0, 0], [0, 1]], 1, 0),
    ([[0, 0], [0, 1], [0, 2]], 0, 1),
    ([[1, 1], [1, 1]], 1, 2),
])
def test_num_loops_vertice(edges, vertice, expected):
    graph = DigraphList(3)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.number_of_loops_vertice(vertice) == expected


@pytest.mark.parametrize("edges,expected", [
    ([[0, 0]], 1),
    ([[0, 0], [0, 1]], 1),
    ([[0, 0], [0, 1], [0, 2]], 1),
    ([[1, 1], [0, 1], [0, 2]], 1),
    ([[1, 1], [1, 1]], 2),
    ([[1, 2], [0, 1], [0, 2]], 0),
])
def test_num_loops_graph(edges, expected):
    graph = DigraphList(3)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.number_of_loops_graph() == expected


