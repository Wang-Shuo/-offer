def Partition1(Array, start, end):
    pivot = Array[start]

    split = start
    for i in range(start + 1, end + 1):
        if Array[i] <= pivot:
            split += 1
            if split != i:
                Array[i], Array[split] = Array[split], Array[i]
    
    Array[start], Array[split] = Array[split], Array[start]
    return split


def Partition2(Array, start, end):
    pivot = Array[start]

    while start < end:
        while start < end and Array[end] >= pivot:
            end -= 1
        Array[start] = Array[end]
        while start < end and Array[start] <= pivot:
            start += 1
        Array[end] = Array[start]
    
    Array[start] = pivot
    return start


# recursive implementation
def QuickSort(Array, start, end):
    if start < end:
        split = Partition2(Array, start, end)
        QuickSort(Array, start, split - 1)
        QuickSort(Array, split + 1, end)


# iterative implementation
def QuickSort(Array):
    if len(Array) < 2:
        return Array
    
    stack = []
    stack.append(len(Array)-1)
    stack.append(0)
    while stack:
        start = stack.pop()
        end = stack.pop()
        index = Partition1(Array, start, end)
        if start < index - 1:
            stack.append(index - 1)
            stack.append(start)
        if end > index + 1:
            stack.append(end)
            stack.append(index + 1)


# test
Array = [2, 4, 1, 5, 6, 8, 7]
QuickSort(Array)
print(Array)
