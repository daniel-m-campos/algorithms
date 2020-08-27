import pytest

import local_search as ls


@pytest.mark.parametrize(
    "constraint, solution, expected",
    [
        ((1, 3), [True, False, True, False], True),
        ((4, -1), [True, False, False, False], False),
    ],
)
def test_is_satisfied(constraint, solution, expected):
    actual = ls.is_satisfied(constraint, solution)
    assert actual == expected


@pytest.mark.parametrize(
    "constraints, solution, expected",
    [
        ([(1, 3), (-1, 4), (-3, 4), (4, -1)], [True, True, True, True], True),
        ([(1, 3), (-1, 4), (-3, 4), (4, -1)], [False, True, False, True], False),
    ],
)
def test_all_satisfied(constraints, solution, expected):
    actual = ls.all_satisfied(constraints, solution)
    assert actual == expected


@pytest.mark.parametrize(
    "num_variables, constraints, expected",
    [
        (2, [(1, 2), (-1, -2)], {1: {-2}, -1: {2}, -2: {1}, 2: {-1}}),
        (
            4,
            [(1, 3), (-1, 4), (-3, 4), (4, -1)],
            {
                -4: {-1, -3},
                -3: {1},
                -2: set(),
                -1: {3},
                1: {4},
                2: set(),
                3: {4},
                4: set(),
            },
        ),
    ],
)
def test_create_graph(num_variables, constraints, expected):
    actual = ls.implication_graph(num_variables, constraints)
    assert actual == expected


@pytest.mark.parametrize(
    "num_variables, constraints, expected",
    [
        (2, [(1, 2), (-1, 2), (-1, -2)], True),
        (2, [(1, 2), (-1, 2), (1, -2), (-1, -2)], False),
        (4, [(1, 3), (-1, 4), (-3, 4), (4, -1)], True),
        (4, [(-3, 4), (2, 2), (-2, -2), (-4, -1)], False),
    ],
)
def test_two_sat_solver(num_variables, constraints, expected):
    actual = ls.two_sat_solver(num_variables, constraints)
    assert actual == expected
