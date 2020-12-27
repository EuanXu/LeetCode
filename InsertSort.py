def insert_sort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
                break
    return array


def shell_sort(array):
    gap = len(array)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(array)):
            for j in range(i % gap, i, gap):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
    return array


if __name__ == '__main__':
    list1 = [4, 5, 6, 7, 3, 2, 6, 9, 8]
    print(insert_sort(list1))
    print(shell_sort(list1))
