import pytest

from algorithms.all_pairs_shortest_paths import johnson
from test.integration import util

RESOURCES = util.resource_directory()


@pytest.mark.parametrize(
    "file, expected",
    [
        (f"{RESOURCES}/all_pairs_test_1.txt", "negative cycle"),
        (f"{RESOURCES}/all_pairs_test_2.txt", -2),
        (f"{RESOURCES}/all_pairs_test_g1.txt", "negative cycle"),
        (f"{RESOURCES}/all_pairs_test_g2.txt", "negative cycle"),
        (f"{RESOURCES}/all_pairs_test_g3.txt", -19),
    ],
)
def test_johnson(file, expected):
    _, graph, distances = util.get_graph(file, directed=True, offset=1)
    actual = johnson(graph, distances)
    if isinstance(actual, str):
        assert actual == expected
    else:
        min_distance = min(actual.values())
        assert min_distance == expected
