from typing import List, Tuple


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
