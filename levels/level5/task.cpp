// Aufgabe: Schreibe ein Programm, das zwei Zahlen multipliziert und das Ergebnis ausgibt.
// Dein Code beginnt hier.

#include <iostream>

int main() {
    int zahl1, zahl2, produkt;
    std::cout << "Gib die erste Zahl ein: ";
    std::cin >> zahl1;
    std::cout << "Gib die zweite Zahl ein: ";
    std::cin >> zahl2;
    produkt = zahl1 * zahl2;
    std::cout << "Das Produkt ist: " << produkt << std::endl;
    return 0;
}