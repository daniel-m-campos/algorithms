from algorithms.all_pairs_shortest_paths import johnson


def test_johnson_example():
    graph = {0: [1], 1: [2], 2: [0, 3, 4], 3: [], 4: [], 5: [3, 4]}
    distances = {
        (0, 1): -2,
        (1, 2): -1,
        (2, 0): 4,
        (2, 3): 2,
        (2, 4): -3,
        (5, 3): 1,
        (5, 4): -4,
    }
    shortest_paths = johnson(graph, distances)
    assert len(shortest_paths) == 30
