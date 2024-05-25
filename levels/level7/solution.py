# Lösung: Implementiere den Bubble Sort Algorithmus

import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return (end_time - start_time) * 1000

# Teste den Bubble Sort Algorithmus
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Sortierte Liste:", arr)

    # Teste den Algorithmus und messe die Zeit
    large_arr = [i for i in range(1000, 0, -1)]
    time_taken = measure_time(bubble_sort, large_arr)
    print("\nTest mit großer Liste:")
    print("Sortierte Liste:", large_arr[:10], "...", large_arr[-10:])  # Zeige nur einen Teil der Liste
    print(f"Zeit für Bubble Sort: {format(time_taken, '.3f')} ms")
