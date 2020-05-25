from unittest import TestCase

import greedy
from test.integration.util import get_jobs, get_graph


class TestScheduler(TestCase):
    jobs = get_jobs("../../../jobs.txt")

    def test_data(self):
        self.assertIsNotNone(self.jobs)

    def test_diff(self):
        schedule = greedy.schedule(self.jobs, "diff")
        completion_time = greedy.completion_time(schedule)
        print(f"Diff completion time is {completion_time}")

    def test_ratio(self):
        schedule = greedy.schedule(self.jobs, "ratio")
        completion_time = greedy.completion_time(schedule)
        print(f"Ratio completion time is {completion_time}")


class TestPrim(TestCase):
    def test_data(self):
        nodes, graph, distances = get_graph("../../../test_edges.txt")
        self.assertIsNotNone(nodes)
        self.assertIsNotNone(graph)
        self.assertIsNotNone(distances)

    def test_small_graph(self):
        nodes, graph, distances = get_graph("../../../test_edges.txt")
        mst = greedy.prim(nodes, graph, distances)
        actual = greedy.total_cost(mst, distances)
        expected = 7
        self.assertEqual(actual, expected)

    def test_big_graph(self):
        nodes, graph, distances = get_graph("../../../edges.txt")
        mst = greedy.prim(nodes, graph, distances)
        cost = greedy.total_cost(mst, distances)
        print(f"The MST cost is {cost}")
