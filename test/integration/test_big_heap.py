from unittest import TestCase

import heaps
from . import util

BIG_ARRAY_LEN = 10_000


class TestBigHeap(TestCase):
    big_array = util.get_big_array("../../../Median.txt")

    def test_size(self):
        self.assertEqual(len(self.big_array), BIG_ARRAY_LEN)

    def test_updates(self):
        low_heap, high_heap = [], []
        medians = [heaps.median_update(v, low_heap, high_heap) for v in self.big_array]
        self.assertEqual(len(medians), BIG_ARRAY_LEN)
        print(f"sum(m) % {BIG_ARRAY_LEN} = {sum(medians) % BIG_ARRAY_LEN}")
