import pytest
from src.search.breadth_first_search import BreadthFirstSearch
from src.search.color import Color
from src.graph.digraph_list import DigraphList
from src.graph.digraph_matrix import DigraphMatrix

@pytest.mark.parametrize("num_vertices,edges_list,start_vertice,color_list,"
                         "result", [
    (1, [], 0, [Color.BLACK], True),
    (1, [], 0, [Color.WHITE], False),
    (1, [], 0, [Color.GRAY], False),
    (1, [[0, 0]], 0, [Color.GRAY], False),
    (1, [[0, 0]], 0, [Color.WHITE], False),
    (1, [[0, 0]], 0, [Color.BLACK], True),
    (1, [[0, 0], [0, 0]], 0, [Color.BLACK], True),
    (1, [[0, 0], [0, 0]], 0, [Color.WHITE], False),
    (1, [[0, 0], [0, 0]], 0, [Color.GRAY], False),

    (2, [], 0, [Color.BLACK, Color.WHITE], True),
    (2, [], 1, [Color.WHITE, Color.BLACK], True),
    (2, [[0, 0], [1, 1]], 1, [Color.WHITE, Color.BLACK], True),
    (2, [[0, 0], [0, 1], [1, 1]], 1, [Color.BLACK, Color.BLACK], True),
    (2, [[0, 0], [0, 1], [1, 1]], 0, [Color.BLACK, Color.BLACK], True),
    (2, [[0, 1]], 1, [Color.BLACK, Color.BLACK], True),
    (2, [[0, 1]], 0, [Color.BLACK, Color.BLACK], True),

    (3, [], 0, [Color.BLACK, Color.WHITE, Color.WHITE], True),
    (3, [], 1, [Color.WHITE, Color.BLACK, Color.WHITE], True),
    (3, [], 2, [Color.WHITE, Color.WHITE, Color.BLACK], True),
    (3, [[0, 1]], 2, [Color.WHITE, Color.WHITE, Color.BLACK], True),
    (3, [[0, 1]], 0, [Color.BLACK, Color.BLACK, Color.WHITE], True),
    (3, [[0, 1]], 1, [Color.BLACK, Color.BLACK, Color.WHITE], True),
    (3, [[0, 1], [1, 2]], 1, [Color.BLACK, Color.BLACK, Color.BLACK], True),
    (3, [[1, 2]], 1, [Color.WHITE, Color.BLACK, Color.BLACK], True),
    (3, [[1, 2]], 2, [Color.WHITE, Color.BLACK, Color.BLACK], True),
])
def test_color_bfs_adjacency_list(num_vertices, edges_list, start_vertice,
                                  color_list, result):
    graph = DigraphList(num_vertices)
    length_list = len(edges_list)
    if length_list > 0:
        for x, y in edges_list:
            graph.add_edge(x, y)
    bfs = BreadthFirstSearch(graph, start_vertice)
    color_bfs = bfs.color
    output = (color_bfs == color_list)
    assert output == result

@pytest.mark.parametrize("num_vertices,edges_list,start_vertice,color_list,"
                         "result", [
     (1, [], 0, [Color.BLACK], True),
     (1, [], 0, [Color.WHITE], False),
     (1, [], 0, [Color.GRAY], False),
     (1, [[0, 0]], 0, [Color.GRAY], False),
     (1, [[0, 0]], 0, [Color.WHITE], False),
     (1, [[0, 0]], 0, [Color.BLACK], True),

     (2, [], 0, [Color.BLACK, Color.WHITE], True),
     (2, [], 1, [Color.WHITE, Color.BLACK], True),
     (2, [[0, 0], [1, 1]], 1, [Color.WHITE, Color.BLACK], True),
     (2, [[0, 0], [0, 1], [1, 1]], 1, [Color.BLACK, Color.BLACK], True),
     (2, [[0, 0], [0, 1], [1, 1]], 0, [Color.BLACK, Color.BLACK], True),
     (2, [[0, 1]], 1, [Color.BLACK, Color.BLACK], True),
     (2, [[0, 1]], 0, [Color.BLACK, Color.BLACK], True),

     (3, [], 0, [Color.BLACK, Color.WHITE, Color.WHITE], True),
     (3, [], 1, [Color.WHITE, Color.BLACK, Color.WHITE], True),
     (3, [], 2, [Color.WHITE, Color.WHITE, Color.BLACK], True),
     (3, [[0, 1]], 2, [Color.WHITE, Color.WHITE, Color.BLACK], True),
     (3, [[0, 1]], 0, [Color.BLACK, Color.BLACK, Color.WHITE], True),
     (3, [[0, 1]], 1, [Color.BLACK, Color.BLACK, Color.WHITE], True),
     (3, [[0, 1], [1, 2]], 1, [Color.BLACK, Color.BLACK, Color.BLACK], True),
     (3, [[1, 2]], 1, [Color.WHITE, Color.BLACK, Color.BLACK], True),
     (3, [[1, 2]], 2, [Color.WHITE, Color.BLACK, Color.BLACK], True),
                         ])
