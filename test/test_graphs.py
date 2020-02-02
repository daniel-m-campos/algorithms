from unittest import TestCase

import graphs


class TestGraphs(TestCase):
    def test_morning_topological_sort(self):
        plan = {
            7: [6, 8],
            3: [],
            4: [2, 5],
            1: [2],
            2: [],
            5: [2, 6],
            6: [9],
            8: [9],
            9: [],
        }
        result = graphs.depth_first_search2(plan)
        actual = result["topological_sort"]
        expected = [1, 4, 5, 2, 3, 7, 6, 8, 9]
        self.assertListEqual(actual, expected)
