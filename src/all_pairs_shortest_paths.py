import math
from typing import List, Tuple, Union, Dict

from dijkstra import shortest_distance_using_heaps
from dynamic_programs import bellman_ford


def johnson(
    graph: Dict[int, List[int]], distances: Dict[Tuple[int, int], float]
) -> Union[Dict[Tuple[int, int], float], str]:
    n = len(graph)
    assert n not in graph
    graph_p = {**graph, **{n: [u for u in graph]}}
    assert len(graph_p) == n + 1
    distances_p = {**distances.copy(), **{(n, u): 0 for u in graph}}

    weights = bellman_ford(n, graph_p, distances_p)
    if isinstance(weights, str):
        return weights

    distances_p = {
        (u, v): d + weights[u] - weights[v] for (u, v), d in distances.items()
    }

    result = {}
    for u in graph:
        for v, d in shortest_distance_using_heaps(u, graph, distances_p).items():
            if u == v or v is None:
                pass
            elif v is not None:
                result[u, v] = d - weights[u] + weights[v]
            else:
                result[u, v] = math.inf
    return result
