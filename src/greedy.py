import heapq
import itertools
from collections import defaultdict

from typing import Set, Dict, Tuple


def schedule(jobs, mode):
    if "diff" in mode:
        key = lambda wl: (wl[0] - wl[1], wl[0])
    elif "ratio" in mode:
        key = lambda wl: (wl[0] / wl[1], wl[0])
    else:
        raise NotImplementedError
    return sorted(jobs, key=key, reverse=True)


def completion_time(schedule):
    completion_times = itertools.accumulate(length for _, length in schedule)
    weights = (weight for weight, _ in schedule)
    return sum(w * t for w, t in zip(weights, completion_times))


def prim(nodes: Set, graph: Dict, distances: Dict):
    mst = defaultdict(set)
    start_node = next(iter(nodes))
    visited = {start_node}

    edges = [(distances[start_node, v], start_node, v) for v in graph[start_node]]
    heapq.heapify(edges)

    while edges:
        cost, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        mst[u].add(v)
        for w in graph[v]:
            if w not in visited:
                heapq.heappush(edges, (distances[v, w], v, w))

    return mst


def total_cost(tree: Dict, distances: Dict[Tuple[int, int], int]):
    return sum(distances[u, v] for u in tree for v in tree[u])
