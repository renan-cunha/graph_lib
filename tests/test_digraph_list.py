import pytest
import random
from src.digraph_list import DigraphList


class TestAbstractDigraph():
    def test_assert_positive_vertice_raises_exception(self):
        with pytest.raises(ValueError) as e:
            graph = DigraphList(-1)

    def test_assert_positive_vertice_zero(self):
        try:
            graph = DigraphList(0)
        except ValueError:
            assert False

    def test_assert_positive_vertice_one(self):
        try:
            graph = DigraphList(1)
        except ValueError:
            assert False

    def test_assert_vertice_exists_in_range(self):
        try:
            graph = DigraphList(3)
            graph.in_neighbourhood(0)
            assert True
        except ValueError:
            assert False

    def test_assert_vertice_exists_less_range(self):
        try:
            graph = DigraphList(3)
            graph.out_neighbourhood(-1)
            assert False
        except ValueError:
            assert True

    def test_assert_vertice_exists_bigger_range(self):
        try:
            graph = DigraphList(3)
            graph.in_neighbourhood(3)
            assert False
        except ValueError:
            assert True

    def test_assert_vertice_exists_two_in_range(self):
        try:
            graph = DigraphList(3)
            graph.add_edge(0,2)
            assert True
        except ValueError:
            assert False

    def test_assert_vertice_exists_first_in_range(self):
        try:
            graph = DigraphList(3)
            graph.add_edge(0,3)
            assert False
        except ValueError:
            assert True

    def test_assert_vertice_exists_last_in_range(self):
        try:
            graph = DigraphList(3)
            graph.add_edge(-1,2)
            assert False
        except ValueError:
            assert True

    def test_assert_vertice_exists_two_not_in_range(self):
        try:
            graph = DigraphList(3)
            graph.add_edge(-1,3)
            assert False
        except ValueError:
            assert True

    def test_number_of_vertice_one(self):
        assert DigraphList(1).number_of_vertices() == 1

    def test_number_of_vertice_zero(self):
        assert DigraphList(0).number_of_vertices() == 0

    def test_number_of_vertice_four(self):
        assert DigraphList(4).number_of_vertices() == 4


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


@pytest.mark.parametrize("edges,expected", [
    ([[0, 0]], (0, 2)),
    ([[0, 0], [0, 1]], (0, 3)),
    ([[0, 0], [0, 1], [0, 2]], (0, 4)),
    ([[1, 1], [0, 1], [0, 2]], (1, 3)),
])
def test_max_degree(edges, expected):
    graph = DigraphList(3)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.max_degree() == expected


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


@pytest.mark.parametrize("edges,size,expected", [
    ([], 1, True),
    ([[0, 0]], 1, True),
    ([], 2, True),
    ([[0, 1]], 2, False),
    ([[0, 0]], 2, True),
    ([[0, 0], [1,1]], 2, False),
    ([[0, 0], [0, 1], [0, 1]], 2, True),
    ([[0, 1], [0, 1]], 2, True),
    ([], 3, True),
    ([[2, 2]], 3, True),
    ([[2, 2], [1, 2]], 3, False),
    ([[0, 1], [1, 2], [0, 2]], 3, True),
    ([[1, 2], [1, 2]], 3, True),
    ([[1, 2], [2, 0]], 3, False),

])
def test_euler_graph(edges, size, expected):
    graph = DigraphList(size)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.is_euler_graph() == expected


@pytest.mark.parametrize("edges,size,expected", [
    ([], 1, False),
    ([[0, 0]], 1, False),
    ([], 2, False),
    ([[0, 1]], 2, True),
    ([[0, 1], [2,2]], 3, False),
    ([[0, 0]], 2, False),
    ([[0, 0], [0, 1], [0, 1]], 2, False),
    ([[0, 1], [0, 1]], 2, False),
    ([], 3, False),
    ([[2, 2]], 3, False),
    ([[2, 2], [1, 2]], 3, True),
    ([[0, 1], [1, 2], [0, 2]], 3, False),
    ([[1, 2], [1, 2]], 3, False),
    ([[1, 2], [2, 0]], 3, True),

])
def test_euler_path(edges, size, expected):
    graph = DigraphList(size)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.has_open_euler_path() == expected


@pytest.mark.parametrize("edges,size,expected", [
    ([], 1, []),
    ([[0, 0]], 1, [0]),
    ([[0, 0], [0, 0]], 1, [0]),
    ([], 2, []),
    ([[0,0]], 2, [0]),
    ([[1,1]], 2, [1]),
    ([[0,0], [1,1]], 2, [0,1]),
    ([[0,0], [0,1], [1,1]], 2, [0,1]),
    ([], 3, []),
    ([[0,0]], 3, [0]),
    ([[1,1]], 3, [1]),
    ([[2,2]], 3, [2]),
    ([[1,2]], 3, [1,2]),
    ([[0,0], [2,2]], 3, [0,2]),
    ([[0,0], [0,1]], 3, [0,1]),
    ([[0,0], [1,2]], 3, [0,1,2]),

])
def test_vertices_with_edges(edges, size, expected):
    graph = DigraphList(size)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.vertices_with_edges() == expected


@pytest.mark.parametrize("edges,size,begin,end,expected", [
    ([[0,1], [1,2], [2,3], [3,4], [0,5]], 6, 0, 5, True),
    ([], 1, 0, 0, False),
    ([[0,0]], 1, 0, 0, True),
    ([[0,0], [0,0]], 1, 0, 0, True),
    ([[0,0], [0,0]], 2, 0, 1, False),
    ([[0,0], [0,1]], 2, 0, 1, True),
    ([[0,0], [0,1], [1,2]], 3, 0, 2, True),
    ([[0,0], [0,1], [1,2]], 3, 1, 2, True),
    ([[0,0], [0,1], [1,2]], 3, 2, 1, True),
    ([[0,0], [0,1], [1,2]], 3, 2, 0, True),
])
def test_path(edges, size, begin, end, expected):
    graph = DigraphList(size)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    print(graph)
    print(begin)
    print(end)
    assert graph.has_path(begin,end) == expected

@pytest.mark.parametrize("edges,size,expected", [
    ([], 1, True),
    ([[0, 0]], 1, True),
    ([[0, 0], [0, 0]], 1, True),
    ([], 2, True),
    ([[0,0]], 2, True),
    ([[1,1]], 2, True),
    ([[0,0], [1,1]], 2, False),
    ([[0,0], [0,1], [1,1]], 2, True),
    ([[0,0]], 3, True),
    ([[0,0], [2,2]], 3, False),
    ([[0,0], [0,1]], 3, True),
    ([[0,0], [1,2]], 3, False),

])
def test_edges_acessible(edges, size, expected):
    graph = DigraphList(size)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.has_acessible_edges() == expected

