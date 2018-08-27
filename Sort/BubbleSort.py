# three methods to implement bubble sort.

def BubbleSort1(A):
    n = len(A)

    for i in range(n-1, -1, -1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j] 



def BubbleSort2(A):
    n = len(A)

    for i in range(n-1, -1, -1):
        flag = 0
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                flag = 1
        if flag == 0:
            break


def BubbleSort3(Array):
    length = len(Array)

    flag = length
    while flag > 0:
        k = flag
        flag = 0
        for i in range(1, k):
            if Array[i-1] > Array[i]:
                Array[i-1], Array[i] = Array[i], Array[i-1]
                flag = i


# test
Array = [2, 5, 1, 3, 6, 8, 7]
#BubbleSort1(Array)
BubbleSort2(Array)
#BubbleSort3(Array)
print(Array)