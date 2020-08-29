import cProfile
import io
import pstats

import pytest

from algorithms import hashtables
from test.integration import util

RESOURCES = util.resource_directory()


@pytest.mark.parametrize(
    "filename, expected",
    [
        (f"{RESOURCES}/input_random_10_40.txt", 11),
        (f"{RESOURCES}/input_random_2_10.txt", 1),
        (f"{RESOURCES}/input_random_23_320.txt", 28),
        (f"{RESOURCES}/input_random_34_2560.txt", 74),
        (f"{RESOURCES}/input_random_43_10000.txt", 148),
        (f"{RESOURCES}/algo1-programming_prob-2sum.txt", 427),
    ],
)
def test(filename, expected):
    array = util.get_array(filename)

    pr = cProfile.Profile()
    pr.enable()

    actual = hashtables.bisect_count_pairs(array, -10_000, 10_000)

    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    ps.print_stats()
    print(s.getvalue())
    print(f"The result for {filename} is: {actual}")
    if expected:
        assert actual == expected
