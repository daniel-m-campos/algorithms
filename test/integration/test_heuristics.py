import pytest

from algorithms import heuristics, dynamic_programs as dp
from test.integration import util

RESOURCES = util.resource_directory()


@pytest.mark.parametrize(
    "file, expected",
    [
        (f"{RESOURCES}/tsp_heuristic_test.txt", 74),
        (f"{RESOURCES}/tsp_heuristic.txt", 1203406),
    ],
)
def test_tsp(file, expected):
    coordinates = util.get_tuples(file, skip_first=True, num_type=float)
    coordinates = [dp.Coordinate(x[1], x[2]) for x in coordinates]
    actual = heuristics.tsp(coordinates)
    assert int(actual) == expected
