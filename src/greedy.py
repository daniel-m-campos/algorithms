import itertools


def schedule(jobs, mode):
    if "diff" in mode:
        key = lambda wl: (wl[0] - wl[1], wl[0])
    elif "ratio" in mode:
        key = lambda wl: (wl[0] / wl[1], wl[0])
    else:
        raise NotImplementedError
    return sorted(jobs, key=key, reverse=True)


def completion_time(schedule):
    completion_times = itertools.accumulate(length for _, length in schedule)
    weights = (weight for weight, _ in schedule)
    return sum(w * t for w, t in zip(weights, completion_times))
