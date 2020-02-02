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
        result = graphs.recursive_depth_first_search(plan)
        actual = result["topological_sort"]
        expected = [1, 4, 5, 2, 3, 7, 8, 6, 9]
        self.assertListEqual(actual, expected)


class TestSCC(TestCase):
    def test_1(self):
        test = "1 4,2 8,3 6,4 7,5 2,6 9,7 1,8 5,8 6,9 7,9 3"
        test = graphs.to_graph(test)
        result = graphs.find_scc(test)
        actual = graphs.sorted_scc(result)
        expected = [3, 3, 3]
        self.assertListEqual(actual, expected)

    def test_2(self):
        test = "1 2,2 6,2 3,2 4,3 1,3 4,4 5,5 4,6 5,6 7,7 6,7 8,8 5,8 7"
        test = graphs.to_graph(test)
        result = graphs.find_scc(test)
        actual = graphs.sorted_scc(result)
        expected = [3, 3, 2]
        self.assertListEqual(actual, expected)

    def test_3(self):
        test = "1 2,2 3,3 1,3 4,5 4,6 4,8 6,6 7,7 8"
        test = graphs.to_graph(test)
        result = graphs.find_scc(test)
        actual = graphs.sorted_scc(result)
        expected = [3, 3, 1, 1]
        self.assertListEqual(actual, expected)

    def test_4(self):
        test = "1 2,2 3,3 1,3 4,4 3,4 6,5 4,6 4,8 6,6 7,7 8"
        test = graphs.to_graph(test)
        result = graphs.find_scc(test)
        actual = graphs.sorted_scc(result)
        expected = [7, 1]
        self.assertListEqual(actual, expected)

    def test_5(self):
        test = "1 2,2 3,2 4,2 5,3 6,4 5,4 7,5 2,5 6,5 7,6 3,6 8,7 8,7 10,8 7,9 7,10 9,10 11,11 12,12 10"
        test = graphs.to_graph(test)
        result = graphs.find_scc(test)
        actual = graphs.sorted_scc(result)
        expected = [6, 3, 2, 1]
        self.assertListEqual(actual, expected)



