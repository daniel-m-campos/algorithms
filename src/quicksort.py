def partition_one(array, left, right):
    pivot = array[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < pivot:
            a_i, a_j = array[i], array[j]
            array[i], array[j] = a_j, a_i
            i += 1
    a_i, a_l = array[i - 1], array[left]
    array[i - 1], array[left] = a_l, a_i
    return i - 1


def quick_sort(array, left, right, partition_fn, counts=None):
    if counts:
        counts[0] += len(array) - 1
    if left < right:
        p = partition_fn(array, left, right)
        quick_sort(array, left, p - 1, partition_fn, counts)
        quick_sort(array, p + 1, right, partition_fn, counts)
