// Lösung: Erstelle ein Struktogramm für ein Programm, das mehrere Funktionen enthält (z.B. eine Funktion zur Berechnung der Summe und eine zur Berechnung des Produkts von zwei Zahlen).

#include <iostream>

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
    int zahl1, zahl2;

    // Eingabe der ersten Zahl
    std::cout << "Geben Sie die erste Zahl ein: ";
    std::cin >> zahl1;

    // Eingabe der zweiten Zahl
    std::cout << "Geben Sie die zweite Zahl ein: ";
    std::cin >> zahl2;

    // Berechnung und Ausgabe der Summe
    int summe = summe_berechnen(zahl1, zahl2);
    std::cout << "Die Summe ist: " << summe << std::endl;

    // Berechnung und Ausgabe des Produkts
    int produkt = produkt_berechnen(zahl1, zahl2);
    std::cout << "Das Produkt ist: " << produkt << std::endl;

    return 0;
}
