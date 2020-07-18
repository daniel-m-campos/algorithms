import huffman


def test_four_symbols():
    weights = {"A": 60, "B": 25, "C": 10, "D": 5}
    expected = {"A": "0", "B": "10", "C": "110", "D": "111"}
    code = huffman.code(weights)
    actual = huffman.as_dict(code)
    assert actual == expected
