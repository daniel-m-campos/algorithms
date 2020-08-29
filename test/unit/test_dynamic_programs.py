import pytest

from algorithms import dynamic_programs as dp


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


@pytest.mark.parametrize(
    "x, y, distance",
    [
        (3, 4, 5),
        (5, 12, 13),
        (8, 15, 17),
        (7, 24, 25),
        (20, 21, 29),
        (12, 35, 37),
        (9, 40, 41),
        (28, 45, 53),
        (11, 60, 61),
        (16, 63, 65),
        (33, 56, 65),
        (48, 55, 73),
        (13, 84, 85),
        (36, 77, 85),
        (39, 80, 89),
        (65, 72, 97),
    ],
)
def test_distance(x, y, distance):
    c1 = dp.Coordinate(x=0, y=0)
    c2 = dp.Coordinate(x=x, y=y)
    assert dp.distance(c1, c2) == distance


def test_encode():
    actual = dp.encode(n=6, subset=[0, 3, 4])
    assert actual == 38


def test_tsp():
    coordinates = [dp.Coordinate(*x) for x in ((0, 0), (4, 3), (4, 0), (0, 3))]
    actual = dp.tsp(coordinates)
    assert actual == 14.0
