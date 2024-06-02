from numpy import random

arr = random.randint(1, 10, size=10)

def counting_sort(arr):
    lt = [0] * (max(arr) + 1)
    
    while len(arr) > 0:
        n = arr.pop(0)
        lt[n] += 1

    for i in range(len(lt)):
        while lt[i] > 0:
            arr.append(i)
            lt[i] -= 1

    return arr

print("Array Before:", arr)
print()
print(counting_sort(arr.tolist()))