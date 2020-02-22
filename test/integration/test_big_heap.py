from unittest import TestCase

import heaps

BIG_ARRAY_LEN = 10_000


def get_big_array(file="../../../Median.txt"):
    with open(file) as file:
        array = [int(integer) for integer in file.readlines()]
    return array


class TestBigHeap(TestCase):
    big_array = get_big_array()

    def test_size(self):
        self.assertEqual(len(self.big_array), BIG_ARRAY_LEN)

    def test_updates(self):
        low_heap, high_heap = [], []
        medians = [heaps.median_update(v, low_heap, high_heap) for v in self.big_array]
        self.assertEqual(len(medians), BIG_ARRAY_LEN)
        print(f"sum(m) % {BIG_ARRAY_LEN} = {sum(medians) % BIG_ARRAY_LEN}")
