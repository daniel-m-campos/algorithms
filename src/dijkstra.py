import math


def shortest_distance(start, end, graph, distances):
    n = len(graph)
    distance = {node: 0 if node == start else math.inf for node in graph}
    visited = []
    u = start
    while len(visited) < n:
        visited.append(u)
        edges = (e for e in distances if e[0] in visited and e[1] not in visited)
        found = None
        greedy = math.inf
        for u, v in edges:
            new_distance = distance[u] + distances[u, v]
            if new_distance < greedy:
                greedy = new_distance
                found = v
        distance[found] = greedy
        u = found

    return distance[end]
