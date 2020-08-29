from collections import defaultdict
from typing import Collection, Set, Dict, Tuple, List


class UnionFind:
    def __init__(self, items: Collection):
        super().__init__()
        num_items = len(items)
        self._items = {item: i for i, item in enumerate(items)}
        self._parents = list(range(num_items))
        self._sizes = [1] * num_items

    def find(self, item) -> int:
        index = self._items[item]
        while index != self._parents[index]:
            index = self._parents[index]
        return index

    def union(self, item_1, item_2):
        parent_1 = self.find(item_1)
        parent_2 = self.find(item_2)
        if self._sizes[parent_1] >= self._sizes[parent_2]:
            parent, child = parent_1, parent_2
        else:
            parent, child = parent_2, parent_1
        self._parents[child] = parent
        self._sizes[parent] += self._sizes[child]

    def groups(self) -> Dict[int, List]:
        groups = defaultdict(list)
        for item in self._items:
            groups[self.find(item)].append(item)
        return {i: group for i, group in enumerate(groups.values())}


def kruskal(
    nodes: Set, distances: Dict[Tuple[int, int], int], num_clusters: int = 1,
) -> [List[Tuple[int, int]], Dict[int, List]]:
    spanning_edges = []
    uf = UnionFind(nodes)
    edges = sorted(distances.keys(), key=lambda x: distances[x], reverse=True)
    while len(spanning_edges) < len(nodes) - num_clusters:
        u, v = edges.pop()
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            spanning_edges.append((u, v))
    if num_clusters == 1:
        return spanning_edges
    next_edge = None
    while edges and next_edge is None:
        u, v = edges.pop()
        if uf.find(u) != uf.find(v):
            next_edge = u, v
    return spanning_edges, distances[next_edge]


def total_cost(edges: List[Tuple[int, int]], distances: Dict[Tuple[int, int], int]):
    return sum(distances[e] for e in edges)
