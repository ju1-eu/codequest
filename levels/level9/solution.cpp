// Lösung: Implementiere den Algorithmus der linearen Suche

#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>

int linear_search(const std::vector<int>& arr, int x) {
    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] == x) {
            return i;
        }
    }
    return -1;
}

int main() {
    std::vector<int> arr = {2, 3, 4, 10, 40};
    int x = 10;

    auto start_time = std::chrono::high_resolution_clock::now();
    int result = linear_search(arr, x);
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> time_taken = end_time - start_time;

    if (result != -1) {
        std::cout << "Element gefunden an Index: " << result << std::endl;
    } else {
        std::cout << "Element nicht gefunden" << std::endl;
    }
    std::cout << "Zeit für die lineare Suche: " << std::fixed << std::setprecision(3) << time_taken.count() << " ms" << std::endl;

    // Test mit einer großen Liste
    std::vector<int> large_arr(1000000);
    for (int i = 0; i < 1000000; ++i) {
        large_arr[i] = i + 1;
    }
    x = 999999;

    start_time = std::chrono::high_resolution_clock::now();
    result = linear_search(large_arr, x);
    end_time = std::chrono::high_resolution_clock::now();
    time_taken = end_time - start_time;

    std::cout << "\nTest mit großer Liste:" << std::endl;
    if (result != -1) {
        std::cout << "Element gefunden an Index: " << result << std::endl;
    } else {
        std::cout << "Element nicht gefunden" << std::endl;
    }
    std::cout << "Zeit für die lineare Suche: " << std::fixed << std::setprecision(3) << time_taken.count() << " ms" << std::endl;

    return 0;
}
