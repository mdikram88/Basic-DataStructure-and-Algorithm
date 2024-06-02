def merge_sort(array):
    def merge(left, right):
        merged = []
        i = j = 0

        while i< len(left) and j< len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged
    
    
    def merge_sort_help(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        sortedLeft = merge_sort_help(left)
        sortedRight = merge_sort_help(right)

        return merge(sortedLeft, sortedRight)


    return merge_sort_help(array)


array = [11, 2, 5, 12, 6, 8, 7, 1, 9, 10, 3]
print("Merge Sort\n:", merge_sort(array))