import dynamic_programs


def test_four_vertex_example():
    max_weight, vertices = dynamic_programs.mwis(weights=[1, 4, 5, 4])
    assert max_weight == 8
    assert vertices == [1, 3]
