from unittest import TestCase

import clusters


class TestUnionFind(TestCase):
    def test_initialized_find(self):
        items = "a b c".split()
        uf = clusters.UnionFind(items)
        for expected, item in enumerate(items):
            actual = uf.find(item)
            self.assertEqual(actual, expected)

    def test_union(self):
        items = "a b c".split()
        uf = clusters.UnionFind(items)
        uf.union("a", "c")
        expected = [0, 1, 0]
        actual = uf._parents
        self.assertListEqual(actual, expected)

    def test_groups(self):
        items = "a b c d e".split()
        uf = clusters.UnionFind(items)
        uf.union("a", "b")
        uf.union("d", "e")
        actual = uf.groups()
        expected = {0: ["a", "b"], 1: ["c"], 2: ["d", "e"]}
        self.assertDictEqual(actual, expected)
