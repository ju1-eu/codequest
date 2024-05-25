// Lösung: Führe ein Code-Review für den Code aus Level 17 durch und verbessere ihn durch Refactoring.

#include <iostream>
#include <stdexcept>

// Funktion zur Berechnung der Summe
int berechne_summe(int a, int b) {
    return a + b;
}

// Funktion zur Berechnung des Produkts
int berechne_produkt(int a, int b) {
    return a * b;
}

// Funktion zur Eingabe einer Zahl
int eingabe_zahl(const std::string& prompt) {
    int zahl;
    std::cout << prompt;
    if (!(std::cin >> zahl)) {
        throw std::invalid_argument("Ungültige Eingabe.");
    }
    return zahl;
}

// Hauptfunktion
int main() {
    try {
        int zahl1 = eingabe_zahl("Geben Sie die erste Zahl ein: ");
        int zahl2 = eingabe_zahl("Geben Sie die zweite Zahl ein: ");

        std::cerr << "Debug: Eingaben sind " << zahl1 << " und " << zahl2 << std::endl;

        int summe = berechne_summe(zahl1, zahl2);
        std::cout << "Die Summe ist: " << summe << std::endl;

        int produkt = berechne_produkt(zahl1, zahl2);
        std::cout << "Das Produkt ist: " << produkt << std::endl;
    } catch (const std::exception &e) {
        std::cerr << "Fehler: " << e.what() << std::endl;
    }

    return 0;
}
