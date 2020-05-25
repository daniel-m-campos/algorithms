from itertools import chain

def get_big_array(filename):
    with open(filename) as filename:
        array = [int(integer) for integer in filename]
    return array

def read_edges(filename):
    edges = []
    with open(filename) as file:
        num = int(next(file))
        for line in file:
            edges.append(tuple(int(l) for l in line.strip().split()))
    return edges, num

def get_jobs(filename):
    jobs, num_jobs = read_edges(filename)
    assert len(jobs) == num_jobs, f"Length of jobs is not {num_jobs}"
    return jobs


def get_edges_with_costs(filename):
    edges, num_nodes = read_edges(filename)
    nodes = set(chain.from_iterable(e[:2] for e in edges))
    assert len(nodes) == num_nodes, f"Length of nodes is not {num_nodes}"
    return edges