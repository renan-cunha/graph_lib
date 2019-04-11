import pytest
from src.graph import Graph
from src.graph_adjacency_list import GraphAdjacencyList


def test_assert_positive_vertice_raises_exception():
    with pytest.raises(ValueError) as e:
        graph = GraphAdjacencyList(-1)


def test_asser_positive_vertice_zero():
    try:
        graph = GraphAdjacencyList(0)
    except ValueError:
        assert False


def test_assert_positive_vertice_one():
    try:
        graph = GraphAdjacencyList(1)
    except ValueError:
        assert False


def test_assert_vertice_exists_in_range():
    try:
        graph = GraphAdjacencyList(3)
        graph.neighbourhood(0)
        assert True
    except ValueError:
        assert False


def test_assert_vertice_exists_less_range():
    try:
        graph = GraphAdjacencyList(3)
        graph.neighbourhood(-1)
        assert False
    except ValueError:
        assert True


def test_assert_vertice_exists_bigger_range():
    try:
        graph = GraphAdjacencyList(3)
        graph.neighbourhood(3)
        assert False
    except ValueError:
        assert True


def test_assert_vertice_exists_two_in_range():
    try:
        graph = GraphAdjacencyList(3)
        graph.add_edge(0,2)
        assert True
    except ValueError:
        assert False


def test_assert_vertice_exists_first_in_range():
    try:
        graph = GraphAdjacencyList(3)
        graph.add_edge(0,3)
        assert False
    except ValueError:
        assert True


def test_assert_vertice_exists_last_in_range():
    try:
        graph = GraphAdjacencyList(3)
        graph.add_edge(-1,2)
        assert False
    except ValueError:
        assert True


def test_assert_vertice_exists_two_not_in_range():
    try:
        graph = GraphAdjacencyList(3)
        graph.add_edge(-1,3)
        assert False
    except ValueError:
        assert True


def test_number_of_vertice_one():
    assert GraphAdjacencyList(1).number_of_vertices() == 1


def test_number_of_vertice_zero():
    assert GraphAdjacencyList(0).number_of_vertices() == 0


def test_number_of_vertice_four():
    assert GraphAdjacencyList(4).number_of_vertices() == 4