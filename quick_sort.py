def quick_sort(array):
    def partition(arr, low, high):
        pivot = arr[high]
        left_wall = low - 1
        
        for i in range(low, high):
            if arr[i] <= pivot:
                left_wall += 1
                arr[i], arr[left_wall] = arr[left_wall], arr[i]
    

        arr[left_wall + 1], arr[high] = arr[high], arr[left_wall+1]
        return left_wall + 1


    def quick_sort_helper(arr, low=0, high=None):
        if not high:
            high = len(arr) - 1
            
        if low < high:
            pivot_index = partition(arr, low, high)
            quick_sort_helper(arr, low, pivot_index - 1)
            quick_sort_helper(arr, pivot_index + 1, high)

    quick_sort_helper(array, 0, len(array) - 1)
    return array

array = [11, 2, 5, 12, 6, 8, 7, 1, 9, 10, 3]
print("Quick Sort:\n", quick_sort(array))