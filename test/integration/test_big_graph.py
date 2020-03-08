import threading
from unittest import TestCase

import graphs

threading.stack_size(67108864)

BIG_GRAPH_SIZE = 875714


def get_big_graph(file="../../../SCC.txt"):
    big_graph = {i: [] for i in range(1, BIG_GRAPH_SIZE + 1)}
    t_big_graph = {i: [] for i in range(1, BIG_GRAPH_SIZE + 1)}
    with open(file) as file:
        for line in file:
            edge = line.split()
            big_graph[int(edge[0])].append(int(edge[1]))
            t_big_graph[int(edge[1])].append(int(edge[0]))
    return big_graph, t_big_graph


class TestBigGraph(TestCase):
    big_graph, t_big_graph = get_big_graph()

    def test_size(self):
        self.assertEqual(len(self.big_graph), BIG_GRAPH_SIZE)

    def test_big_scc(self):
        def main():
            scc = graphs.find_scc(self.big_graph, self.t_big_graph)
            top_5 = scc.most_common(5)
            print(top_5)
            print(",".join(str(t[1]) for t in top_5))

        thread = threading.Thread(target=main)
        thread.start()
