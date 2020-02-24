from collections import Counter


def count_pairs(array, lower, upper):
    array.sort()
    values = {v: i for i, v in enumerate(array)}
    counter = Counter()
    for x in values:
        l = lower
        while True:
            i = values.get(l - x, None)
            if i is not None or l >= upper:
                break
            else:
                l += 1
        u = upper
        while True:
            j = values.get(u - x, None)
            if j is not None or u <= lower:
                break
            else:
                u -= 1
        if i is None or j is None:
            continue
        for k in range(i, j + 1):
            y = array[k]
            if x != y and lower <= x + y <= upper:
                counter[x + y] += 1
    return len(counter)


def brute_count_pairs(array, lower, upper):
    array.sort()
    counter = Counter()
    for i, x in enumerate(array):
        for y in array[i + 1 :]:
            if x != y and lower <= x + y <= upper:
                counter[x + y] += 1
    return len(counter)


def fast_count_pairs(array, lower, upper):
    array.sort()
    n = len(array)
    values = {v: i for i, v in enumerate(array)}
    ts = []
    for t in range(lower, upper + 1):
        i = 0
        while i < n:
            x = array[i]
            j = values.get(t - x, None)
            if j is not None and x != array[j]:
                ts.append(t)
                break
            else:
                i += 1
    return len(ts)
