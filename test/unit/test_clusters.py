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
        expected = uf.find("a")
        actual = uf.find("c")
        self.assertEqual(actual, expected)
