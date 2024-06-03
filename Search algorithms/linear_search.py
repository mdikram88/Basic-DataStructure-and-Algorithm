from numpy import random

arr = random.randint(1, 8, size=10)

def linear_search(arr, target):
    for i, ele in enumerate(arr):
        if ele == target:
            return i

    return -1


print("Array: ", arr)
ind = linear_search(arr, 3)
if ind != -1:
    print(f"Target: 3 is present at index {ind}")
else:
    print("Target 3 not present in array")