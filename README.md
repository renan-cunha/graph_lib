## A basic python lib for graphs

[python 3.6.7](https://www.python.org/downloads/release/python-367/)

The algorithms are on `\src`

#####  Install Requirements

```bash
pip3 install -r requirements.txt --user
```

#### Usage
```bash
Usage: main.py [OPTIONS]

Options:
  -nv, --num_vertices INTEGER     Number of vertices in the graph  [required]
  -e, --edges TEXT                Edges in the graph, in the format
                                  '[[vertice1, vertice2, weight],...]' or
                                  '[[vertice1, vertice2],...]'
  -w, --do_warshall / -no_w, --no_do_warshall
  -ts, --topological_sorting / -no_ts, --no_topological_sorting
  -sc, --strong_components / -no_sc, --no_strong_components
  -d, --dijkstra INTEGER          Dijkstra algorithm, needs a beginning
                                  vertice
  --help                          Show this message and exit.

```

#### Examples

An example can be run by

```bash
bash example.sh
```

##### Strong Components
```bash
python3 main.py -nv 3 -e '[[0,1,4],[1,2,5],[1,0,0]]' -sc
```
```bash
Strong Components:
[0, 1]
[2]
```

##### Warshall
```bash
python3 main.py -nv 3 -e '[[0,1,4],[1,2,5],[1,0,0]]' -w
```
```bash
Transitive Closure (Warshall):
V   0  1  2  
0  [1, 1, 1]
1  [1, 1, 1]
2  [0, 0, 0]
```
##### Topological Sorting
```bash
python3 main.py -nv 3 -e '[[0,1,4],[1,2,5]]' -ts
```
```bash
Topological Sorting:
[0, 1, 2]
```

##### Dijkstra 
```bash
python3 main.py -nv 3 -e '[[0,1,4],[1,2,5],[1,0,0]]' -d 0
```

```bash
Dijkstra from 0:
vertice, cost, path
0, 0, [0]
1, 4, [0, 1]
2, 9, [0, 1, 2]

```
