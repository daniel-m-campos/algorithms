from collections import defaultdict
from itertools import chain
from typing import List, Tuple, Dict, Set


def get_tuples(filename: str) -> List[Tuple]:
    with open(filename) as filename:
        return [tuple(int(i) for i in line.split()) for line in filename]


def get_array(filename: str) -> List[int]:
    with open(filename) as filename:
        return [int(integer) for integer in filename]


def read_edges(filename: str) -> [List[Tuple], int]:
    edges = []
    with open(filename) as file:
        num = int(next(file))
        for line in file:
            edges.append(tuple(int(l) for l in line.strip().split()))
    return edges, num


def get_jobs(filename: str) -> List[Tuple]:
    jobs, num_jobs = read_edges(filename)
    assert len(jobs) == num_jobs, f"Length of jobs is not {num_jobs}"
    return jobs


def get_edges_with_costs(filename: str) -> List[Tuple]:
    edges, num_nodes = read_edges(filename)
    nodes = set(chain.from_iterable(e[:2] for e in edges))
    assert len(nodes) == num_nodes, f"Length of nodes is not {num_nodes}"
    return edges


def to_graph(edges: List[Tuple]) -> [Set, Dict, Dict]:
    nodes = set()
    graph = defaultdict(list)
    distances = {}
    for u, v, d in edges:
        graph[v].append(u)
        distances[u, v] = d
        for node in (u, v):
            nodes.add(node)
    return nodes, graph, distances


def get_graph(filename, directed=False, offset=0):
    graph = defaultdict(list)
    distances = {}
    nodes = set()
    with open(filename) as file:
        num_nodes, num_edges = tuple(int(l) for l in next(file).strip().split())
        for line in file:
            u, v, d = (int(l) for l in line.strip().split())
            u, v = u - offset, v - offset
            graph[u].append(v)
            distances[u, v] = d
            if not directed:
                graph[v].append(u)
                distances[v, u] = d
            for node in (u, v):
                nodes.add(node)
    assert len(nodes) == num_nodes, f"Number of nodes is not {num_nodes}"
    num_distances = num_edges if directed else 2 * num_edges
    assert (
        len(distances) == num_distances
    ), f"Number of distances is not {num_distances}"
    return nodes, graph, distances
