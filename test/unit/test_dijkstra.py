from unittest import TestCase

import dijkstra


class TestDijkstra(TestCase):
    def test_shortest_distance(self):
        graph = {1: [2, 3], 2: [3, 4], 3: [4]}
        distances = {(1, 2): 1, (1, 3): 4, (2, 3): 2, (2, 4): 6, (3, 4): 3}
        actual = dijkstra.shortest_distance(1, 4, graph, distances)
        expected = 6
        self.assertEqual(actual, expected)
