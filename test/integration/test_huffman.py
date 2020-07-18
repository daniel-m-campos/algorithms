from unittest import TestCase

import huffman
from test.integration import util


class TestHuffman(TestCase):
    def test_huffman_10_40_input(self):
        array = util.get_array("../../../huffman_10_40_input.txt")
        weights = {str(k): w for k, w in enumerate(array[1:])}
        code = huffman.code(weights)
        lengths = huffman.lengths(code)
        assert min(lengths) == 4
        assert max(lengths) == 9
