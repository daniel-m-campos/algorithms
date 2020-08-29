import random

import pytest

from algorithms import quicksort


@pytest.mark.parametrize(
    "partitioner",
    [quicksort.partition_first, quicksort.partition_last, quicksort.partition_median],
)
def test_partition(partitioner):
    n = 10
    expected = list(range(n))
    actual = expected.copy()
    random.shuffle(actual)
    quicksort.quick_sort(actual, 0, n - 1, partitioner)
    assert actual == expected


def test_counts():
    n = 10
    actual = list(range(n))
    counts = [0]
    quicksort.quick_sort(actual, 0, n - 1, quicksort.partition_first, counts)
    assert counts[0] > 0
    print(counts[0])


def test_median_pivot_even():
    array = [7, 5, 1, 3]
    n = len(array)
    actual = quicksort.get_median_index(array, 0, n - 1)
    expected = 1
    assert expected == actual


def test_median_pivot_odd():
    array = [7, 5, 1, 3, 2]
    n = len(array)
    actual = quicksort.get_median_index(array, 0, n - 1)
    expected = 4
    assert expected == actual
