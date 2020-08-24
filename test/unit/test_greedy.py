import pytest

import greedy


@pytest.mark.parametrize(
    "jobs, modes, expected",
    [
        ([(10, 2), (10, 7), (10, 4)], ("diff", "ratio"), [(10, 2), (10, 4), (10, 7)]),
        ([(2, 1), (7, 1), (4, 1)], ("diff", "ratio"), [(7, 1), (4, 1), (2, 1)]),
        (
            [(1, 2), (2, 3), (7, 4), (10, 4)],
            ("diff", "ratio"),
            [(10, 4), (7, 4), (2, 3), (1, 2)],
        ),
        (
            [(1, 2), (2, 3), (7, 4), (10, 4)],
            ("diff", "ratio"),
            [(10, 4), (7, 4), (2, 3), (1, 2)],
        ),
    ],
)
def test_scheduler(jobs, modes, expected):
    for mode in modes:
        actual = greedy.schedule(jobs, mode)
        assert actual == expected


def test_completion_time():
    schedule = [
        (7, 4),
        (2, 3),
        (1, 2),
    ]
    actual = greedy.completion_time(schedule)
    expected = 4 * 7 + 2 * 7 + 1 * 9
    assert actual == expected
