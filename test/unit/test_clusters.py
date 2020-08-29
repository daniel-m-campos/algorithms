from algorithms import clusters


def test_initialized_find():
    items = "a b c".split()
    uf = clusters.UnionFind(items)
    for expected, item in enumerate(items):
        actual = uf.find(item)
        assert actual == expected


def test_union():
    items = "a b c".split()
    uf = clusters.UnionFind(items)
    uf.union("a", "c")
    expected = [0, 1, 0]
    actual = uf._parents
    assert actual == expected


def test_groups():
    items = "a b c d e".split()
    uf = clusters.UnionFind(items)
    uf.union("a", "b")
    uf.union("d", "e")
    actual = uf.groups()
    expected = {0: ["a", "b"], 1: ["c"], 2: ["d", "e"]}
    assert actual == expected
