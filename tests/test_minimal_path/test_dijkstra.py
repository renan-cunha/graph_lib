import pytest
from src.graph_matrix import GraphMatrix
from src.minimal_path.dijkstra import Dijkstra

inf = float("Inf")

@pytest.mark.parametrize("size, edges, start_vertice, expected", [
    (1, [], 0, {0: (0, [0])}),
    (1, [[0, 0, 10]], 0, {0: (0, [0])}),
    (2, [], 0, {0: (0, [0]),
                1: (inf, [None, 1])}),
    (2, [[0, 1, 10]], 0, {0: (0, [0]),
                          1: (10, [0, 1])}),
    (2, [[0, 1, 10]], 1, {0: (inf, [None, 0]),
                          1: (0, [1])}),
    (3, [[0, 1, 10], [0, 2, 5]], 0, {0: (0, [0]),
                                     1: (10, [0, 1]),
                                     2: (5, [0, 2])}),
    (3, [[0, 1, 10], [1, 2, 5]], 0, {0: (0, [0]),
                                     1: (10, [0, 1]),
                                     2: (15, [0, 1, 2])}),
    (3, [[0, 1, 1], [1, 2, 2], [0, 2, 5]], 0, {0: (0, [0]),
                                               1: (1, [0, 1]),
                                               2: (3, [0, 1, 2])}),
    (3, [[0, 1, 10], [1, 2, 5]], 1, {0: (inf, [None, 0]),
                                     1: (0, [1]),
                                     2: (5, [1, 2])}),
    (5, [[0, 1, 10], [0, 2, 5], [1, 4, 1], [1, 2, 2], [2, 3, 2], [2, 4, 9],
         [2, 1, 3], [3, 0, 7], [3, 4, 6], [4, 3, 4]], 0, {0: (0, [0]),
                                                          1: (8, [0, 2, 1]),
                                                          2: (5, [0, 2]),
                                                          3: (7, [0, 2, 3]),
                                                          4: (9, [0, 2, 1, 4])})
])
def test_eval(size, edges, start_vertice, expected):
    graph = GraphMatrix(size, digraph=True)
    for x, y, w in edges:
        graph.add_edge(x, y, weight=w)
    dijkstra = Dijkstra(graph)
    result = dijkstra.run(start_vertice)
    assert result == expected
