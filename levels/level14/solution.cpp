// Lösung: Übersetze das Struktogramm aus Level 13 in funktionierenden C++ und Python-Code.

#include <iostream>

int main() {
    int zahl1, zahl2, summe;

    std::cout << "Geben Sie die erste Zahl ein: ";
    std::cin >> zahl1;

    std::cout << "Geben Sie die zweite Zahl ein: ";
    std::cin >> zahl2;

    summe = zahl1 + zahl2;

    std::cout << "Die Summe ist: " << summe << std::endl;

    return 0;
}
