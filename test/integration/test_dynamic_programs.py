import pytest

import dynamic_programs as dp
from test.integration import util

RESOURCES = util.resource_directory()


@pytest.mark.parametrize(
    "file, expected",
    [
        (f"{RESOURCES}/mwis_16_80.txt", "10100000"),
        (f"{RESOURCES}/mwis.txt", "10100110"),
    ],
)
def test_vertex_in_mwis(file, expected):
    array = util.get_array(file)
    selected = [1, 2, 3, 4, 17, 117, 517, 997]
    max_weight, vertices = dp.mwis(array[1:])
    check = [str(int(s in vertices)) for s in selected]
    actual = "".join(check)
    print(actual)
    assert actual == expected


@pytest.mark.parametrize(
    "file, expected",
    [
        (f"{RESOURCES}/knapsack_test1.txt", 147),
        (f"{RESOURCES}/knapsack1.txt", 2493893),
        (f"{RESOURCES}/knapsack_big.txt", 4243395),
    ],
)
def test_knapsack(file, expected):
    knapsack_data = util.get_tuples(file)
    size, _ = knapsack_data[0]
    items = knapsack_data[1:]
    knapsack = dp.Knapsack()
    actual = knapsack(size, items)
    assert actual == expected


@pytest.mark.parametrize(
    "file, expected",
    [
        (f"{RESOURCES}/tsp_test.txt", 19.69),
        pytest.param(
            f"{RESOURCES}/tsp.txt", 26442.73, marks=pytest.mark.skip, reason="Too slow"
        ),
    ],
)
def test_tsp(file, expected):
    coordinates = util.get_tuples(file, skip_first=True, num_type=float)
    coordinates = [dp.Coordinate(*x) for x in coordinates]
    actual = dp.tsp(coordinates)
    assert round(actual, 2) == expected
