import pytest


from src.graph_matrix import GraphMatrix
from src.transitive_closure.transitive_closure import Warshall


@pytest.mark.parametrize("size, edges, expected", [
    (1, [], [[0]]),
    (1, [[0, 0]], [[1]]),
    (2, [], [[0, 0],
             [0, 0]]),
    (2, [[0, 1]], [[0, 1],
                   [0, 0]]),
    (2, [[0, 1], [1, 1]], [[0, 1],
                           [0, 1]]),
    (2, [[0, 1], [1, 0]], [[1, 1],
                           [1, 1]]),
    (4, [[0, 3], [1, 0], [1, 2], [2, 0], [2, 3], [3, 2]], [[1, 0, 1, 1],
                                                           [1, 0, 1, 1],
                                                           [1, 0, 1, 1],
                                                           [1, 0, 1, 1]]),
])
def test_eval(size, edges, expected):
    graph = GraphMatrix(size, digraph=True)
    for x, y in edges:
        graph.add_edge(x, y)
    warshall = Warshall(graph)
    assert warshall.run() == expected