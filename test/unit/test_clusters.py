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
        self.assertEqual(uf.find("a"), uf.find("c"))
        self.assertNotEqual(uf.find("a"), uf.find("b"))
        self.assertNotEqual(uf.find("b"), uf.find("c"))
