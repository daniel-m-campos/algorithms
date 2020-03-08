import random
from unittest import TestCase

import quicksort


class TestQuickSort(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.n = 10
        self.expected = list(range(self.n))
        self.actual = self.expected.copy()
        random.shuffle(self.actual)

    def partition_exam(self, partition_fn):
        quicksort.quick_sort(self.actual, 0, self.n - 1, partition_fn)
        self.assertListEqual(self.actual, self.expected)

    def test_partition_first(self):
        self.partition_exam(quicksort.partition_first)

    def test_partition_last(self):
        self.partition_exam(quicksort.partition_last)

    def test_partition_median(self):
        self.partition_exam(quicksort.partition_median)

    def test_counts(self):
        counts = [0]
        quicksort.quick_sort(
            self.actual, 0, self.n - 1, quicksort.partition_first, counts
        )
        self.assertTrue(counts[0] > 0)
        print(counts[0])

    def test_median_pivot_even(self):
        array = [7, 5, 1, 3]
        n = len(array)
        actual = quicksort.get_median_index(array, 0, n - 1)
        expected = 1
        self.assertEqual(expected, actual)

    def test_median_pivot_odd(self):
        array = [7, 5, 1, 3, 2]
        n = len(array)
        actual = quicksort.get_median_index(array, 0, n - 1)
        expected = 4
        self.assertEqual(expected, actual)
