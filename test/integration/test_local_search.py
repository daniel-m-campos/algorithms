import pytest

import local_search as ls
from test.integration import util

RESOURCES = util.resource_directory()


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("2sat_false_test.txt", False),
        ("2sat_true_test.txt", True),
        ("2sat1.txt", True),
        ("2sat2.txt", False),
        ("2sat3.txt", True),
        ("2sat4.txt", True),
        ("2sat5.txt", False),
        ("2sat6.txt", False),
    ],
)
def test_two_sat_solver(filename, expected):
    constraints, num_variables = util.read_edges(f"{RESOURCES}/{filename}")
    actual = ls.two_sat_checker(num_variables, constraints)
    assert actual == expected
