from typing import List, Tuple, Dict, Set

import graphs as gs


def is_satisfied(constraint: Tuple[int, int], solution: List[bool]) -> bool:
    check = False
    for literal in constraint:
        check |= solution[literal - 1] if literal > 0 else not solution[-literal - 1]
    return check


def all_satisfied(constraints: List[Tuple[int, int]], solution: List[bool]) -> bool:
    return all(is_satisfied(c, solution) for c in constraints)


def implication_graph(
    num_variables: int, constraints: List[Tuple[int, int]]
) -> Dict[int, Set[int]]:
    """https://en.wikipedia.org/wiki/Implication_graph"""
    graph = {}
    for i in range(1, num_variables + 1):
        graph[i] = set()
        graph[-i] = set()
    for l1, l2 in constraints:
        graph[-l1].add(l2)
        graph[-l2].add(l1)
    return graph


def two_sat_checker(num_variables: int, constraints: List[Tuple[int, int]]):
    """2-Sat SCC algorithm"""
    graph = implication_graph(num_variables, constraints)
    scc = gs.find_scc(graph)
    return not any(k == -v for k, v in scc["leaders"].items())
