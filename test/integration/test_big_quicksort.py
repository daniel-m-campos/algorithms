import pytest

import quicksort as qs
from test.integration import util

RESOURCES = util.resource_directory()
BIG_ARRAY_LEN = 10_000
BIG_ARRAY = util.get_array(f"{RESOURCES}/QuickSort.txt")
SORTED_BIG_ARRAY = sorted(BIG_ARRAY)


def test_size():
    assert len(BIG_ARRAY) == BIG_ARRAY_LEN


@pytest.mark.parametrize(
    "partition_fn", [qs.partition_first, qs.partition_last, qs.partition_median]
)
def test(partition_fn):
    counts = [0]
    array = BIG_ARRAY.copy()
    qs.quick_sort(array, 0, BIG_ARRAY_LEN - 1, partition_fn, counts)
    assert array == SORTED_BIG_ARRAY
    print(counts[0])
