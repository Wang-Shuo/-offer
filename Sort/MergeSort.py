
def Merge(left, right):
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    merged.extend(left if left else right)
    return merged


# recursive implementation
def MergeSort1(Array):
    
    if len(Array) <= 1:
        return Array
    
    mid = len(Array) // 2
    left = MergeSort1(Array[:mid])
    right = MergeSort1(Array[mid:])
    return Merge(left, right)

# iterative implementation 
def MergeSort2(Array):
    length = len(Array)
    step = 1

    while step < length:
        for left in range(0, length-step, 2 * step):
            result = Merge(Array[left: left + step], Array[left + step: min(left + 2 * step, length)])
            Array = Array[0:left] + result + Array[min(left + 2 * step, length):]
        step *= 2
    
    return Array




# test 
Array = [2, 4, 1, 5, 6, 8, 7]
print(MergeSort1(Array))
print(MergeSort2(Array))