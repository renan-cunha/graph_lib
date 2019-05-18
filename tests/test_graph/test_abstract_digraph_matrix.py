import pytest
from src.graph.digraph_matrix import DigraphMatrix


class TestAbstractDigraph():
    def test_assert_positive_vertice_raises_exception(self):
        with pytest.raises(ValueError) as e:
            graph = DigraphMatrix(-1)

    def test_assert_positive_vertice_zero(self):
        try:
            graph = DigraphMatrix(0)
        except ValueError:
            assert False

    def test_assert_positive_vertice_one(self):
        try:
            graph = DigraphMatrix(1)
        except ValueError:
            assert False

    def test_assert_vertice_exists_in_range(self):
        try:
            graph = DigraphMatrix(3)
            graph.in_neighbourhood(0)
            assert True
        except ValueError:
            assert False

    def test_assert_vertice_exists_less_range(self):
        try:
            graph = DigraphMatrix(3)
            graph.out_neighbourhood(-1)
            assert False
        except ValueError:
            assert True

    def test_assert_vertice_exists_bigger_range(self):
        try:
            graph = DigraphMatrix(3)
            graph.in_neighbourhood(3)
            assert False
        except ValueError:
            assert True

    def test_assert_vertice_exists_two_in_range(self):
        try:
            graph = DigraphMatrix(3)
            graph.add_edge(0,2)
            assert True
        except ValueError:
            assert False

    def test_assert_vertice_exists_first_in_range(self):
        try:
            graph = DigraphMatrix(3)
            graph.add_edge(0,3)
            assert False
        except ValueError:
            assert True

    def test_assert_vertice_exists_last_in_range(self):
        try:
            graph = DigraphMatrix(3)
            graph.add_edge(-1,2)
            assert False
        except ValueError:
            assert True

    def test_assert_vertice_exists_two_not_in_range(self):
        try:
            graph = DigraphMatrix(3)
            graph.add_edge(-1,3)
            assert False
        except ValueError:
            assert True

    def test_number_of_vertice_one(self):
        assert DigraphMatrix(1).number_of_vertices() == 1

    def test_number_of_vertice_zero(self):
        assert DigraphMatrix(0).number_of_vertices() == 0

    def test_number_of_vertice_four(self):
        assert DigraphMatrix(4).number_of_vertices() == 4

