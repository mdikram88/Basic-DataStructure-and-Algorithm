def selection_sort(arr: list):
    array = arr.copy()    

    for i in range(len(array) - 1):
        m_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[m_index]:
                m_index = j

        array[i], array[m_index] = array[m_index], array[i]
    
    return array
arry = [2, 5, 12, 6, 8, 7, 1, 9, 10, 3]
arr_2 = [7, 3, 9, 12, 11]

print("Array before sorting: ", arry)

new_array = selection_sort(arry)
print("Array after sorting: ", new_array)