def test_color_bfs_matrix(num_vertices, edges_list, start_vertice,
                                  color_list, result):
    graph = DigraphMatrix(num_vertices)
    length_list = len(edges_list)
    if length_list > 0:
        for x, y in edges_list:
            graph.add_edge(x, y)
    bfs = BreadthFirstSearch(graph, start_vertice)
    color_bfs = bfs.color
    output = (color_bfs == color_list)
    assert output == result


@pytest.mark.parametrize("num_vertices,edges_list,start_vertice,distance_list",[
    (1, [], 0, [0]),
    (1, [[0, 0]], 0, [0]),
    (1, [[0, 0], [0, 0]], 0, [0]),

    (2, [], 0, [0, None]),
    (2, [], 1, [None, 0]),
    (2, [[0, 0], [1, 1]], 1, [None, 0]),
    (2, [[0, 0], [1, 1]], 0, [0, None]),
    (2, [[0, 0], [0, 1], [1, 1]], 1, [1, 0]),
    (2, [[0, 0], [0, 1], [1, 1]], 0, [0, 1]),
    (2, [[0, 1]], 1, [1, 0]),
    (2, [[0, 1]], 0, [0, 1]),

    (3, [], 0, [0, None, None]),
    (3, [], 1, [None, 0, None]),
    (3, [], 2, [None, None, 0]),
    (3, [[0, 1]], 2, [None, None, 0]),
    (3, [[0, 1]], 0, [0, 1, None]),
    (3, [[0, 1]], 1, [1, 0, None]),
    (3, [[0, 1], [1, 2]], 1, [1, 0, 1]),
    (3, [[0, 1], [1, 2]], 0, [0, 1, 2]),
    (3, [[0, 1], [1, 2]], 2, [2, 1, 0]),
    (3, [[1, 2]], 1, [None, 0, 1]),
    (3, [[1, 2]], 2, [None, 1, 0]),
                         ])
def test_distance_bfs_adjacency_list(num_vertices, edges_list, start_vertice,
                                  distance_list):
    graph = DigraphList(num_vertices)
    length_list = len(edges_list)
    if length_list > 0:
        for x, y in edges_list:
            graph.add_edge(x, y)
    bfs = BreadthFirstSearch(graph, start_vertice)
    distance_bfs = bfs.dist_from_source
    assert distance_bfs == distance_list



@pytest.mark.parametrize("num_vertices,edges_list,start_vertice,distance_list",[
    (1, [], 0, [0]),
    (1, [[0, 0]], 0, [0]),

    (2, [], 0, [0, None]),
    (2, [], 1, [None, 0]),
    (2, [[0, 0], [1, 1]], 1, [None, 0]),
    (2, [[0, 0], [1, 1]], 0, [0, None]),
    (2, [[0, 0], [0, 1], [1, 1]], 1, [1, 0]),
    (2, [[0, 0], [0, 1], [1, 1]], 0, [0, 1]),
    (2, [[0, 1]], 1, [1, 0]),
    (2, [[0, 1]], 0, [0, 1]),

    (3, [], 0, [0, None, None]),
    (3, [], 1, [None, 0, None]),
    (3, [], 2, [None, None, 0]),
    (3, [[0, 1]], 2, [None, None, 0]),
    (3, [[0, 1]], 0, [0, 1, None]),
    (3, [[0, 1]], 1, [1, 0, None]),
    (3, [[0, 1], [1, 2]], 1, [1, 0, 1]),
    (3, [[0, 1], [1, 2]], 0, [0, 1, 2]),
    (3, [[0, 1], [1, 2]], 2, [2, 1, 0]),
    (3, [[1, 2]], 1, [None, 0, 1]),
    (3, [[1, 2]], 2, [None, 1, 0]),
])
def test_distance_bfs_matrix(num_vertices, edges_list, start_vertice,
                                  distance_list):
    graph = DigraphMatrix(num_vertices)
    length_list = len(edges_list)
    if length_list > 0:
        for x, y in edges_list:
            graph.add_edge(x, y)
    bfs = BreadthFirstSearch(graph, start_vertice)
    distance_bfs = bfs.dist_from_source
    assert distance_bfs == distance_list


