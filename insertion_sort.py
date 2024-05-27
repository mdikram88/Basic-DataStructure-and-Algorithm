def insertion_sort(arr: list):
    array = arr.copy()    

    n = len(array)
    for i in range(1,n):
        insert_index = i
        current_value = array[i]
        for j in range(i-1, -1, -1):
            if array[j] > current_value:
                array[j+1] = array[j]
                insert_index = j
            else:
                break
        array[insert_index] = current_value

    
    return array
arry = [2, 5, 12, 6, 8, 7, 1, 9, 10, 3]
arr_2 = [7, 3, 9, 12, 11]

print("Array before sorting: ", arry)

new_array = insertion_sort(arry)
print("Array after sorting: ", new_array)