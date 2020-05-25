from unittest import TestCase

import clusters
from test.integration.util import get_edges_with_costs, to_graph, get_graph


class TestLoadingData(TestCase):
    edges = get_edges_with_costs("../../../test_clustering_1_8.txt")

    def test_read(self):
        self.assertIsNotNone(self.edges)

    def test_to_graph(self):
        nodes, graph, distances = to_graph(self.edges)
        self.assertIsInstance(nodes, set)
        self.assertIsInstance(graph, dict)
        self.assertIsInstance(distances, dict)
        self.assertTrue(len(nodes) == len(graph))
        self.assertTrue(len(distances) == 2 * len(self.edges))


class TestKruskal(TestCase):
    def test_small_graph(self):
        nodes, _, distances = get_graph("../../../test_edges.txt")
        mst = clusters.kruskal(nodes, distances)
        actual = clusters.total_cost(mst, distances)
        expected = 7
        self.assertEqual(actual, expected)

    def test_big_graph(self):
        nodes, graph, distances = get_graph("../../../edges.txt")
        mst = clusters.kruskal(nodes, distances)
        actual = clusters.total_cost(mst, distances)
        expected = -3612829
        self.assertEqual(actual, expected)
