def quick_sort(data, start, end):
    """
        Функция quick_sort осуществляет быструю сортировку.

        Аргументы:
            data - данные
            start - левый указатель
            end - правый указатель
    """

    if start >= end:
        return data

    i_pivot = partition(data, start, end - 1)

    data = quick_sort(data, start, i_pivot)

    data = quick_sort(data, i_pivot + 1, end)

    return data


def partition(data, start, end):
    """ arrange (left array < pivot) and (right array > pivot) """
    pivot = data[end]

    i_pivot = start

    for i in range(start, end):
        #
        if data[i] <= pivot:
            data[i_pivot], data[end] = data[end], data[i_pivot]
            i_pivot += 1

    data[i_pivot], data[end] = data[end], data[i_pivot]

    return i_pivot

def main():
    a = [1, 5, 2, 8, 23, 342, 234, 4, 4, 3,2 ,5, 4, 6,4]
    quick_sort(a, 0, len(a))
    print(a)

main()
