import math
import sys
from collections import defaultdict, Counter

sys.setrecursionlimit(10 ** 6)


def transpose(graph):
    rev_graph = {n: [] for n in graph}
    for node, adjs in graph.items():
        for adj in adjs:
            rev_graph[adj].append(node)
    return rev_graph


def sort(graph):
    return {k: graph[k] for k in range(1, len(graph) + 1)}


def reverse(graph):
    return {k: graph[k] for k in range(len(graph), 0, -1)}


def _result(finish_time, graph, start_time, visited, leaders=None):
    result = {
        n: {
            "visited": visited[n],
            "start_time": start_time[n],
            "finish_time": finish_time[n],
        }
        for n in graph
    }
    topological_sort = list(finish_time.keys())
    topological_sort.reverse()
    return {**result, "topological_sort": topological_sort, "leaders": leaders}


def iterative_depth_first_search(graph, increment_finish_time=True, node_order=None):
    time = 1
    visited = {}
    start_time = {}
    finish_time = {}
    for node in graph:
        visited[node] = False
        start_time[node] = math.inf

    nodes = graph if node_order is None else node_order
    for node in nodes:
        stack = [node]
        while stack:
            u = stack.pop()
            if not visited[u]:
                stack.append(u)
                visited[u] = True
                start_time[u] = time
                for v in graph[u]:
                    stack.append(v)
                time += 1
            elif u not in finish_time:
                finish_time[u] = time
                if increment_finish_time:
                    time += 1

    return _result(finish_time, graph, start_time, visited)


def recursive_depth_first_search(graph, node_order=None):
    def visit(node, leader):
        nonlocal start_time
        nonlocal finish_time
        visited[node] = True
        leaders[node] = leader
        start_time += 1
        start_times[node] = start_time
        for adjacent in graph[node]:
            if not visited[adjacent]:
                visit(adjacent, leader)
        finish_time += 1
        finish_times[node] = finish_time

    start_time = 0
    finish_time = 0
    visited = {}
    start_times = {}
    finish_times = {}
    leaders = {}
    for node in graph:
        visited[node] = False
        start_times[node] = math.inf

    nodes = graph if node_order is None else node_order
    for node in nodes:
        if not visited[node]:
            visit(node, node)

    return _result(finish_times, graph, start_times, visited, leaders)


def find_scc(graph, t_graph=None):
    if t_graph is None:
        t_graph = transpose(graph)
    result = recursive_depth_first_search(t_graph)
    order = result["topological_sort"]
    result2 = recursive_depth_first_search(graph, node_order=order)
    return Counter(result2["leaders"].values())


def sorted_scc(scc_result):
    return sorted(scc_result.values(), reverse=True)


def to_graph(text, delimiter=","):
    edges = (t for t in text.split(delimiter) if t != "")
    edges = (e.split(" ") for e in edges)
    edges = ((int(e[0]), int(e[1])) for e in edges)
    graph = defaultdict(list)
    size = 0
    for u, v in edges:
        graph[u].append(v)
        size = max(size, u, v)
    if len(graph) < size:
        for i in range(1, size + 1):
            if i not in graph:
                graph[i] = []
    return graph
