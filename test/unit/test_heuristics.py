import dynamic_programs as dp
import heuristics as hs


def test_tsp():
    """
    Shortest Path: 1 3 2 5 6 4 1
    """
    coordinates = [
        dp.Coordinate(*x) for x in [(2, 1), (4, 0), (2, 0), (0, 0), (4, 3), (0, 3)]
    ]
    actual = hs.tsp(coordinates)
    assert round(actual, 4) == 15.2361
