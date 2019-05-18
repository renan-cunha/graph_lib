def is_euler_graph(self) -> bool:
    """Returns a boolean variable saying if it's an euler graph

    the input must be conex"""
    for vertice in self.get_vertices():
        if self.degree(vertice) % 2 == 1:
            return False
    return True


def has_open_euler_path(self) -> bool:
    """Returns a boolean variable saying it the graph has an open euler
    path, the input must be conex"""
    count = 0
    for vertice in self.get_vertices():
        count += self.degree(vertice) % 2
    if count == 2:
        return True
    else:
        return False