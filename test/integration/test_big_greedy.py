from unittest import TestCase

import greedy


def get_jobs(filename):
    jobs = []
    with open(filename) as file:
        num_jobs = int(next(file))
        for line in file:
            jobs.append(tuple(int(l) for l in line.strip().split()))
    assert len(jobs) == num_jobs, f"Length of jobs is not {num_jobs}"
    return jobs

class TestGreedy(TestCase):
    jobs = get_jobs("../../../jobs.txt")

    def test_data(self):
        self.assertIsNotNone(self.jobs)

    def test_diff(self):
        schedule = greedy.schedule(self.jobs, "diff")
        completion_time = greedy.completion_time(schedule)
        print(f"Diff completion time is {completion_time}")


    def test_ratio(self):
        schedule = greedy.schedule(self.jobs, "ratio")
        completion_time = greedy.completion_time(schedule)
        print(f"Ratio completion time is {completion_time}")