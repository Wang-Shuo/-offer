def SelectionSort(Array):
    length = len(Array)

    for i in range(length):
        minIdx = i
        for j in range(i+1, length):
            if Array[j] < Array[minIdx]:
                minIdx = j
        
        Array[i], Array[minIdx] = Array[minIdx], Array[i]


# test
Array = [2, 4, 1, 5, 6, 8, 7]
SelectionSort(Array)
print(Array)