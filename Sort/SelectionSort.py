
def SelectionSort(A):
    n = len(A)

    for i in range(n):
        minIdx = i
        for j in range(i+1, n):
            if A[j] < A[minIdx]:
                minIdx = j
        
        A[i], A[minIdx] = A[minIdx], A[i]

# test
Array = [2, 4, 1, 5, 6, 8, 7]
SelectionSort(Array)
print(Array)