from numpy import random

arr = random.randint(1, 100, size=10)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

def heap_sort(array):
    n = len(array)

    for i in range( n // 2 -1 , -1 , -1):
        heapify(array, n, i)

    for j in range(n-1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, j, 0)

heap_sort(arr)
print("Sorted Array:\n", arr)