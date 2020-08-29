from algorithms import greedy
from test.integration import util

RESOURCES = util.resource_directory()


def test_diff():
    jobs = util.get_jobs(f"{RESOURCES}/jobs.txt")
    schedule = greedy.schedule(jobs, "diff")
    completion_time = greedy.completion_time(schedule)
    print(f"Diff completion time is {completion_time}")


def test_ratio():
    jobs = util.get_jobs(f"{RESOURCES}/jobs.txt")
    schedule = greedy.schedule(jobs, "ratio")
    completion_time = greedy.completion_time(schedule)
    print(f"Ratio completion time is {completion_time}")


def test_data():
    nodes, graph, distances = util.get_graph(f"{RESOURCES}/test_edges.txt")
    assert nodes is not None
    assert graph is not None
    assert distances is not None


def test_small_graph():
    nodes, graph, distances = util.get_graph(f"{RESOURCES}/test_edges.txt")
    mst = greedy.prim(nodes, graph, distances)
    actual = greedy.total_cost(mst, distances)
    expected = 7
    assert actual == expected


def test_big_graph():
    nodes, graph, distances = util.get_graph(f"{RESOURCES}/edges.txt")
    mst = greedy.prim(nodes, graph, distances)
    cost = greedy.total_cost(mst, distances)
    print(f"The MST cost is {cost}")
