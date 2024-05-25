// Lösung: Erweitere den Code aus Level 16, um Fehlerbehandlung und Debugging-Informationen hinzuzufügen.

#include <iostream>
#include <stdexcept>

// Funktion zur Berechnung der Summe
int summe_berechnen(int a, int b) {
    return a + b;
}

// Funktion zur Berechnung des Produkts
int produkt_berechnen(int a, int b) {
    return a * b;
}

// Hauptfunktion
int main() {
    try {
        int zahl1, zahl2;

        // Eingabe der ersten Zahl
        std::cout << "Geben Sie die erste Zahl ein: ";
        if (!(std::cin >> zahl1)) {
            throw std::invalid_argument("Ungültige Eingabe für zahl1.");
        }

        // Eingabe der zweiten Zahl
        std::cout << "Geben Sie die zweite Zahl ein: ";
        if (!(std::cin >> zahl2)) {
            throw std::invalid_argument("Ungültige Eingabe für zahl2.");
        }

        // Debugging-Ausgabe
        std::cerr << "Debug: Eingaben sind " << zahl1 << " und " << zahl2 << std::endl;

        // Berechnung und Ausgabe der Summe
        int summe = summe_berechnen(zahl1, zahl2);
        std::cout << "Die Summe ist: " << summe << std::endl;

        // Berechnung und Ausgabe des Produkts
        int produkt = produkt_berechnen(zahl1, zahl2);
        std::cout << "Das Produkt ist: " << produkt << std::endl;
    } catch (const std::exception &e) {
        std::cerr << "Fehler: " << e.what() << std::endl;
    }

    return 0;
}
