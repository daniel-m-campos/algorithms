import sys
from typing import List, Tuple

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
