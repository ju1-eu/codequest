# Aufgabe: Implementiere den Algorithmus der linearen Suche
# Dein Code beginnt hier

import time

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def measure_time(func, arr, x):
    start_time = time.time()
    result = func(arr, x)
    end_time = time.time()
    return result, (end_time - start_time) * 1000

# Teste den Algorithmus der linearen Suche
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    result, time_taken = measure_time(linear_search, arr, x)
    if result != -1:
        print("Element gefunden an Index:", result)
    else:
        print("Element nicht gefunden")
    print(f"Zeit für die lineare Suche: {format(time_taken, '.3f')} ms")

    # Test mit einer großen Liste
    large_arr = [i for i in range(1, 1000001)]
    x = 999999
    result, time_taken = measure_time(linear_search, large_arr, x)
    print("\nTest mit großer Liste:")
    if result != -1:
        print("Element gefunden an Index:", result)
    else:
        print("Element nicht gefunden")
    print(f"Zeit für die lineare Suche: {format(time_taken, '.3f')} ms")
