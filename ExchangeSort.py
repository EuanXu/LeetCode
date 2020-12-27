def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def quick_sort(array):
    def recursive(begin, end):
        if begin > end:
            return
        l, r = begin, end
        pivot = array[l]
        while l < r:
            while l < r and array[r] > pivot:
                r -= 1
            while l < r and array[l] <= pivot:
                l += 1
            array[l], array[r] = array[r], array[l]
        array[l], array[begin] = pivot, array[l]
        recursive(begin, l - 1)
        recursive(r + 1, end)

    recursive(0, len(array) - 1)
    return array


if __name__ == '__main__':
    list1 = [4, 5, 6, 7, 3, 2, 6, 9, 8]
    print(bubble_sort(list1))
    print(quick_sort(list1))
