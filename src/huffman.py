import heapq
from typing import Dict, Tuple, Union, List


def code(weights: Dict[Union[str, int], int]) -> Union[str, Tuple[str, Tuple]]:
    heap = [(weight, symbol) for symbol, weight in weights.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        w1, s1 = heapq.heappop(heap)
        w2, s2 = heapq.heappop(heap)
        heapq.heappush(heap, (w1 + w2, (s2, s1)))
    return heap[0][1]


def fill(code: Dict, tree: Union[str, Tuple[str, Tuple]], position: str = ""):
    if not isinstance(tree, tuple):
        code[tree] = position
    elif len(tree) == 2:
        fill(code, tree[0], position + "0")
        fill(code, tree[1], position + "1")
    else:
        raise ValueError("Tree must be nested binary tuples")


def as_dict(code: Union[str, Tuple[str, Tuple]]) -> Dict[str, str]:
    d_code = {}
    fill(d_code, code)
    return d_code


def lengths(code: Union[str, Tuple[str, Tuple]]) -> List[int]:
    code_dict = as_dict(code)
    return [len(str(c)) for c in code_dict.values()]
