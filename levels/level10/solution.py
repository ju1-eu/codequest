# Lösung: Implementiere den Algorithmus der binären Suche

import time

def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def measure_time(func, arr, x):
    start_time = time.time()
    result = func(arr, x)
    end_time = time.time()
    return result, (end_time - start_time) * 1000

# Teste den Algorithmus der binären Suche
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    result, time_taken = measure_time(binary_search, arr, x)
    if result != -1:
        print("Element gefunden an Index:", result)
    else:
        print("Element nicht gefunden")
    print(f"Zeit für die binäre Suche: {format(time_taken, '.3f')} ms")

    # Test mit einer großen sortierten Liste
    large_arr = sorted([i for i in range(1, 1000001)])
    x = 999999
    result, time_taken = measure_time(binary_search, large_arr, x)
    print("\nTest mit großer Liste:")
    if result != -1:
        print("Element gefunden an Index:", result)
    else:
        print("Element nicht gefunden")
    print(f"Zeit für die binäre Suche: {format(time_taken, '.3f')} ms")
