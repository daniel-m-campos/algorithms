import cProfile
import io
import pstats
from unittest import TestCase

import hashtables
from . import util


class TestBigHastTables(TestCase):
    t = (-10_000, 10_000)

    def check(self, filename, expected, fcn=hashtables.bisect_count_pairs):
        array = util.get_big_array(filename)

        pr = cProfile.Profile()
        pr.enable()

        actual = fcn(array, *self.t)

        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
        ps.print_stats()
        print(s.getvalue())
        print(f"The result for {filename} is: {actual}")
        if expected:
            self.assertEqual(expected, actual)

    def test_input_random_10_40(self):
        self.check("../../../input_random_10_40.txt", 11)

    def test_input_random_2_10(self):
        self.check("../../../input_random_2_10.txt", 1)

    def test_input_random_23_320(self):
        self.check("../../../input_random_23_320.txt", 28)

    def test_input_random_34_2560(self):
        self.check("../../../input_random_34_2560.txt", 74)

    def test_input_random_43_10000(self):
        self.check("../../../input_random_43_10000.txt", 148)

    def test_one_million(self):
        self.check("../../../algo1-programming_prob-2sum.txt", 427)
