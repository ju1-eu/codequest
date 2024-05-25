# Aufgabe: Implementiere den Quick Sort Algorithmus
# Dein Code beginnt hier

import time
import random
from memory_profiler import memory_usage

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_memory_and_time(func, arr):
    start_time = time.time()
    mem_usage = memory_usage((func, [arr.copy()]), interval=0.01)
    end_time = time.time()
    return (max(mem_usage) - min(mem_usage)) * 1024, (end_time - start_time) * 1000

# Teste den Quick Sort Algorithmus und analysiere Zeit- und Raumkomplexität
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    large_arr = [random.randint(1, 1000) for _ in range(3000)]  # Listengröße

    # Teste den Algorithmus
    print("Sortierte Liste:", quick_sort(arr))

    # Analysiere Zeit- und Raumkomplexität mit großer Liste
    quick_sort_mem, quick_sort_time = measure_memory_and_time(quick_sort, large_arr)
    print("\nTest mit großer Liste:")
    print("Quick Sort Zeit:", format(quick_sort_time, ".3f"), "ms")
    print("Quick Sort Speicher:", format(quick_sort_mem, ".3f"), "KB")

    # Zusammenfassung der Ergebnisse
    print("\nZusammenfassung der Ergebnisse:")
    print(f"Quick Sort Zeit (Python): {format(quick_sort_time, '.3f')} ms")
    print(f"Quick Sort Speicher (Python): {format(quick_sort_mem, '.3f')} KB")
