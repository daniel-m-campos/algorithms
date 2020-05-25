from unittest import TestCase

from test.integration.util import get_edges_with_costs


class TestCluster(TestCase):
    edges = get_edges_with_costs("../../../test_clustering_1_8.txt")

    def test_data(self):
        self.assertIsNotNone(self.edges)
