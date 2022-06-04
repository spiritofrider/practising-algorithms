def quickSort(arr):
    if len(arr) <2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i<pivot]
        greater = [i for i in arr[1:] if i>pivot]
        return quickSort(lesser) + [pivot] + quickSort(greater)


print(quickSort([21,1,43,2,7,33,89,65,12,19,17,80]))