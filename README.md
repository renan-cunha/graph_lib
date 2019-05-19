### A basic python lib for non-directed graphs


Pre-requisites: python 3.6.7+

#### To-do

1. Make UML class diagram

#### Requirements

1. make function below 
    ```python
    create_graph(num_vertices: int, is_digraph: bool, is_matrix) returns Graph
    ```
2. GraphClass
    1. add_edge
    2. return number of vertices
    3. return number of edges
    4. number of loops of the graph
    
3. DigraphClass
    1. return the vertices that go to a specific vertice
    2. return the vertices that can be acessed direct from a vertice
    3. return the out and in degree of a vertice
    5. return the max in and out degree of a graph

4. Non Directed Graph Class
    1. return the adjacent vertices
    2. return the degree of a vertice
    3. return the max degree of a vertice

5. Both Digraph and Graph can have the following data structure
    1. AdjacencyList
    2. Matrix

5. Euler Static Class for Non Directed Graph Class
    1. has open euler path method
    2. has closes euler path method
    
6. BFS class
    1. has color
    2. has parent vector
    3. has time vector

7. DFS class
    1. has color
    2. has parent vector
    3. has time vector

8. ConnectedComponentsClass
    1. Use DFS

9. Make Transitive Closude for Digraphs with Matrixes
    1. Boolean Matrixes
    2. Warshall 


