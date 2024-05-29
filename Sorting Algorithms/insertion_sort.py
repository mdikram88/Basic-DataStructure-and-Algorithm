def insertion_sort(arr: list):
    array = arr.copy()    

    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]

    
    return array
arry = [2, 5, 12, 6, 8, 7, 1, 9, 10, 3]
arr_2 = [7, 3, 9, 12, 11]

print("Array before sorting: ", arry)

new_array = insertion_sort(arry)
print("Array after sorting: ", new_array)