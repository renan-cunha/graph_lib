@pytest.mark.parametrize("edges,size,expected", [
    ([], 1, True),
    ([[0, 0]], 1, True),
    ([], 2, True),
    ([[0, 1]], 2, False),
    ([[0, 0]], 2, True),
    ([[0, 0], [1,1]], 2, False),
    ([], 3, True),
    ([[2, 2]], 3, True),
    ([[2, 2], [1, 2]], 3, False),
    ([[0, 1], [1, 2], [0, 2]], 3, True),
    ([[1, 2], [2, 0]], 3, False),

])
def test_euler_graph(edges, size, expected):
    graph = NonDigraphMatrix(size)
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
    ([], 3, False),
    ([[2, 2]], 3, False),
    ([[2, 2], [1, 2]], 3, True),
    ([[0, 1], [1, 2], [0, 2]], 3, False),
    ([[1, 2], [2, 0]], 3, True),

])
def test_euler_path(edges, size, expected):
    graph = NonDigraphMatrix(size)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    assert graph.has_open_euler_path() == expected