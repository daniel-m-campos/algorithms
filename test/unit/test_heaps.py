import random

import pytest

from algorithms import heaps


@pytest.mark.parametrize("number", [8, 11])
def test(number):
    expected = (number + 1) / 2 - 1 if number % 2 else number / 2 - 1
    values = list(range(number))
    random.shuffle(values)
    low_heap, high_heap = [], []
    for value in values:
        median = heaps.median_update(value, low_heap, high_heap)
    assert median == expected
