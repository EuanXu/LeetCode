def select_sort(array):
    for i in range(len(array)):
        x = i
        for j in range(i, len(array)):
            if array[j] < array[x]:
                x = j
        array[i], array[x] = array[x], array[i]
    return array


def heap_sort(array):
    def heap_adjust(parent):
        child = 2 * parent + 1  # left child
        while child < len(heap):
            if child + 1 < len(heap):
                if heap[child + 1] > heap[child]:
                    child += 1  # right child
            if heap[parent] >= heap[child]:
                break
            heap[parent], heap[child] = \
                heap[child], heap[parent]
            parent, child = child, 2 * child + 1

    heap, array = array.copy(), []
    for i in range(len(heap) // 2, -1, -1):
        heap_adjust(i)
    while len(heap) != 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        array.insert(0, heap.pop())
        heap_adjust(0)
    return array


if __name__ == '__main__':
    list1 = [4, 5, 6, 7, 3, 2, 6, 9, 8]
    print(select_sort(list1))
    print(heap_sort(list1))
