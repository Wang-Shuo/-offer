def ShellSort(Array):
    length = len(Array)

    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            temp = Array[i]
            j = i
            while j >= gap and Array[j-gap] > temp:
                Array[j] = Array[j-gap]
                j -= gap
            Array[j] = temp
        gap = gap // 2


def ShellSort(A):
    n = len(A)

    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j-gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
        gap = gap // 2

# test
Array = [2, 4, 1, 5, 6, 8, 7]
ShellSort(Array)
print(Array)

