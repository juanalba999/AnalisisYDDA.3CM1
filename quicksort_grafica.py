import random
import time
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def measure_quicksort_time(arr):
    start_time = time.time()
    quicksort(arr)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    random.seed(42)
    array_sizes = [random.randint(1, 100) for _ in range(100)]
    execution_times = []

    for size in array_sizes:
        random_array = generate_random_array(size)
        execution_time = measure_quicksort_time(random_array)
        execution_times.append(execution_time)

    plt.plot(array_sizes, execution_times, 'ro-')
    plt.title("Tiempo de ejecución QuickSort con arreglos aleatorios")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo de ejecución (en segundos)")
    plt.show()
