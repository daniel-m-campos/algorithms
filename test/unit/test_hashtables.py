from unittest import TestCase

import hashtables


class TestHashTables(TestCase):
    def check(self, values, t, expected, fcn):
        actual = fcn(values, *t)
        self.assertEqual(expected, actual)

    def test_brute_case_1(self):
        self.check(
            values=[-3, -1, 1, 2, 9, 11, 7, 6, 2],
            t=(3, 10),
            expected=8,
            fcn=hashtables.brute_count_pairs,
        )

    def test_brute_case_2(self):
        self.check(
            values=[-2, 0, 0, 4], t=(0, 4), expected=2, fcn=hashtables.brute_count_pairs
        )

    def test_fast_case_1(self):
        self.check(
            values=[-3, -1, 1, 2, 9, 11, 7, 6, 2],
            t=(3, 10),
            expected=8,
            fcn=hashtables.bisect_count_pairs,
        )

    def test_fast_case_2(self):
        self.check(
            values=[-2, 0, 0, 4],
            t=(0, 4),
            expected=2,
            fcn=hashtables.bisect_count_pairs,
        )
