import dynamic_programs as dp


def test_four_vertex_mwis():
    max_weight, vertices = dp.mwis(weights=[1, 4, 5, 4])
    assert max_weight == 8
    assert vertices == [2, 4]


def test_four_item_knapsack():
    knapsack = dp.Knapsack()
    actual = knapsack(capacity=6, items=[(3, 4), (2, 3), (4, 2), (4, 3)])
    assert actual == 8


def test_bellman_ford_negative_cycle():
    graph = {0: [1], 1: [2], 2: [3], 3: [4], 4: [1]}
    distances = {(0, 1): 10, (1, 2): -4, (2, 3): 3, (3, 4): -5, (4, 1): 4}
    actual = dp.bellman_ford(0, graph, distances)
    assert actual == "negative cycle"


def test_bellman_ford_shortest_paths():
    graph = {0: [1, 2], 1: [2, 3], 2: [4], 3: [4], 4: []}
    distances = {(0, 1): 2, (0, 2): 4, (1, 2): -1, (1, 3): 2, (3, 4): 2, (2, 4): 4}
    actual = dp.bellman_ford(0, graph, distances)
    assert actual == [0, 2, 1, 4, 5]
