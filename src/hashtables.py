import bisect
from collections import Counter


def count_pairs(array, lower, upper):
    n = len(array)
    array.sort()
    values = {v: i for i, v in enumerate(array)}
    counter = Counter()
    for x in array:
        if x + x >= upper:
            break
        l, u = lower, upper
        i, j = None, None
        while True:
            j = values.get(u - x, None)
            if j is not None:
                break
            else:
                u -= 1
            if i is not None:
                break
            else:
                l += 1
            i = values.get(l - x, None)
            if l >= u:
                break
        if i is None and j is None:
            continue
        if j is not None:
            k = j
            step = -1
        else:
            k = i
            step = 1
        while 0 <= k < n and lower <= x + array[k] <= upper:
            if x != array[k]:
                counter[x + array[k]] += 1
            k += step
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
    values = {v: i for i, v in enumerate(array)}
    counts = 0
    for t in range(lower, upper + 1):
        for x in array:
            if 2 * x >= t:
                break
            if t - x in values:
                counts += 1
                break

    return counts

def bisect_count_pairs(array, lower, upper):
    array.sort()
    counter = Counter()
    for x in array:
        i = bisect.bisect_left(array, lower - x) - 1
        j = bisect.bisect_left(array, upper - x) +1
        for y in array[i:j]:
            if x != y and lower <= x+y <= upper:
                counter[x + y] += 1
    return len(counter)