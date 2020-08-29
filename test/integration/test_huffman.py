import pytest

from algorithms import huffman
from test.integration import util

RESOURCES = util.resource_directory()


@pytest.mark.parametrize(
    "file, min_length, max_length",
    [
        (f"{RESOURCES}/huffman_10_40_input.txt", 4, 9),
        (f"{RESOURCES}/huffman.txt", 9, 19),
    ],
)
def test_code_lengths(file, min_length, max_length):
    array = util.get_array(file)
    weights = {str(k): w for k, w in enumerate(array[1:])}
    code = huffman.code(weights)
    lengths = huffman.lengths(code)
    assert min(lengths) == min_length
    assert max(lengths) == max_length
