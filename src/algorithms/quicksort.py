def partition_first(array, left, right):
    pivot = array[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i - 1], array[left] = array[left], array[i - 1]
    return i - 1


def partition_last(array, left, right):
    array[left], array[right] = array[right], array[left]
    return partition_first(array, left, right)


def get_median_index(array, left, right):
    length = right - left + 1
    middle = length // 2 - 1 if length % 2 == 0 else length // 2
    middle += left
    pivots = {array[i]: i for i in (left, middle, right)}
    sorted_values = sorted(list(pivots.keys()))
    median_index = pivots[sorted_values[1]]
    return median_index


def partition_median(array, left, right):
    median_index = get_median_index(array, left, right)
    array[left], array[median_index] = array[median_index], array[left]
    return partition_first(array, left, right)


def quick_sort(array, left, right, partition_fn, counts=None):
    if left < right:
        if counts:
            counts[0] += right - left
        p = partition_fn(array, left, right)
        quick_sort(array, left, p - 1, partition_fn, counts)
        quick_sort(array, p + 1, right, partition_fn, counts)
