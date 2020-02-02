from unittest import TestCase

import graphs

BIG_GRAPH_SIZE = 875714


def get_big_graph(file="../../SCC.txt"):
    big_graph = {}
    for i in range(1, BIG_GRAPH_SIZE + 1):
        big_graph[i] = []
    with open(file) as file:
        for line in file.readlines():
            edge = line.split(" ")
            big_graph[int(edge[0])].append(int(edge[1]))
    return big_graph


class TestBigGraph(TestCase):
    big_graph = get_big_graph()

    def test_size(self):
        self.assertEqual(len(self.big_graph), BIG_GRAPH_SIZE)

    def test_big_scc(self):
        scc = graphs.find_scc(self.big_graph)
        print(scc.most_common(5))
