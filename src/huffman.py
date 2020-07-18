import heapq
from typing import Dict, Tuple, Union


def code(weights: Dict[str, int]) -> Dict[str, int]:
    heap = [(weight, symbol) for symbol, weight in weights.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        w1, s1 = heapq.heappop(heap)
        w2, s2 = heapq.heappop(heap)
        heapq.heappush(heap, (w1 + w2, (s2, s1)))
    tree = heap[0][1]
    code = {}
    fill(code, tree)
    return code


def fill(code: Dict, tree: Union[str, Tuple[str, Tuple]], position: int = 0):
    if len(tree) == 1:
        code[tree] = position
    elif len(tree) == 2:
        position *= 10
        fill(code, tree[0], position + 0)
        fill(code, tree[1], position + 1)
    else:
        raise ValueError("Tree must be nested binary tuples")
