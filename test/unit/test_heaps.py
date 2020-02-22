import random
from unittest import TestCase

import heaps


class TestQuickSort(TestCase):
    def do(self, n):
        expected = (n + 1) / 2 - 1 if n % 2 else n / 2 - 1
        values = list(range(n))
        random.shuffle(values)
        low_heap, high_heap = [], []
        for value in values:
            median = heaps.median_update(value, low_heap, high_heap)
        self.assertEqual(median, expected)

    def test_median_even(self):
        self.do(n=8)

    def test_median_odd(self):
        self.do(n=11)
