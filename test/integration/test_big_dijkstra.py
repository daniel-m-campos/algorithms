from collections import defaultdict
from unittest import TestCase

BIG_GRAPH_LEN = 200


def get_data(file="../../../dijkstraData.txt"):
    graph = defaultdict(list)
    distances = {}
    with open(file) as file:
        for line in file.readlines():
            edges = line.split("\t")
            u = int(edges[0])
            for edge in (e for e in edges[1:] if e != "\n"):
                v, d = (int(e) for e in edge.split(","))
                graph[u].append(v)
                distances[u, v] = d
    return graph, distances


class TestBigGraph(TestCase):
    graph, distances = get_data()

    def test_size(self):
        self.assertEqual(len(self.graph), BIG_GRAPH_LEN)

    def test_shortest_paths(self):
        self.assertEqual(len(self.graph), BIG_GRAPH_LEN)