from collections import defaultdict, Counter
import math
import sys

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


def depth_first_search2(graph, increment_finish_time=True):
    time = 1
    visited = {}
    start_time = {}
    finish_time = {}
    for node in graph:
        visited[node] = False
        start_time[node] = math.inf

    for node in graph:
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
    result = {
        n: {
            "visited": visited[n],
            "start_time": start_time[n],
            "finish_time": finish_time[n],
        }
        for n in graph
    }
    topological_sort = list(finish_time.keys())[::-1]
    return {**result, "topological_sort": topological_sort}


def find_scc(graph):
    result = depth_first_search2(graph)
    t_graph = transpose(graph)
    sorted_t_graph = {i: t_graph[i] for i in result["topological_sort"]}
    result2 = depth_first_search2(sorted_t_graph, increment_finish_time=False)
    del result2["topological_sort"]
    return Counter((node["finish_time"] for node in result2.values()))


def sorted_scc(scc_result):
    return sorted(scc_result.values(), reverse=True)


# def find_scc_old(graph):
#     n = len(graph)
#     t_graph = transpose(graph)
#     rt_graph = reverse(t_graph)
#     rev_result = depth_first_search2(rt_graph)
#     finish_times = {
#         i: rev_result[i]["finish_time"]
#         for i in range(1, n + 1)
#     }
#     sorted_graph = {
#         finish_times[node]: [finish_times[e] for e in adjs]
#         for node, adjs in graph.items()
#     }
#     graph_t = transpose(sorted_graph)
#     result = depth_first_search2(reverse(graph_t))
#     return Counter((node['start_time'] for node in result.values()))


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
