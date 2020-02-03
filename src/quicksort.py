def partition_one(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            a_i, a_j = array[i], array[j]
            array[i], array[j] = a_j, a_i
    a_i, a_r = array[i + 1], array[r]
    array[i + 1], array[r] = a_r, a_i
    return i + 1


def quick_sort(array, p, r, partition_fn, counts=None):
    if counts:
        counts[0] += len(array) - 1
    if p < r:
        q = partition_fn(array, p, r)
        quick_sort(array, p, q - 1, partition_fn, counts)
        quick_sort(array, q + 1, r, partition_fn, counts)
