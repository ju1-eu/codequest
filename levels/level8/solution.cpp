// Lösung: Implementiere den Selection Sort Algorithmus

#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>

void selection_sort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        std::swap(arr[min_idx], arr[i]);
    }
}

int main() {
    std::vector<int> arr = {64, 25, 12, 22, 11};
    selection_sort(arr);
    std::cout << "Sortierte Liste: ";
    for (int x : arr) {
        std::cout << x << " ";
    }
    std::cout << std::endl;

    // Teste den Algorithmus und messe die Zeit
    std::vector<int> large_arr(1000);
    for (int i = 0; i < 1000; ++i) {
        large_arr[i] = 1000 - i;
    }

    auto start_time = std::chrono::high_resolution_clock::now();
    selection_sort(large_arr);
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> time_taken = end_time - start_time;

    std::cout << "\nTest mit großer Liste:" << std::endl;
    std::cout << "Sortierte Liste: ";
    for (int i = 0; i < 10; ++i) {
        std::cout << large_arr[i] << " ";
    }
    std::cout << "... ";
    for (int i = 990; i < 1000; ++i) {
        std::cout << large_arr[i] << " ";
    }
    std::cout << std::endl;
    std::cout << "Zeit für Selection Sort: " << std::fixed << std::setprecision(3) << time_taken.count() << " ms" << std::endl;

    return 0;
}
