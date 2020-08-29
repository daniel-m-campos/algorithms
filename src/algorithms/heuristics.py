import math
from typing import List

from algorithms import dynamic_programs as dp


def tsp(coordinates: List[dp.Coordinate]) -> float:
    """
    A heuristic greedy algorithm for approximately solving the Traveling salesman problem
    """

    total_distance = 0
    start = coordinates[0]
    locations = coordinates[1:].copy()
    locations.sort(key=lambda c: c.x)
    route = [start]
    while len(route) < len(coordinates):
        u = route[-1]
        min_distance = math.inf
        head = None
        for v in locations:
            if pow(u.x - v.x, 2) > min_distance:
                break
            distance = dp.squared_distance(u, v)
            if distance < min_distance:
                min_distance = distance
                head = v
        total_distance += math.sqrt(min_distance)
        route.append(head)
        locations.remove(head)

    total_distance += dp.distance(start, route[-1])
    return total_distance
