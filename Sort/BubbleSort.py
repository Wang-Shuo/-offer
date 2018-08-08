# three methods to implement bubble sort.

def BubbleSort1(Array):
    length = len(Array)

    for i in range(length):
        for j in range(1, length-i):
            if Array[j-1] > Array[j]:
                Array[j-1], Array[j] = Array[j], Array[j-1]


def BubbleSort2(Array):
    length = len(Array)

    flag = True
    k = length

    while flag:
        flag = False
        for i in range(1, k):
            if Array[i-1] > Array[i]:
                Array[i-1], Array[i] = Array[i], Array[i-1]
                flag = True
        k -= 1



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
#BubbleSort2(Array)
BubbleSort3(Array)
print(Array)