@pytest.mark.parametrize("num_vertices,edges_list,start_vertice,parent_list",[
    (1, [], 0, [None]),
    (1, [[0, 0]], 0, [None]),
    (1, [[0, 0], [0, 0]], 0, [None]),

    (2, [], 0, [None, None]),
    (2, [], 1, [None, None]),
    (2, [[0, 0], [1, 1]], 1, [None, None]),
    (2, [[0, 0], [1, 1]], 0, [None, None]),
    (2, [[0, 0], [0, 1], [1, 1]], 1, [1, None]),
    (2, [[0, 0], [0, 1], [1, 1]], 0, [None, 0]),
    (2, [[0, 1]], 1, [1, None]),
    (2, [[0, 1]], 0, [None, 0]),

    (3, [], 0, [None, None, None]),
    (3, [], 1, [None, None, None]),
    (3, [], 2, [None, None, None]),
    (3, [[0, 1]], 2, [None, None, None]),
    (3, [[0, 1]], 0, [None, 0, None]),
    (3, [[0, 1]], 1, [1, None, None]),
    (3, [[0, 1], [1, 2]], 1, [1, None, 1]),
    (3, [[0, 1], [1, 2]], 0, [None, 0, 1]),
    (3, [[0, 1], [1, 2]], 2, [1, 2, None]),
    (3, [[1, 2]], 1, [None, None, 1]),
    (3, [[1, 2]], 2, [None, 2, None]),
])
def test_parent_bfs_adjacency_list(num_vertices, edges_list, start_vertice,
                                     parent_list):
    graph = DigraphList(num_vertices)
    length_list = len(edges_list)
    if length_list > 0:
        for x, y in edges_list:
            graph.add_edge(x, y)
    bfs = BreadthFirstSearch(graph, start_vertice)
    parent_bfs = bfs.parent_vertice
    assert parent_bfs == parent_list

@pytest.mark.parametrize("num_vertices,edges_list,start_vertice,parent_list",[
    (1, [], 0, [None]),
    (1, [[0, 0]], 0, [None]),

    (2, [], 0, [None, None]),
    (2, [], 1, [None, None]),
    (2, [[0, 0], [1, 1]], 1, [None, None]),
    (2, [[0, 0], [1, 1]], 0, [None, None]),
    (2, [[0, 0], [0, 1], [1, 1]], 1, [1, None]),
    (2, [[0, 0], [0, 1], [1, 1]], 0, [None, 0]),
    (2, [[0, 1]], 1, [1, None]),
    (2, [[0, 1]], 0, [None, 0]),

    (3, [], 0, [None, None, None]),
    (3, [], 1, [None, None, None]),
    (3, [], 2, [None, None, None]),
    (3, [[0, 1]], 2, [None, None, None]),
    (3, [[0, 1]], 0, [None, 0, None]),
    (3, [[0, 1]], 1, [1, None, None]),
    (3, [[0, 1], [1, 2]], 1, [1, None, 1]),
    (3, [[0, 1], [1, 2]], 0, [None, 0, 1]),
    (3, [[0, 1], [1, 2]], 2, [1, 2, None]),
    (3, [[1, 2]], 1, [None, None, 1]),
    (3, [[1, 2]], 2, [None, 2, None]),
])
def test_parent_bfs_matrix(num_vertices, edges_list, start_vertice,
                                   parent_list):
    graph = DigraphMatrix(num_vertices)
    length_list = len(edges_list)
    if length_list > 0:
        for x, y in edges_list:
            graph.add_edge(x, y)
    bfs = BreadthFirstSearch(graph, start_vertice)
    parent_bfs = bfs.parent_vertice
    assert parent_bfs == parent_list
