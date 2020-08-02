import heapq
import math
from typing import Dict, List, Tuple


def shortest_distance(
    start: int,
    graph: Dict[int, List[int]],
    distances: Dict[Tuple[int, int], float],
    end: int = None,
) -> Dict[int, float]:
    n = len(graph)
    shortest_distances = {node: 0 if node == start else math.inf for node in graph}
    visited = []
    u = start
    while len(visited) < n:
        visited.append(u)
        edges = (e for e in distances if e[0] in visited and e[1] not in visited)
        found = None
        greedy = math.inf
        for u, v in edges:
            new_distance = shortest_distances[u] + distances[u, v]
            if new_distance < greedy:
                greedy = new_distance
                found = v
        shortest_distances[found] = greedy
        u = found

    return shortest_distances[end] if end else shortest_distances


def remove(heap, lookup, item):
    index = lookup[item]
    heap[index] = heap[-1]
    heap.pop()
    if index < len(heap):
        heapq._siftup(heap, index)
        heapq._siftdown(heap, 0, index)


def shortest_distance_using_heaps(
    start: int,
    graph: Dict[int, List[int]],
    distances: Dict[Tuple[int, int], float],
    end: int = None,
) -> Dict[int, float]:
    shortest_distances = {node: 0 if node == start else math.inf for node in graph}
    heap = [(0, start)]
    visited = set()
    while heap:
        d, u = heapq.heappop(heap)
        visited.add(u)
        for v in graph[u]:
            if v in visited:
                continue
            new_distance = d + distances[u, v]
            if new_distance < shortest_distances[v]:
                shortest_distances[v] = new_distance
                heapq.heappush(heap, (new_distance, v))
    assert len(graph) == len(shortest_distances)
    return shortest_distances[end] if end else shortest_distances
