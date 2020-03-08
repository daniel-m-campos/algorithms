from unittest import TestCase


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

    def test_jobs(self):
        self.assertIsNotNone(self.jobs)