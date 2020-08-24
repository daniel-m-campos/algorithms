import math
import sys
from collections import namedtuple
from functools import lru_cache
from itertools import combinations
from typing import List, Tuple, Union, Dict

import graphs

sys.setrecursionlimit(10 ** 6)


def mwis(weights: List[int]) -> [int, List[int]]:
    """Maximum weighted independent set"""
    n = len(weights)
    solutions = [0] * n
    solutions[0] = weights[0]
    solutions[1] = max(solutions[0], weights[1])
    for i in range(2, n):
        solutions[i] = max(solutions[i - 1], solutions[i - 2] + weights[i])
    max_weight = solutions[-1]
    vertices = []
    i = n - 1
    while i >= 2:
        if solutions[i - 1] >= solutions[i - 2] + weights[i]:
            i -= 1
        else:
            vertices.append(i + 1)
            i -= 2
    if i < 2:
        vertices.append(i + 1)
    return max_weight, sorted(vertices)


def knapsack(capacity: int, items: List[Tuple[int, int]]) -> int:
    n = len(items)
    solns = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i, (value, size) in enumerate(items, start=1):
        for c in range(capacity + 1):
            if size > c:
                solns[i][c] = solns[i - 1][c]
            else:
                solns[i][c] = max(solns[i - 1][c], solns[i - 1][c - size] + value)
    return solns[n][capacity]


class Knapsack:
    def __init__(self) -> None:
        super().__init__()
        self._cache = {}

    def __call__(self, capacity: int, items: List[Tuple[int, int]]) -> int:
        if capacity <= 0:
            return 0

        value, size = items[-1]
        if len(items) == 1:
            return value if size <= capacity else 0

        n_sub_items = len(items[:-1])
        key1 = (n_sub_items, capacity)
        value1 = self._cache.get(key1)
        if value1 is None:
            value1 = self(capacity, items[:-1])
            self._cache[key1] = value1

        key2 = (n_sub_items, capacity - size)
        value2 = self._cache.get(key2)
        if value2 is None:
            if size <= capacity:
                value2 = self(capacity - size, items[:-1])
                self._cache[key2] = value2
            else:
                return value1

        return max(value1, value2 + value)


def bellman_ford(
    start: int, graph: Dict[int, List[int]], distances: Dict[Tuple[int, int], float]
) -> Union[List[float], str]:
    n = len(graph)
    t_graph = graphs.transpose(graph)
    solutions = [[math.inf] * n for _ in range(n + 1)]
    solutions[0][start] = 0
    for i in range(1, n + 1):
        stable = True
        for v in graph:
            if not t_graph[v]:
                solutions[i][v] = solutions[i - 1][v]
            else:
                solutions[i][v] = min(
                    solutions[i - 1][v],
                    min(solutions[i - 1][w] + distances[w, v] for w in t_graph[v]),
                )
            if solutions[i][v] != solutions[i - 1][v]:
                stable = False
        if stable:
            return solutions[i - 1]
    return "negative cycle"


Coordinate = namedtuple("Coordinate", ["x", "y"])


def squared_distance(c1: Coordinate, c2: Coordinate):
    return sum(pow(x[0] - x[1], 2) for x in zip(c1, c2))


@lru_cache()
def distance(c1: Coordinate, c2: Coordinate):
    return math.sqrt(squared_distance(c1, c2))


def encode(n: int, subset: List[int]):
    bit_array = [0] * n
    for i in subset:
        bit_array[i] = 1
    return int("".join(str(i) for i in bit_array), base=2)


def subset_index(n: int, subset: List[int]):
    return encode(n - 1, [j - 1 for j in subset]) - 1


def tsp(coordinates: List[Coordinate]):
    """
    The Bellman-Held-Karp algorithm for solving the Traveling salesman problem
    in O(n^2 2^n) time
    """

    n = len(coordinates)
    solutions = [[0] * (n - 1) for _ in range(pow(2, n - 1) - 1)]
    c1 = coordinates[0]
    indexes = list(range(n))
    for j, adjacent in enumerate(coordinates[1:]):
        s = subset_index(n, [j + 1])
        solutions[s][j] = distance(c1, adjacent)
    for s_size in range(2, n):
        for subset in combinations(indexes[1:], s_size):
            s = subset_index(n, subset)
            for j_index, j in enumerate(subset):
                subset_minus_j = subset[:j_index] + subset[j_index + 1 :]
                s_j = subset_index(n, subset_minus_j)
                solutions[s][j - 1] = min(
                    solutions[s_j][k - 1] + distance(coordinates[k], coordinates[j])
                    for k in subset_minus_j
                )
    s = subset_index(n, indexes)
    return min(
        solutions[s][j] + distance(cj, c1) for j, cj in enumerate(coordinates[1:])
    )
