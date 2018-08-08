def InsertSort(Array):
    length = len(Array)
    
    for i in range(1, length):
        key = Array[i]
        j = i - 1
        while j >= 0 and Array[j] > key:
            Array[j+1] = Array[j]
            j -= 1
        Array[j+1] = key


# test 
Array = [2, 4, 1, 5, 6, 8, 7]
InsertSort(Array)
print(Array)
