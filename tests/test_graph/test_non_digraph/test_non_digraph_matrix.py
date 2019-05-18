import pytest
from src.graph.non_digraph_matrix import NonDigraphMatrix


def test_assert_positive_vertice_raises_exception():
    with pytest.raises(ValueError) as e:
        graph = NonDigraphMatrix(-1)


def test_asser_positive_vertice_zero():
    try:
        graph = NonDigraphMatrix(0)
    except ValueError:
        assert False


def test_assert_positive_vertice_one():
    try:
        graph = NonDigraphMatrix(1)
    except ValueError:
        assert False


def test_assert_vertice_exists_in_range():
    try:
        graph = NonDigraphMatrix(3)
        graph.neighbourhood(0)
        assert True
    except ValueError:
        assert False


def test_assert_vertice_exists_less_range():
    try:
        graph = NonDigraphMatrix(3)
        graph.neighbourhood(-1)
        assert False
    except ValueError:
        assert True


def test_assert_vertice_exists_bigger_range():
    try:
        graph = NonDigraphMatrix(3)
        graph.neighbourhood(3)
        assert False
    except ValueError:
        assert True


def test_assert_vertice_exists_two_in_range():
    try:
        graph = NonDigraphMatrix(3)
        graph.add_edge(0,2)
        assert True
    except ValueError:
        assert False


def test_assert_vertice_exists_first_in_range():
    try:
        graph = NonDigraphMatrix(3)
        graph.add_edge(0,3)
        assert False
    except ValueError:
        assert True


def test_assert_vertice_exists_last_in_range():
    try:
        graph = NonDigraphMatrix(3)
        graph.add_edge(-1,2)
        assert False
    except ValueError:
        assert True


def test_assert_vertice_exists_two_not_in_range():
    try:
        graph = NonDigraphMatrix(3)
        graph.add_edge(-1,3)
        assert False
    except ValueError:
        assert True


def test_number_of_vertice_one():
    assert NonDigraphMatrix(1).number_of_vertices() == 1


def test_number_of_vertice_zero():
    assert NonDigraphMatrix(0).number_of_vertices() == 0


def test_number_of_vertice_four():
    assert NonDigraphMatrix(4).number_of_vertices() == 4


@pytest.mark.parametrize("size, edges,expected", [
    (0, [], 0),
    (1, [], 0),
    (1, [[0,0]], 1),
    (2, [], 0),
    (2, [[0,1]], 1),
    (2, [[0,1],[0,0],[1,1]], 3),
    (3, [], 0),
    (3, [[0,0], [1,1], [2,2]], 3),
    (3, [[0,0], [1,1], [2,2], [0,1], [0,2], [1,2]], 6),
])
def test_number_of_edges(size, edges, expected):
    graph = NonDigraphMatrix(size)
    print(graph)
    for x, y in edges:
        graph.add_edge(x, y)
    print(graph)
    assert graph.number_of_edges() == expected


@pytest.mark.parametrize("edges,vertice,expected", [
    ([[0, 0]], 0, {0}),
    ([[0, 0], [0, 1]], 0, {0, 1}),
    ([[0, 0], [0, 1]], 1, {0}),
    ([[0, 0], [0, 1], [0, 2]], 0, {0, 1, 2}),
])
def test_neighbourhood(edges, vertice, expected):
    graph = NonDigraphMatrix(3)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.neighbourhood(vertice) == expected


@pytest.mark.parametrize("edges,vertice,expected", [
    ([[0, 0]], 0, 2),
    ([[0, 0], [0, 1]], 0, 3),
    ([[0, 0], [0, 1]], 1, 1),
    ([[0, 0], [0, 1], [0, 2]], 0, 4),
])
def test_degree(edges, vertice, expected):
    graph = NonDigraphMatrix(3)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.degree(vertice) == expected


@pytest.mark.parametrize("edges,expected", [
    ([[0, 0]], (0, 2)),
    ([[0, 0], [0, 1]], (0, 3)),
    ([[0, 0], [0, 1], [0, 2]], (0, 4)),
    ([[1, 1], [0, 1], [0, 2]], (1, 3)),
])
def test_max_degree(edges, expected):
    graph = NonDigraphMatrix(3)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.max_degree() == expected


@pytest.mark.parametrize("edges,expected", [
    ([[0, 0]], 1),
    ([[0, 0], [0, 1]], 1),
    ([[0, 0], [0, 1], [0, 2]], 1),
    ([[1, 1], [0, 1], [0, 2]], 1),
    ([[1, 1], [2, 1]], 1),
    ([[1, 2], [0, 1], [0, 2]], 0),
])
def test_num_loops_graph(edges, expected):
    graph = NonDigraphMatrix(3)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.number_of_loops_graph() == expected



