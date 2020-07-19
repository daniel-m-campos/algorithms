import pytest

from dynamic_programs import mwis
from test.integration import util


@pytest.mark.parametrize(
    "file, expected",
    [("../../../mwis_16_80.txt", "10100000"), ("../../../mwis.txt", "10100110")],
)
def test_vertex_in_mwis(file, expected):
    array = util.get_array(file)
    selected = [1, 2, 3, 4, 17, 117, 517, 997]
    max_weight, vertices = mwis(array[1:])
    check = [str(int(s in vertices)) for s in selected]
    actual = "".join(check)
    print(actual)
    assert actual == expected
