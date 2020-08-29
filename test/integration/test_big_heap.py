from algorithms import heaps
from test.integration import util

RESOURCES = util.resource_directory()
BIG_ARRAY_LEN = 10_000


BIG_ARRAY = util.get_array(f"{RESOURCES}/Median.txt")


def test_size():
    assert len(BIG_ARRAY) == BIG_ARRAY_LEN


def test_updates():
    low_heap, high_heap = [], []
    medians = [heaps.median_update(v, low_heap, high_heap) for v in BIG_ARRAY]
    assert len(medians) == BIG_ARRAY_LEN
    print(f"sum(m) % {BIG_ARRAY_LEN} = {sum(medians) % BIG_ARRAY_LEN}")
