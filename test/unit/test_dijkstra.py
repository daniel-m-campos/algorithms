from algorithms import dijkstra


def test_shortest_distance():
    graph = {1: [2, 3], 2: [3, 4], 3: [4], 4: []}
    distances = {(1, 2): 1, (1, 3): 4, (2, 3): 2, (2, 4): 6, (3, 4): 3}
    actual = dijkstra.shortest_distance_using_heaps(1, graph, distances)
    assert actual[4] == 6
