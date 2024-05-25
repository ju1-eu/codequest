// Aufgabe: Vergleiche und optimiere die Algorithmen Bubble Sort und Quick Sort
// Dein Code beginnt hier

#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include <algorithm>
#include <stdlib.h>

void bubble_sort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped)
            break;
    }
}

void quick_sort(std::vector<int>& arr, int left, int right) {
    int i = left, j = right;
    int pivot = arr[(left + right) / 2];
    while (i <= j) {
        while (arr[i] < pivot)
            i++;
        while (arr[j] > pivot)
            j--;
        if (i <= j) {
            std::swap(arr[i], arr[j]);
            i++;
            j--;
        }
    }
    if (left < j)
        quick_sort(arr, left, j);
    if (i < right)
        quick_sort(arr, i, right);
}

void print_memory_usage() {
    // This function is designed to be used with valgrind for more precise memory usage measurements.
    std::cout << "Memory usage can be measured with tools like valgrind." << std::endl;
}

int main() {
    std::vector<int> large_arr(3000);  // Listengröße
    std::generate(large_arr.begin(), large_arr.end(), []() { return rand() % 1000; });

    // Test mit großer Liste
    std::cout << "Test mit großer Liste:" << std::endl;

    auto start_time = std::chrono::high_resolution_clock::now();
    bubble_sort(large_arr);
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> bubble_sort_time = end_time - start_time;
    std::cout << "Bubble Sort Zeit: " << std::fixed << std::setprecision(3) << bubble_sort_time.count() << " ms" << std::endl;

    print_memory_usage(); // Platzhalter, sollte mit valgrind gemessen werden

    std::generate(large_arr.begin(), large_arr.end(), []() { return rand() % 1000; });

    start_time = std::chrono::high_resolution_clock::now();
    quick_sort(large_arr, 0, large_arr.size() - 1);
    end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> quick_sort_time = end_time - start_time;
    std::cout << "Quick Sort Zeit: " << std::fixed << std::setprecision(3) << quick_sort_time.count() << " ms" << std::endl;

    print_memory_usage(); // Platzhalter, sollte mit valgrind gemessen werden

    // Zusammenfassung der Ergebnisse
    std::cout << "\nZusammenfassung der Ergebnisse:" << std::endl;
    std::cout << "Bubble Sort Zeit (C++): " << std::fixed << std::setprecision(3) << bubble_sort_time.count() << " ms" << std::endl;
    std::cout << "Quick Sort Zeit (C++): " << std::fixed << std::setprecision(3) << quick_sort_time.count() << " ms" << std::endl;

    // Vergleich der Algorithmen
    std::cout << "\nVergleich der Algorithmen:" << std::endl;
    std::cout << "Bubble Sort vs Quick Sort (C++):" << std::endl;
    std::cout << "Bubble Sort ist " << std::fixed << std::setprecision(1) << (bubble_sort_time.count() / quick_sort_time.count()) << " Mal langsamer als Quick Sort in C++." << std::endl;

    return 0;
}
