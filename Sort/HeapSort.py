def Heapify(Array, n, i):
    largest = i
    left = 2 * i +1
    right = 2 * i + 2

    if left < n and Array[left] > Array[i]:
        largest = left

    if right < n and Array[right] > Array[largest]:
        largest = right

    if largest != i:
        Array[i], Array[largest] = Array[largest], Array[i]
        Heapify(Array, n, largest)


def HeapSort(Array):
    n = len(Array)

    for i in range(n//2, -1, -1):
        Heapify(Array, n, i)

    for i in range(n-1, 0, -1):
        Array[0], Array[i] = Array[i], Array[0]
        Heapify(Array, i, 0)


# test
Array = [2, 4, 1, 5, 6, 8, 7, 9]
HeapSort(Array)
print(Array)