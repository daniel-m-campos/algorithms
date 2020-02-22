from unittest import TestCase

import quicksort as qs

BIG_ARRAY_LEN = 10_000


def get_big_array(file="../../../QuickSort.txt"):
    with open(file) as file:
        array = [int(integer) for integer in file.readlines()]
    return array


class TestBigQuickSort(TestCase):
    big_array = get_big_array()
    sorted_big_array = sorted(big_array)

    def test_size(self):
        self.assertEqual(len(self.big_array), BIG_ARRAY_LEN)

    def big_partition_exam(self, partition_fn):
        counts = [0]
        array = self.big_array.copy()
        qs.quick_sort(array, 0, BIG_ARRAY_LEN - 1, partition_fn, counts)
        self.assertListEqual(array, self.sorted_big_array)
        print(counts[0])

    def test_partition_first(self):
        self.big_partition_exam(qs.partition_first)

    def test_partition_last(self):
        self.big_partition_exam(qs.partition_last)

    def test_partition_median(self):
        self.big_partition_exam(qs.partition_median)
