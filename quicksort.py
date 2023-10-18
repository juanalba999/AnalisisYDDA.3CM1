import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

arr_list = []
for _ in range(100):
    size = random.randint(1, 100)
    arr = [random.randint(1, 100) for _ in range(size)]
    arr_list.append(arr)

sorted_arr_list = [quicksort(arr) for arr in arr_list]

for i, arr in enumerate(sorted_arr_list):
    print(f"Arreglo {i + 1}: {arr}")
