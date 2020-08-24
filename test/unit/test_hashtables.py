import pytest

import hashtables


@pytest.mark.parametrize(
    "values, lower, upper, fcn, expected",
    [
        ([-3, -1, 1, 2, 9, 11, 7, 6, 2], 3, 10, hashtables.brute_count_pairs, 8),
        ([-3, -1, 1, 2, 9, 11, 7, 6, 2], 3, 10, hashtables.bisect_count_pairs, 8),
        ([-2, 0, 0, 4], 0, 4, hashtables.brute_count_pairs, 2),
        ([-2, 0, 0, 4], 0, 4, hashtables.bisect_count_pairs, 2),
    ],
)
def test(values, lower, upper, fcn, expected):
    actual = fcn(values, lower, upper)
    assert expected == actual
