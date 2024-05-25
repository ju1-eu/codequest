// Aufgabe: Erstelle ein Programm, das die Summe von zwei Zahlen berechnet und ausgibt.
// Dein Code beginnt hier

#include <iostream>
#include <stdexcept>

int main() {
    try {
        int zahl1, zahl2, summe;

        std::cout << "Geben Sie die erste Zahl ein: ";
        if (!(std::cin >> zahl1)) {
            throw std::invalid_argument("Ungültige Eingabe für zahl1.");
        }

        std::cout << "Geben Sie die zweite Zahl ein: ";
        if (!(std::cin >> zahl2)) {
            throw std::invalid_argument("Ungültige Eingabe für zahl2.");
        }

        summe = zahl1 + zahl2;

        std::cout << "Die Summe ist: " << summe << std::endl;
    } catch (const std::exception &e) {
        std::cerr << "Fehler: " << e.what() << std::endl;
    }

    return 0;
}
