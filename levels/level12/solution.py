# Lösung: Vergleiche und optimiere die Algorithmen Bubble Sort und Quick Sort

import time
import random
from memory_profiler import memory_usage

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

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

# Teste und vergleiche die Algorithmen
if __name__ == "__main__":
    large_arr = [random.randint(1, 1000) for _ in range(3000)]  # Listengröße

    # Test mit großer Liste
    print("Test mit großer Liste:")

    bubble_sort_mem, bubble_sort_time = measure_memory_and_time(bubble_sort, large_arr)
    print("Bubble Sort Zeit:", format(bubble_sort_time, ".3f"), "ms")
    print("Bubble Sort Speicher:", format(bubble_sort_mem, ".3f"), "KB")

    quick_sort_mem, quick_sort_time = measure_memory_and_time(quick_sort, large_arr)
    print("Quick Sort Zeit:", format(quick_sort_time, ".3f"), "ms")
    print("Quick Sort Speicher:", format(quick_sort_mem, ".3f"), "KB")

    # Zusammenfassung der Ergebnisse
    print("\nZusammenfassung der Ergebnisse:")
    print(f"Bubble Sort Zeit (Python): {format(bubble_sort_time, '.3f')} ms")
    print(f"Bubble Sort Speicher (Python): {format(bubble_sort_mem, '.3f')} KB")
    print(f"Quick Sort Zeit (Python): {format(quick_sort_time, '.3f')} ms")
    print(f"Quick Sort Speicher (Python): {format(quick_sort_mem, '.3f')} KB")

    # Vergleich der Algorithmen
    print("\nVergleich der Algorithmen:")
    print(f"Bubble Sort vs Quick Sort (Python):")
    print(f"Bubble Sort ist {format(bubble_sort_time / quick_sort_time, '.1f')} Mal langsamer als Quick Sort in Python.")
    if quick_sort_mem > 0:
        print(f"Bubble Sort verwendet {format(bubble_sort_mem / quick_sort_mem, '.1f')} Mal mehr Speicher als Quick Sort in Python.")
    else:
        print("Quick Sort hat keinen zusätzlichen Speicher verwendet.")
