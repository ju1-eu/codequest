# Aufgabe: Implementiere den Selection Sort Algorithmus
# Dein Code beginnt hier

import time

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return (end_time - start_time) * 1000

# Teste den Selection Sort Algorithmus
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    selection_sort(arr)
    print("Sortierte Liste:", arr)

    # Teste den Algorithmus und messe die Zeit
    large_arr = [i for i in range(1000, 0, -1)]
    time_taken = measure_time(selection_sort, large_arr)
    print("\nTest mit großer Liste:")
    print("Sortierte Liste:", large_arr[:10], "...", large_arr[-10:])  # Zeige nur einen Teil der Liste
    print(f"Zeit für Selection Sort: {format(time_taken, '.3f')} ms")
