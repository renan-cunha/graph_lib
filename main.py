import click
from src.graph_matrix import GraphMatrix
from typing import List
import ast
from src.transitive_closure.transitive_closure import Warshall

@click.command()
@click.option("--num_vertices", "-nv", help="Number of vertices in the graph",
              required=True, type=int)
@click.option("--edges", "-e", help="Edges in the graph, in the format\n"
                                    "'[[vertice1, vertice2, weight],...]' or\n"
                                    "'[[vertice1, vertice2],...]'",
              type=str)
@click.option("--do_warshall/--no_do_warshall", "-w/-no_w", default=False)
@click.option("--topological_sorting/--no_topological_sorting", "-ts/-no_ts",
              default=False)
@click.option("--strong_components/--no_strong_components", "-sc/-no_sc",
              default=False)
@click.option("--dijkstra", "-d", help="Dijkstra algorithm, needs a beginning "
                                       "vertice", default=-1)
def main(num_vertices, edges, do_warshall, topological_sorting,
         strong_components,
         dijkstra):
    graph = GraphMatrix(num_vertices, digraph=True)

    if edges:
        edges = ast.literal_eval(edges)
        graph = add_edges(graph, edges)

    _print_graph(graph)

    if do_warshall:
        warshall = Warshall(graph)
        print(warshall)

    if topological_sorting:



def add_edges(graph: GraphMatrix, edges_list: List[List[int]]) -> GraphMatrix:
    if len(edges_list[0]) == 3:
        for x, y, z in edges_list:
            graph.add_edge(x, y, weight=z)
    else:
        for x, y in edges_list:
            graph.add_edge(x, y)
    return graph


def _print_graph(graph: GraphMatrix) -> None:
    print("Graph:")
    print(graph)
    print("Edge Weight:")
    print(graph.str_weight())


if __name__ == "__main__":
    main()
