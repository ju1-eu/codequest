// Lösung: Implementiere den Bubble Sort Algorithmus

#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>

void bubble_sort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main() {
    std::vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    bubble_sort(arr);
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
    bubble_sort(large_arr);
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
    std::cout << "Zeit für Bubble Sort: " << std::fixed << std::setprecision(3) << time_taken.count() << " ms" << std::endl;

    return 0;
}
