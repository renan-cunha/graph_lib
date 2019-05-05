import pytest
from src.breadth_first_search import BreadthFirstSearch
from src.search_color import Color
from src.graph_adjacency_list import GraphAdjacencyList
from src.graph_matrix import GraphMatrix

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
    graph = GraphAdjacencyList(num_vertices)
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
    graph = GraphMatrix(num_vertices)
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
    graph = GraphAdjacencyList(num_vertices)
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
    graph = GraphMatrix(num_vertices)
    length_list = len(edges_list)
    if length_list > 0:
        for x, y in edges_list:
            graph.add_edge(x, y)
    bfs = BreadthFirstSearch(graph, start_vertice)
    distance_bfs = bfs.dist_from_source
    assert distance_bfs == distance_list
