def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
            print "found smallest and its", arr[i], "and index", smallest_index
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
        print "in sort at index" , i, "newArr", newArr
    return newArr




print selectionSort([1, 3, 6, 5, 2, -1])
