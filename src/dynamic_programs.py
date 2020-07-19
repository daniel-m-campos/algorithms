from typing import List


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
            vertices.append(i+1)
            i -= 2
    if i < 2:
        vertices.append(i+1)
    return max_weight, sorted(vertices)
