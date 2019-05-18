import pytest
from src.graph.digraph_list import DigraphList


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

