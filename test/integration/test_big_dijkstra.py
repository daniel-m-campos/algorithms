from collections import defaultdict
from unittest import TestCase

from algorithms import dijkstra
from test.integration import util

RESOURCES = util.resource_directory()
BIG_GRAPH_LEN = 200


def get_data(filename):
    graph = defaultdict(list)
    distances = {}
    with open(filename) as file:
        for line in file:
            edges = line.split("\t")
            u = int(edges[0])
            for edge in (e for e in edges[1:] if e != "\n"):
                v, d = (int(e) for e in edge.split(","))
                graph[u].append(v)
                distances[u, v] = d
    return graph, distances


def compute(start, ends, graph, distances):
    shortest_distance = {}
    for node in ends:
        shortest_distance[node] = dijkstra.shortest_distance_using_heaps(
            start, graph, distances, node
        )
    return ",".join(str(v) for v in shortest_distance.values())


class TestBigGraph(TestCase):
    def test_shortest_paths_1(self):
        graph, distances = get_data(f"{RESOURCES}/input_random_2_4.txt")
        ends = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
        start = 1
        actual = compute(start, ends, graph, distances)
        expected = "247,431,362,429,376,382,430,474,430,361"
        self.assertEqual(actual, expected)

    def test_shortest_paths_2(self):
        graph, distances = get_data(f"{RESOURCES}/dijkstraData.txt")
        ends = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
        start = 1
        print(compute(start, ends, graph, distances))
