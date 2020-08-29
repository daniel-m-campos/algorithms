import heapq


def median_update(value, low_heap, high_heap):
    if not low_heap:
        heapq.heappush(low_heap, -value)
        return -low_heap[0]
    if low_heap and not high_heap:
        if value <= -low_heap[0]:
            heapq.heappush(high_heap, -heapq.heappushpop(low_heap, -value))
        else:
            heapq.heappush(high_heap, value)
        return -low_heap[0]

    if value <= -low_heap[0]:
        heapq.heappush(low_heap, -value)
    else:
        heapq.heappush(high_heap, value)

    len_diff = len(low_heap) - len(high_heap)
    if len_diff > 1:
        heapq.heappush(high_heap, -heapq.heappop(low_heap))
    elif len_diff < -1:
        heapq.heappush(low_heap, -heapq.heappop(high_heap))
    if len(low_heap) >= len(high_heap):
        return -low_heap[0]
    else:
        return high_heap[0]
