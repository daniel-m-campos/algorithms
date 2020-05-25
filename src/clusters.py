"""
In this programming problem and the next you'll code up the clustering algorithm from
lecture for computing a max-spacing kk-clustering.

Download the text file below.

clustering1.txt
This file describes a distance function (equivalently, a complete graph with edge
costs). It has the following format:

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...

There is one edge (i,j) for each choice of 1 \leq i \lt j \leq n1≤i<j≤n, where nn
is the number of nodes.

For example, the third line of the file is "1 3 5250", indicating that the distance
between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can assume
that distances are positive, but you should NOT assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on this data
set, where the target number kk of clusters is set to 4. What is the maximum spacing of
a 4-clustering?

ADVICE: If you're not getting the correct answer, try debugging your algorithm using
some small test cases. And then post them to the discussion forum!
"""

from typing import List


class UnionFind:
    def __init__(self, items: List):
        super().__init__()
        num_items = len(items)
        self._items = {item: i for i, item in enumerate(items)}
        self._parents = list(range(num_items))
        self._sizes = [1] * num_items

    def find(self, item):
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
