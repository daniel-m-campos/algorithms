import dynamic_programs as dp


def test_four_vertex_mwis():
    max_weight, vertices = dp.mwis(weights=[1, 4, 5, 4])
    assert max_weight == 8
    assert vertices == [2, 4]


def test_four_item_knapsack():
    actual = dp.knapsack(capacity=6, items=[(3, 4), (2, 3), (4, 2), (4, 3)])
    assert actual == 8
