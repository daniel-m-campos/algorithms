import threading

from algorithms import graphs
from test.integration import util

threading.stack_size(67108864)

RESOURCES = util.resource_directory()
BIG_GRAPH_SIZE = 875714


def get_big_graph(file=f"{RESOURCES}/SCC.txt"):
    big_graph = {i: [] for i in range(1, BIG_GRAPH_SIZE + 1)}
    t_big_graph = {i: [] for i in range(1, BIG_GRAPH_SIZE + 1)}
    with open(file) as file:
        for line in file:
            edge = line.split()
            big_graph[int(edge[0])].append(int(edge[1]))
            t_big_graph[int(edge[1])].append(int(edge[0]))
    return big_graph, t_big_graph


BIG_GRAPH, T_BIG_GRAPH = get_big_graph()


def test_size():
    assert len(BIG_GRAPH) == BIG_GRAPH_SIZE


def test_big_scc():
    def main():
        scc = graphs.find_scc(BIG_GRAPH, T_BIG_GRAPH)
        scc = graphs.leader_counts(scc)
        top_5 = scc.most_common(5)
        print(top_5)
        print(",".join(str(t[1]) for t in top_5))

    thread = threading.Thread(target=main)
    thread.start()
