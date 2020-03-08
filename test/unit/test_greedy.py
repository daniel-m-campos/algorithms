from unittest import TestCase

import greedy


class TestGreedy(TestCase):
    def test_equal_weight_job_schedule(self):
        jobs = [
            (10, 2),
            (10, 7),
            (10, 4),
        ]
        for mode in ("diff", "ratio"):
            actual = greedy.schedule(jobs, mode)
            expected = [
                (10, 2),
                (10, 4),
                (10, 7),
            ]
            self.assertListEqual(actual, expected)

    def test_equal_length_job_schedule(self):
        jobs = [
            (2, 1),
            (7, 1),
            (4, 1),
        ]
        for mode in ("diff", "ratio"):
            actual = greedy.schedule(jobs, mode)
            expected = [
                (7, 1),
                (4, 1),
                (2, 1),
            ]
            self.assertListEqual(actual, expected)

    def test_diff_job_schedule(self):
        jobs = [
            (1, 2),
            (2, 3),
            (7, 4),
            (10, 4),
        ]
        actual = greedy.schedule(jobs, "diff")
        expected = [
            (10, 4),
            (7, 4),
            (2, 3),
            (1, 2),
        ]
        self.assertListEqual(actual, expected)

    def test_ratio_job_schedule(self):
        jobs = [
            (1, 2),
            (2, 3),
            (7, 4),
            (10, 4),
        ]
        actual = greedy.schedule(jobs, "diff")
        expected = [
            (10, 4),
            (7, 4),
            (2, 3),
            (1, 2),
        ]
        self.assertListEqual(actual, expected)

    def test_completion_time(self):
        schedule = [
            (7, 4),
            (2, 3),
            (1, 2),
        ]
        actual = greedy.completion_time(schedule)
        expected = 4 * 7 + 2 * 7 + 1 * 9
        self.assertEqual(actual, expected)